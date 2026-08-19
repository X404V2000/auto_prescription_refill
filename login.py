import uuid
import bcrypt
from apiCall import InvalidOperationResponse, ValidOperationResponse
from syslogGenerator import logger
from user_repository import UserRepository

class AuthenticationService:
    """
    Handles the login flow — maps to the AUTHENTICATION SERVICE box in the auth design.

    This is a terminal (level 1) app, so there's no separate frontend process —
    'client-side' credential collection and validation are folded in here rather
    than split into a real network-facing client. MFA and JWT/session signing are
    out of scope for now since there's no web layer to hand a token to yet.
    """

    def __init__(self):
        self.repo = UserRepository()

    def collect_credentials(self):
        username = input("Enter Username: ").strip()
        password = input("Enter Password: ")
        return username, password

    def validate_input(self, username, password):
        if not username or not password:
            return False
        if len(username) < 3 or len(password) < 6:
            return False
        return True

    def verify_password(self, username, password):
        if self.repo.is_account_locked(username):
            InvalidOperationResponse.usrDisplay(
                    403,
                    "Forbidden",
                    "Account locked due to too many failed attempts. Try again later."
                )
            logger.log_warning(f"Login blocked — account locked: {username}")
            return False

        user_row = self.repo.fetch_user_by_username(username)
        if not user_row:
            self.repo.record_login_attempt(username, False)
            InvalidOperationResponse.usrDisplay(400, "Bad Request", "Invalid username or password")
            logger.log_warning(f"Failed login attempt — unknown user: {username}")
            return False

        user_id, stored_hash = user_row
        success = bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))
        self.repo.record_login_attempt(username, success)

        if success:
            ValidOperationResponse.usrDisplay(200, "OK", "Login successful")
            logger.log_success(f"User logged in: {username}")
        else:
            InvalidOperationResponse.usrDisplay(400, "Bad Request", "Invalid username or password")
            logger.log_warning(f"Failed login attempt: {username}")

        return success

    def generate_session_token(self):
        ##simple session id — no JWT signing needed until there's a real web layer to consume it
        return str(uuid.uuid4())

    def login(self):
        username, password = self.collect_credentials()

        if not self.validate_input(username, password):
            InvalidOperationResponse.usrDisplay(400, "Bad Request", "Invalid username/password format")
            return None

        if self.verify_password(username, password):
            return self.generate_session_token()
        return None


if __name__ == "__main__":
    auth = AuthenticationService()
    token = auth.login()
    if token:
        print(f"Session token: {token}")
