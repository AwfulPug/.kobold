import requests
from requests.auth import HTTPDigestAuth
import json
from discord.ext import commands as kobold

class Spells:
    def __init__(self,kobold):
        self.kobold = kobold

def setup(kobold):
    kobold.add_cog(Spells(kobold))