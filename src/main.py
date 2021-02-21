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
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    validStrs = {"who\'s joe", "whos joe", "who is joe", "whose joe"}
    if message.author == bot.user:
        return
    if(bot.start):
        responses = ["Joe fuck yourself", "Joe mama", "Joe Biden"]
        if any(x in message.content.lower() for x in validStrs):
            await message.reply(responses[randint(0, 2)], mention_author=True)
            print(message.content)
    await bot.process_commands(message)


@bot.command(name="src", brief="Returns source code link", description="Returns a github link to the source code for the bot")
async def src(ctx):
    await ctx.send("https://github.com/PopsicleTreehouse/JoeMamaDiscordBot")

# Make this one method?


@bot.command(name="stop", brief="Stops the bot from running", description="Stops the bot if it is currently running")
@commands.is_owner()
async def stop(ctx, master=""):
    if(bot.start):
        print("stopped")
        bot.start = False
        await ctx.send("Stopped")
    else:
        await ctx.send("Already stopped")


@bot.command(name="start", brief="Starts the bot", description="Starts the bot if it is not currently running")
@commands.is_owner()
async def stop(ctx):
    if(not bot.start):
        print("started")
        bot.start = True
        await ctx.send("Started")
    else:
        await ctx.send("Already started")

load_dotenv()
bot.run(getenv('TOKEN'))
