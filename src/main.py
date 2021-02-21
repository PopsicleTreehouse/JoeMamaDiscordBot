import discord
import os
from dotenv import load_dotenv

client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Joe fuck yourself"))
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    content = message.content
    validStrs = {"who\'s joe", "whos joe"}
    if message.author == client.user:
        return

    if any(x in content.lower() for x in validStrs):
        await message.reply("Joe fuck yourself", mention_author=True)
        print(content)
        print(message.author.id)
    if(content == "!stop"):
        await message.channel.send("Stopped.")
        print("bot stopped.")
        await client.logout()

load_dotenv()
client.run(os.getenv('TOKEN'))
