from pypresence import Presence
import time
from colorama import Fore
import os
import sys

def main():
    os.system('clear')
    sys.stdout.write("\x1b]2;CustomRPC - Intel1337\x07")
    print(f"""                                               
{Fore.BLUE} _____         _                _____ _____ _____ 
{Fore.BLUE}|     |_ _ ___| |_ ___ _____   | __  |  _  |     |
{Fore.WHITE}|   --| | |_ -|  _| . |     |  |    -|   __|   --|
{Fore.WHITE}|_____|___|___|_| |___|_|_|_|  |__|__|__|  |_____|
{Fore.BLUE}                                               """)
    print(f"{Fore.WHITE}        Discord Rich Presence Maker :")
    print(f"""{Fore.WHITE}        Credits: github.com/intel1337
          
          """)
    client_id = input(f"{Fore.BLUE}Crpc@{Fore.WHITE}Enter Client ID>")
    large_image = input(f"{Fore.BLUE}Crpc@{Fore.WHITE}Enter your Large Image name>")
    large_text = input(f"{Fore.BLUE}Crpc@{Fore.WHITE}Enter your Large Text>")
    state = input(f"{Fore.BLUE}Crpc@{Fore.WHITE}Enter your State>")
    start = int(time.time())
    RPC = Presence(client_id)
    RPC.connect()

    while True:
        RPC.update(
            large_image=large_image,
            large_text=large_text,
            state=state,
            start=start,
        )
        print(f"{Fore.GREEN}> Connected to Discord API")
        time.sleep(15)

    while False:
        if RPC.connection_timeout():
            print(f"{Fore.RED}Failed to Connect to Discord API")
            input("Press any key to restart..")
            main()

if __name__ == "__main__":
    os.system('clear')
    main()