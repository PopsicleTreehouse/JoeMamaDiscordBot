import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from random import randint

bot = commands.Bot(command_prefix='-joe ')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Using prefix \'-joe\'"))
    print('We have logged in as {0.user}'.format(bot))


@bot.command(name="src", description="Returns source code link", )
async def src(ctx):
    await ctx.send("https://github.com/PopsicleTreehouse/JoeMamaDiscordBot")


@bot.event
async def on_message(message):
    validStrs = {"who\'s joe", "whos joe"}
    if message.author == bot.user:
        return

    if any(x in message.content.lower() for x in validStrs):
        if(randint(0, 1) == 1):
            await message.reply("Joe fuck yourself", mention_author=True)
        else:
            await message.reply("Joe mama", mention_author=True)
        print(message.content)
    await bot.process_commands(message)

load_dotenv()
bot.run(getenv('TOKEN'))
