import bcrypt
import random
import json
from apiCall import InvalidOperationResponse, ValidOperationResponse
from dbase import get_db_connection, hash_password, save_user

class create_usr:
    def __init__(self, first_name: str=None last_name: str=None user_name: str=None date_of_birt: str=None email: str=None cell_number: str=None password: str=None):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.cell_number = cell_number
        self.password = password

    def usr_form(self):
        print("Please fill in the follow ing form")
        try:
            name = input("Enter your name: ").strip().title()
            surname = input("Enter your surname: ").strip().title()
            
            ##auto generate username
            first_char = name[0:2]
            if len(surname) >= 4:
                second_char = surname[3:-1]
            else:
                second_char = surname[-1:]

            last_char = random.randint(1000, 9999)
            ##final outcome
            usrname = str(first_char + second_char + str(last_char))

            dob = input("Enter your date of birth ... e.g., 23/09/1999: ").strip()
            email = input("Enter your email: ").strip()
            phone = input("Enter your phone number: ").strip()
            print("Almost done")
            print("Please create a login password for your account")
            password = input("Create login password: ")

            ##hash password
            password_bytes = password.encode('utf-8')
            hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
            password_hash = hashed.decode('utf-8')
            
            response = {
                    "status ": "success",
                    "message": "User profile created successful",
                    "Name           ": name,
                    "Surname        ": surname,
                    "Date of Birth  ": dob,
                    "Email          ": email,
                    "Phone number   ": phone
            })

            print(f"Thank you for being part of the family, {usrname}")
            return json.dumps(response, indent=2)

        except Exception as e:
            error_response = InvalidOperationResponse.usrDisplay(
                    400,
                    "Bad Request",
                    "Server cannot process the request"
                )
            print(json.dumps(error_response, indent=2))
            return json.dumps(error_response)
            
    def usrData_toDBase(self, name, surname, usrname, dob, email, phone, password_hash):
        ##write usr_data to dbase
        #connect to dbase
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO medicUsr (first_name, surname, usrname, dob, email, cell_number, password_hash)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        values = (name, surname, usrname, dob, email, phone, password_hash)

        try:
            cursor.execute(sql, values)
            conn.commit()
            print(...)  ##generate new response altinative to 'user data saved to dbase
        except Exception as e:
            print(...)  ##generate new response altinative to 'user data saved to dbase
            raise
        finally:
            cursor.close()
            conn.close()

