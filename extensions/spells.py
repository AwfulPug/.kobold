import requests
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
        if not jdata["results"]:
            await self.kobold.say("Spell Not Found")
        else:
            results = jdata["results"][0]
            url = results["url"]

            jdata = requests.get(url).json()
            embed = discord.Embed(colour=discord.Color.blue())
            embed.title = jdata["name"]
            embed.description = jdata["desc"][0]
            embed.add_field(name="Higher Levels",value=jdata["higher_level"][0])
            embed.add_field(name="Range",value=jdata["range"])
            embed.add_field(name="Components",value=jdata["components"])
            embed.add_field(name="Cast Time",value=jdata["casting_time"])
            embed.add_field(name="Ritual",value=jdata["ritual"])
            embed.add_field(name="Duration",value=jdata["duration"])
            embed.add_field(name="Concentration",value=jdata["concentration"])
            await self.kobold.say(embed=embed)

def setup(kobold):
    kobold.add_cog(Spells(kobold))