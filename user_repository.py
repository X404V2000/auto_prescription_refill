from dbase_creds import get_db_connection

LOCKOUT_THRESHOLD = 5      # max failed attempts allowed
LOCKOUT_WINDOW_MIN = 15    # minutes to look back when counting failed attempts

class UserRepository:
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    ##Database layer for authentication — maps to the DATABASE box in the auth design.##
    ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>##
    def fetch_user_by_username(self, username):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "SELECT id, password_hash FROM medicUsr WHERE usrname = %s",
                (username,)
            )
            return cursor.fetchone()
        finally:
            cursor.close()
            conn.close()

    def record_login_attempt(self, username, success):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO login_attempts (usrname, success) VALUES (%s, %s)",
                (username, success)
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()

    def is_account_locked(self, username):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                SELECT COUNT(*) FROM login_attempts
                WHERE usrname = %s
                  AND success = FALSE
                  AND attempted_at >= (NOW() - INTERVAL %s MINUTE)
                """,
                (username, LOCKOUT_WINDOW_MIN)
            )
            failed_count = cursor.fetchone()[0]
            return failed_count >= LOCKOUT_THRESHOLD
        finally:
            cursor.close()
            conn.close()
