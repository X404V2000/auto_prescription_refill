from fastapi import FastAPI
from apiCall import InvalidOperationResponse, ValidOperationResponse

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

def main_menu():
    while True:
        ##client login screen
        print(f"{RED}={RESET}"*60 + f"\n{GREEN}Welcome to OpenX Medic{RESET}\n" + f"{RED}={RESET}"*60)
        print(f"{RED}[1]{RESET}{GREEN}. Login.{RESET}")
        print(f"{RED}[2]{RESET}{GREEN}. Create Profile.{RESET}")
        print(f"{RED}[3]{RESET}{GREEN}. Forgot Password.{RESET}")
        print(f"{RED}[4]{RESET}{GREEN}. Exit{RESET}")
        print(f"{RED}={RESET}"*60)

        try:
            main_menuArg = int(input("Choose option 1-4: "))
        except ValueError:
            invalidReturn()
            continue

        ###############################################################################
        if main_menuArg == 1:
            ## if login True
            print(f"{RED}={RESET}"*60 + f"\n{GREEN}OpenX Medic{RESET}\n" + f"{RED}={RESET}"*60)
            ## patient argument
            print(f"{RED}[1]{RESET}{GREEN}. Request prescription.{RESET}")
            print(f"{RED}[2]{RESET}{GREEN}. Check notification.{RESET}")
            print(f"{RED}[3]{RESET}{GREEN}. Track prescription pick-up.{RESET}")
            print(f"{RED}[4]{RESET}{GREEN}. Exit{RESET}")
            print(f"{RED}={RESET}"*60)

        ################################################################################
        elif main_menuArg == 2:
            ##under-development
            print(...)

        ################################################################################
        elif main_menuArg == 3:
            ##under-development
            print(...)

        ################################################################################
        elif main_menuArg == 4:
            print("System shutting-down")

if __name__ == "__main__":
    main()
