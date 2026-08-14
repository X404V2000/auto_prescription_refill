from fastapi import FastAPI

app = FastAPI()

## cli colors
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def menu():
    print(f"{RED}={RESET}"*60 + f"\n{GREEN}OpenX Medic{RESET}\n" + f"{RED}={RESET}"*60)
    ## patient argument
    print(f"{RED}[1]{RESET}{GREEN}. Talk to medic autobot.{RESET}")
    print(f"{RED}[2]{RESET}{GREEN}. Track your request.{RESET}")
    print(f"{RED}[3]{RESET}{GREEN}. Exit{RESET}")
    print(f"{RED}={RESET}")

def main():
    while True:
        menu()

        try:
            menu_arg = int(input("Choose option 1-3: "))
        except Exception:
            return {
                "Error message": "Invalid Input ... choose 1-3",
                "Error code": "Error 500"
            }
            continue 
        if menu_arg == 1:
            ## call function
            print("testing")
        elif menu_arg == 2:
            ## call function
            print("testing")
        elif menu_arg == 3:
            ## call function
            print("testing")
            break
        else:
            continue

if __name__ == "__main__":
    main()
