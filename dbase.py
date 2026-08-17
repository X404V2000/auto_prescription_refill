import bcrypt
import mysql.connector
from create_profile import create_usr
from creds import host, user, password, database

# 1. DATABASE CONNECTION

def get_db_connection():
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

# ------------------------
# 3. SAVE USER TO MYSQL (Registration)
# ------------------------
def save_user(username, plain_text_password):
    """
    Stores ONLY the hash in the database. Never store the raw password.
    """
    # Generate the hash
    password_hash = hash_password(plain_text_password)
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # IMPORTANT: The column should be VARCHAR(255) to hold the long hash
    sql = "INSERT INTO users (username, password_hash) VALUES (%s, %s)"
    values = (username, password_hash)
    
    try:
        cursor.execute(sql, values)
        conn.commit()
        print(f"User {username} saved successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# ------------------------
# 4. CHECK PASSWORD ON LOGIN
# ------------------------
def login(username, plain_text_password):
    """
    Checks if the entered password matches the hash in MySQL.
    Returns True if correct, False otherwise.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Retrieve ONLY the hash for this username
    sql = "SELECT password_hash FROM users WHERE username = %s"
    cursor.execute(sql, (username,))
    result = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if result is None:
        print("Username not found.")
        return False
    
    # The hash stored in the database
    stored_hash = result[0].encode('utf-8')
    
    # The password the user just typed (convert to bytes)
    typed_password_bytes = plain_text_password.encode('utf-8')
    
    # bcrypt.checkpw() compares the typed password against the stored hash
    # It extracts the salt from the stored hash automatically
    if bcrypt.checkpw(typed_password_bytes, stored_hash):
        print("Login successful!")
        return True
    else:
        print("Invalid password.")
        return False

# ------------------------
# 5. EXAMPLE USAGE
# ------------------------
if __name__ == "__main__":
    # --- REGISTRATION ---
