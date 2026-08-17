from autobot_arg import arg

## cli colors
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

class sysbot:
    @staticmethod
    def main_arg():
        while True:
            try:
                sys_arg = input("Patient healthcare ID: ").strip()
            except ValueError:
                print("Choose y/N")
                continue

            if not sys_arg:
                continue
            else:
                break

    def menu():
    print(f"{RED}={RESET}"*60 + f"\n{GREEN}OpenX Medic{RESET}\n" + f"{RED}={RESET}"*60)
    print(f"{RED}[1]{RESET}{GREEN}. refill prescription.{RESET}")
    print(f"{RED}[2]{RESET}{GREEN}. Other.{RESET}")
    print(f"{RED}[3]{RESET}{GREEN}. Exit{RESET}")
    print(f"{RED}={RESET}")
        
    def bot_isTrue():
        if sys_arg == y or sys_arg == Y:

            while True:
                try:
                    pat_fullname = input("Patient fullname: ").strip().title()
                except ValueError:
                    print("Invalid Error")
                    continue
                
                if menu_arg == 1:
                    arg.arg_ifTrue()
                    
    def bot_isFalse():
        if sys_arg == n or sys_arg == N:
            return {"testing ... returning unsuccessful"}

if __name__ == "__main_arg__":
    main_arg()
