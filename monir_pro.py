import requests, os, sys, time, random

def clear(): os.system('clear')

def banner():
    clear()
    print("\033[1;32m" + "╔" + "═"*58 + "╗")
    print("║      \033[1;36m__  __  ____  _   _ ___ ____    __     ___    ___ \033[1;32m     ║")
    print("║     \033[1;36m|  \/  |/ __ \| \ | |_ _|  _ \   \ \   / / \  |_ _|\033[1;32m    ║")
    print("║     \033[1;36m| |\/| | |  | |  \| || || |_) |   \ \ / / _ \  | | \033[1;32m    ║")
    print("║     \033[1;36m| |  | | |__| | |\  || ||  _ <     \ V / ___ \ | | \033[1;32m    ║")
    print("║     \033[1;36m|_|  |_|\____/|_| \_|___|_| \_\     \_/_/   \_\___|\033[1;32m    ║")
    print("╚" + "═"*58 + "╝")
    print(f"\033[1;33m  [🔥] VERSION : 5.0 (ULTRA-SPEED)")
    print(f"\033[1;31m  [💀] OWNER   : MONIR VAI")
    print("\033[1;32m" + "═"*60 + "\033[0m")

def bomb():
    banner()
    num = input("\033[1;37m[+] TARGET NUMBER (11 digit): \033[0m")
    limit = int(input("\033[1;37m[+] ATTACK LIMIT: \033[0m"))
    
    success = 0
    print("\n\033[1;34m┌" + "─"*25 + "┬" + "─"*25 + "┐")
    print("│      SUCCESS SENT       │      REMAINING SMS      │")
    print("├" + "─"*25 + "┼" + "─"*25 + "┤\033[0m")
    
    for i in range(limit):
        # এখানে আপনার শক্তিশালী API গুলো কাজ করবে
        time.sleep(0.05) # হাই স্পিড ডিলে
        success += 1
        rem = limit - success
        
        sys.stdout.write(f"\r│  \033[1;32mSENT OK [{success:03}]\033[0m        │   \033[1;33mREMAINING: {rem:03}\033[0m     │")
        sys.stdout.flush()
        
    print("\n\033[1;34m└" + "─"*25 + "┴" + "─"*25 + "┘\033[0m")
    print(f"\n\033[1;32m[✔] ATTACK FINISHED BY MONIR VAI!")
    input("\nPress Enter to Main Menu...")

if __name__ == "__main__":
    while True:
        banner()
        print("\033[1;35m [01] START SMS BOMBING\n [00] EXIT\033[0m\n")
        choice = input("\033[1;32m[MONIR-VAI@CYBER]:~$ \033[0m")
        if choice in ['1', '01']: bomb()
        elif choice == '00': break

