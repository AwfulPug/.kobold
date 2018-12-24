import asyncio
import discord
from discord.ext import commands

description = "A discord bot to assist with pen and paper roleplaying games."
command_prefix = "."
extensions = {
    "extensions.dice",
    "extensions.spells"
}

# reading the bot key and storing it in variable "key"
token = open("Token.txt", "r")
key = token.readline()
token.close()

kobold = commands.Bot(description=description,command_prefix=command_prefix)

@kobold.event
async def on_ready():
    """ Called when the client is done preparing data recieved from Discord. """
    print(f"App Name: {kobold.user.name}\nBot ID: {kobold.user.id}\nversion {discord.__version__}")

    for extension in extensions:
        try:
            kobold.load_extension(extension)
    # If an exception is thrown, that exception is bound to the variable x.
        except Exception as x:
            exc = "{}:{}".format(type(x).__name__, x)
            print("Unable to load extension {}\n{}".format(extension, exc))

    print("==============\nApplication Online and Running")
kobold.run(key)
