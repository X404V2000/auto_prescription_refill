from fastapi import FastAPI
from apiCall import InvalidOperationResponse, ValidOperationResponse
from syslogGenerator import logger, write_toFilesys
from create_profile import create_usr
import sys

app = FastAPI()

## cli colors
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

## error handling arguments
def invalidReturn():
    invalidResponse = InvalidOperationResponse.usrDisplay(
            400,
            "Bad Request",
            "Server cannot process the request"
        )

def validReturn():
    validResponse = ValidOperationResponse.usrDisplay(
            200,
            "OK",
            "The request was successful"
        )
## error handling arguments

def display_main_menu():
    print(f"{RED}={RESET}"*60)
    print(f"{GREEN}Welcome to OpenX Medic{RESET}")
    print(f"{RED}={RESET}"*60)
    print(f"{RED}[1]{RESET}{GREEN}. Login.{RESET}")
    print(f"{RED}[2]{RESET}{GREEN}. Create Profile.{RESET}")
    print(f"{RED}[3]{RESET}{GREEN}. Forgot Password.{RESET}")
    print(f"{RED}[4]{RESET}{GREEN}. Exit{RESET}")
    print(f"{RED}={RESET}"*60)

def display_patient_menu():
    print(f"{RED}={RESET}"*60)
    print(f"{GREEN}OpenX Medic{RESET}")
    print(f"{RED}={RESET}"*60)
    print(f"{RED}[1]{RESET}{GREEN}. Request prescription.{RESET}")
    print(f"{RED}[2]{RESET}{GREEN}. Check notification.{RESET}")
    print(f"{RED}[3]{RESET}{GREEN}. Track prescription pick-up.{RESET}")
    print(f"{RED}[4]{RESET}{GREEN}. Exit{RESET}")
    print(f"{RED}={RESET}"*60)

def handle_login():
    logger.log_info("User attempting to login")
    
    ##checks credentials
    ##For now, just show patient menu
    while True:
        display_patient_menu()
        try:
            patient_choice = int(input("Choose option 1-4: "))
            
            if patient_choice == 1:
                logger.log_success("Patient requested prescription")
                print("Processing prescription request...")
                
            elif patient_choice == 2:
                logger.log_success("Patient checked notifications")
                print("Checking notifications...")
                
            elif patient_choice == 3:
                logger.log_success("Patient tracked prescription")
                print("Tracking prescription pick-up...")
                
            elif patient_choice == 4:
                logger.log_info("Patient logged out")
                print("Returning to main menu...")
                break
                
            else:
                logger.log_error(f"Invalid patient menu option: {patient_choice}")
                print("Invalid option. Please choose 1-4.")
                
        except ValueError as e:
            logger.handle_exception(e)
            print("Please enter a valid number (1-4).")
        
        input("\nPress Enter to continue...")

def main():
    """Main application entry point"""
    try:
        logger.log_info("Application started", details={"version": "1.0.0"})
        
        while True:
            display_main_menu()
            
            try:
                main_menuArg = int(input("Choose option 1-4: "))
                
                # Log the input
                if main_menuArg in [1, 2, 3, 4]:
                    write_toFilesys(main_menuArg, is_valid=True)
                else:
                    write_toFilesys(main_menuArg, is_valid=False)
                    invalidReturn()
                    continue
                
                # Handle menu options
                if main_menuArg == 1:
                    handle_login()
                
                elif main_menuArg == 2:
                    logger.log_info("Create Profile selected", menu_arg=2)
                    new_user = create_usr()
                    new_user.usr_form()
                
                elif main_menuArg == 3:
                    logger.log_info("Forgot Password selected", menu_arg=3)
                    print("Forgot Password feature coming soon...")
                
                elif main_menuArg == 4:
                    logger.log_info("Application shutting down", menu_arg=4)
                    print("System shutting-down...")
                    break
                
                else:
                    # This shouldn't happen due to validation
                    invalidReturn()
                
            except ValueError as e:
                logger.handle_exception(e, menu_arg=None)
                print("Invalid input. Please enter a number (1-4).")
                invalidReturn()
                continue
                
            except KeyboardInterrupt:
                logger.log_info("Application interrupted by user")
                print("\n\nExiting application...")
                break
                
            except Exception as e:
                logger.handle_exception(e)
                print(f"An unexpected error occurred: {e}")
                invalidReturn()
                continue
            
            input("\nPress Enter to continue...")
            
    except Exception as e:
        logger.log_error(f"Fatal error in main: {str(e)}")
        print(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
