import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from random import randint

bot = commands.Bot(command_prefix='&')


@bot.event
async def on_ready():
    bot.start = True
    await bot.change_presence(activity=discord.Game(name="Type &help for help | Prefix \'&\'"))


@bot.event
async def on_message(message):
    validStrs = {"who\'s joe", "whos joe", "who is joe", "whose joe"}
    if message.author == bot.user:
        return
    if (bot.start):
        responses = ["Joe fuck yourself", "Joe mama", "Joe Biden"]
        if any(x in message.content.lower() for x in validStrs):
            await message.reply(responses[randint(0, 2)], mention_author=True)
    await bot.process_commands(message)


@bot.command(name="src", brief="Returns source code link", description="Returns a github link to the source code for the bot")
async def src(ctx):
    await ctx.send("https://github.com/PopsicleTreehouse/JoeMamaDiscordBot")


# Make this one method?

@bot.command(name="cstate", brief="Starts or stops the bot")
async def cstate(ctx, master=""):
    if(master == "master"):
        exit()
    if(bot.start):
        bot.start = False
        await ctx.send("Stopped")
    else:
        bot.start = True
        await ctx.send("Started")


load_dotenv()
bot.run(getenv('TOKEN'))
