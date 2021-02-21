import discord
from dotenv import load_dotenv
from os import getenv
from random import randint

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
        if(randint(0, 1) == 1):
            await message.reply("Joe fuck yourself", mention_author=True)
        else:
            await message.reply("Joe mama", mention_author=True)
        print(content)

load_dotenv()
client.run(getenv('TOKEN'))
