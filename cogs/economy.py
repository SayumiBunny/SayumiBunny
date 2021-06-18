import discord
from discord.ext import commands
from pymongo import MongoClient
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

load_dotenv('.env')
dbclient = MongoClient(os.getenv('DBSTRING1'))
db = dbclient[os.getenv('DBSTRING2')]

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
      print ('Economy module is ready.')

# big wip wip sayu is dying <3

# this is the end of the code, type all mod commands above this
def setup(client):
    client.add_cog(Economy(client))
