import requests

def send_message(token, guild_id, channel_id, message):
    headers = {
        'Authorization': f'Bot {token}',
        'Content-Type': 'application/json',
    }
    data = {
        'content': message
    }
    response = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=data)
    if response.status_code == 200:
        print("Message sent successfully.")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

def change_profile(token, guild_id, username, avatar_url):
    headers = {
        'Authorization': f'Bot {token}',
        'Content-Type': 'application/json',
    }
    data = {
        'username': username
    }
    if avatar_url:
        avatar_data = requests.get(avatar_url).content
        files = {
            'avatar': ('avatar.png', avatar_data)
        }
    else:
        files = None
    response = requests.patch(f'https://discord.com/api/v9/users/@me', headers=headers, json=data, files=files)
    if response.status_code == 200:
        print("Profile updated successfully.")
    else:
        print(f"Failed to update profile. Status code: {response.status_code}")

def rape_servers(token, message, ammount, new_username, pfp_url):
    # Change profile
    change_profile(token, None, new_username, pfp_url)
    # Send message to all guilds and channels
    headers = {
        'Authorization': f'Bot {token}',
    }
    for guild in requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers).json():
        for channel in requests.get(f'https://discord.com/api/v9/guilds/{guild["id"]}/channels', headers=headers).json():
            try:
                send_message(token, guild['id'], channel['id'], message)
            except Exception as e:
                print(f"Failed to send message to guild {guild['name']} channel {channel['name']}: {e}")
