import asyncio
import discord
from discord.ext import commands

description = "A discord bot to assist with pen and paper roleplaying games."
command_prefix = "."
kobold = commands.Bot(description=description,command_prefix=command_prefix)

@kobold.event
async def on_ready():
    """ Called when the client is done preparing data recieved from Discord. """
    print("Logged In.")
    print("Name : {}".format(kobold.user.name))
    print("ID : {}".format(kobold.user.id))
    print("Discord Ver : {}".format(discord.__version__))

@kobold.command(pass_context=True)
async def hello(ctx):
        """ Hello : Hello greets the user that calls the command. """
        await kobold.say("Hello " + ctx.message.author.mention + ", how are you today?")

kobold.run('MzQ1NzA5NzQ1MDc4MDA5ODU2.DG_O3w.w8HFMcHSTG0whozlZBqTP8v2xj0')