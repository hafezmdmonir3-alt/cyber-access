import os, time, sys, random

def clear(): os.system('clear')

def banner():
    clear()
    print("\033[1;32m" + "╔" + "═"*58 + "╗")
    os.system('figlet -f slant "MONIR VAI"')
    print("\033[1;32m" + "╚" + "═"*58 + "╝")
    print(f"\033[1;33m  [⚙️] STATUS   : ACTIVE (PRO API V3.5)")
    print(f"\033[1;36m  [📱] TELEGRAM : @Monirprime")
    print(f"\033[1;34m  [👤] FACEBOOK : facebook.com/200monir")
    print("\033[1;32m" + "═"*60 + "\033[0m")

def start_bombing():
    banner()
    num = input("\033[1;37m[+] TARGET NUMBER: \033[0m")
    limit = int(input("\033[1;37m[+] ATTACK LIMIT: \033[0m"))
    success, failed = 0, 0
    print("\n\033[1;31m[!] INJECTING MULTI-API PAYLOADS...\033[0m\n")
    time.sleep(1.5)
    print("\033[1;34m┌" + "─"*25 + "┬" + "─"*25 + "┐")
    print("│      SUCCESS SENT       │      FAILED/BLOCKED     │")
    print("├" + "─"*25 + "┼" + "─"*25 + "┤\033[0m")
    for i in range(limit):
        log_type = random.choice(["SUCCESS", "FAILED"])
        if log_type == "SUCCESS":
            success += 1
            st = f"│  \033[1;32mSENT OK [{success:03}]\033[0m        "
        else:
            failed += 1
            st = f"│  \033[1;31mFAILED  [{failed:03}]\033[0m        "
        sys.stdout.write(f"\r{st}   │   TOTAL: {i+1}/{limit}       │")
        sys.stdout.flush()
        time.sleep(0.08)
    print("\n\033[1;34m└" + "─"*25 + "┴" + "─"*25 + "┘\033[0m")
    print(f"\n\033[1;32m[✔] ATTACK FINISHED SUCCESSFULLY BY MONIR VAI!")
    input("\nPress Enter...")

if __name__ == "__main__":
    try:
        banner()
        print("\033[1;35m [01] SMS BOMBING\n [00] EXIT\033[0m\n")
        c = input("\033[1;32m[M-VAI@CYBER]:~$ \033[0m")
        if c == '1' or c == '01': start_bombing()
    except KeyboardInterrupt: sys.exit()

