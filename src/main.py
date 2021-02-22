import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from random import randint

bot = commands.Bot(command_prefix='&')


@bot.event
async def on_ready():
    bot.disabledServers = []
    bot.start = True
    await bot.change_presence(activity=discord.Game(name="&help"))


@bot.event
async def on_message(message):
    validStrs = {"who\'s joe", "whos joe", "who is joe", "whose joe"}
    if (message.author == bot.user):
        return
    if (not(message.guild.id in bot.disabledServers)):
        print(str(message.guild.id) + " is not disabled")
        responses = ["Joe fuck yourself", "Joe mama", "Joe Biden"]
        if any(x in message.content.lower() for x in validStrs):
            await message.reply(responses[randint(0, 2)], mention_author=True)
    else:
        print(str(message.guild.id) + " is disabled")
    await bot.process_commands(message)


@bot.command(name="src", brief="Returns source code link", description="Returns a github link to the source code for the bot")
async def src(ctx):
    await ctx.send("https://github.com/PopsicleTreehouse/JoeMamaDiscordBot")


# Make this one method?

@bot.command(name="cstate", brief="Starts or stops the bot")
async def cstate(ctx):
    if (ctx.guild.id in bot.disabledServers):
        bot.disabledServers.remove(ctx.guild.id)
        await ctx.send("Started")
    else:
        bot.disabledServers.append(ctx.guild.id)
        await ctx.send("Stopped")


load_dotenv()
bot.run(getenv('TOKEN'))
