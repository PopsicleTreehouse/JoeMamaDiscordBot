# @TODO: Make database of responses and disabled servers

import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from random import randint

bot = commands.Bot(command_prefix='&')
bot.responses = {}
bot.disabledServers = []


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="&help"))


@bot.event
async def on_message(message):
    validStrs = {"who\'s joe", "whos joe", "who is joe", "whose joe"}
    if (message.author == bot.user):
        return
    if(not message.guild.id in bot.responses):
        bot.responses[message.guild.id] = [
            "Joe fuck yourself", "Joe mama", "Joe Biden"]
    if (not(message.guild.id in bot.disabledServers)):
        if any(x in message.content.lower() for x in validStrs):
            print(str(message.guild.id) + " is not disabled")
            await message.reply(bot.responses[message.guild.id][randint(0, 2)], mention_author=True)
    else:
        print(str(message.guild.id) + " is disabled")
    await bot.process_commands(message)


@bot.command(name="src", brief="Returns source code link", description="Returns a github link to the source code for the bot")
async def src(ctx):
    await ctx.send("https://github.com/PopsicleTreehouse/JoeMamaDiscordBot")


@bot.command(name="cstate", brief="Starts or stops the bot")
@commands.has_permissions(administrator=True)
async def cstate(ctx):
    if (ctx.guild.id in bot.disabledServers):
        bot.disabledServers.remove(ctx.guild.id)
        await ctx.send("Started")
    else:
        bot.disabledServers.append(ctx.guild.id)
        await ctx.send("Stopped")


@bot.command(name="add", brief="Adds response")
@commands.has_permissions(administrator=True)
async def add(ctx, arg):
    if(arg is None):
        ctx.send("Enter a valid response")
    else:
        bot.responses[ctx.guild.id].append(arg)
        await ctx.send(f"`\'{arg}\' added to responses`")


@bot.command(name="delete", brief="Deletes response")
@commands.has_permissions(administrator=True)
async def delete(ctx, arg):
    if(arg is None):
        ctx.send("Enter a valid response")
    else:
        bot.responses[ctx.guild.id].remove(arg)
        await ctx.send(f"`\'{arg}\' removed from responses`")


@bot.command(name="ls", brief="Lists responses")
async def ls(ctx):
    await ctx.send(str(bot.responses[ctx.guild.id]).strip('[]'))

load_dotenv()
bot.run(getenv('TOKEN'))
