import discord
import os
import logging
from discord.ext import commands
from pymongo import MongoClient
from dotenv import load_dotenv

# python -m pip install dnspython

load_dotenv('.env')
dbclient = MongoClient(os.getenv('DBSTRING1'))
db = dbclient[os.getenv('DBSTRING2')]
  
intents = discord.Intents.default()
intents.members = True
logging.basicConfig(level=logging.INFO)

def get_prefix(bot, message):
  global dbclient
  if not message.guild:
    return commands.when_mentioned_or(",")(bot, message)
  prefix = ","
  collection = db["Prefix"]
  for x in collection.find({"server_id":message.guild.id}):
    prefix=x["prefix"]
  return commands.when_mentioned_or(prefix)(bot, message)

client = commands.Bot(command_prefix=get_prefix, intents=intents)

client.remove_command("help")

# event on_ready (bot runs)
@client.event
async def on_ready():
  print('Bot is online.')
  game = discord.Game(",help")
  await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Error;MissingRequiredArgument")
  if isinstance(error, commands.MissingPermissions):
    await ctx.send("Error;MissingPermissions")
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.send("Error;BotMissingPermissions")

# get all files from the "cogs" directory & load them in as commands
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

load_dotenv('.env')
client.run(os.getenv('TOKEN'))
# "if i delete this, the red line goes away" *deletes 2 lines of code* -dok
