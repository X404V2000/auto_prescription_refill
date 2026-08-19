from dbase_creds import get_db_connection

def create_medicUsr_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DROP TABLE IF EXISTS medicUsr")
        print("Dropped old medicUsr table (if it existed)")

        cursor.execute("""
            CREATE TABLE medicUsr (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(50) NOT NULL,
                surname VARCHAR(50) NOT NULL,
                usrname VARCHAR(20) NOT NULL UNIQUE,
                dob VARCHAR(10) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                cell_number VARCHAR(20) NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        print("Created medicUsr table")

    except Exception as e:
        print(f"Failed to generate table: {e}")
        raise
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    create_medicUsr_table()
