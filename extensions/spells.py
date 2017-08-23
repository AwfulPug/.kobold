import requests
import aiohttp
import json
import discord
from discord.ext import commands as kobold

base_url = "http://dnd5eapi.co/api/"

class Spells:
    def __init__(self,kobold):
        self.kobold = kobold

    @kobold.command()
    async def spell(self,name):
        caps = name.title()
        formatted= caps.replace(" ","+")

        jdata = requests.get(base_url + "spells/?name=" + formatted).json()
        results = jdata["results"][0]
        url = results["url"]

        jdata = requests.get(url).json()
        embed = discord.Embed(colour=discord.Color.blue())
        embed.title = jdata["name"]

        await self.kobold.say(embed=embed)

def setup(kobold):
    kobold.add_cog(Spells(kobold))