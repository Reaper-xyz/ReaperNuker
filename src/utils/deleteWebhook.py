import requests
from utils.common import *

def deleteWebhook(url):
    set_console_title("Reaper V2  | Made by realecstacy. | Delete Webhook")
    requests.delete(url)
    print(f"{Fore.WHITE}[{Fore.LIGHTCYAN_EX}C{Fore.WHITE}] Deleted Webhook")
    sleep(1)
