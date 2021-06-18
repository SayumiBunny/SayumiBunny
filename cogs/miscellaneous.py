import discord
import time, datetime
from discord.ext import commands
from pymongo import MongoClient
import os
from dotenv import load_dotenv

start_time=time.time()

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

load_dotenv('.env')
dbclient = MongoClient(os.getenv('DBSTRING1'))
db = dbclient[os.getenv('DBSTRING2')]

class Miscellaneous(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
      print ('Miscellaneous module is ready.')

    # ping
    @commands.command()
    async def ping(self, ctx):
      await ctx.send(f"pong~! <a:bun:816363543174840320>・`{round(self.client.latency * 1000)}ms`")

    # invite
    @commands.command(aliases=['inv'])
    async def invite(self, ctx):
      em = discord.Embed(description = "₊˚✦`🌿`⊹﹕[invite me to your server](https://tinyurl.com/invitekei) <a:KB_bunWhack:816632384342196254>", color = 0xadcca6)

      await ctx.send(embed = em)

    # rando command idfk
    @commands.command(aliases=['docs'])
    async def readme(self, ctx):
        em = discord.Embed(title = "Documentation", description = "GitHub Repository: https://github.com/Dok4440/KaitoBot\nCommands list: https://github.com/Dok4440/KaitoBot/wiki/Command-List", color = 0xadcca6)

        await ctx.send(embed = em)

     # open source
    @commands.command(aliases=['code', 'source'])
    async def opensource(self, ctx):
      await ctx.send("₊˚✦`🌿`⊹﹕access my open-source code on Flo's repl.it profile!: https://repl.it/@flo0003")
    
    # avatar
    @commands.command(aliases=['av', 'pfp', 'profilepic', 'profilepicture'])
    @commands.guild_only() # only able to do this command in a server (not in DM)
    async def avatar(self, ctx, *, user: discord.Member = None):
        user = user or ctx.author
        # size = size or 1024 # gotta figure this out later
        size = 1024
        await ctx.send(f"₊˚✦`🌿`⊹﹕{user.name}'s avatar・꒷꒦\n{user.avatar_url_as(size=size)}")
		
    # say
    @commands.command(aliases=['repeat', 'speak'])
    async def say(self, ctx, *, msg="₊˚✦`🌿`⊹﹕please provide text for me to say!・꒷꒦"):
        await ctx.send(msg)
        await ctx.message.delete()
		
    # bot stats
    @commands.command()
    async def stats(self, ctx):
        em = discord.Embed(color = 0xadcca6)
        
        v=str(os.getenv('VERSION'))
        
        em.set_author(name=f"﹕🌿・KeiBot {v}・✦", icon_url = "https://media.discordapp.net/attachments/819845888155058207/822567557595791380/Untitled58_20210319212933.png?width=665&height=665")
        em.add_field(name="୨୧・authors", value="✦ー`Dok4440`\n✦ー`Flo0003`")
        
        uptime=str(datetime.timedelta(seconds=int(round(time.time() - start_time))))
        em.add_field(name="୨୧・uptime", value=f"✦ー`{uptime}`", inline=False)
        
        em.add_field(name="୨୧・server count", value = f"✦ー`{str(len(self.client.guilds))}`")

        await ctx.send(embed = em)

    # greet msg
    @commands.Cog.listener()
    async def on_member_join(self, member):
      collection = db["Greetings"]
      results = collection.find({"server_id": member.guild.id})

      for result in results:
        msg = result["message"]
        guild = result["server_id"]
        ch = result["channel_id"]

      server = self.client.get_guild(guild)
      channel = server.get_channel(ch)
      await channel.send(msg)
        
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def greetmsg(self, ctx, *, message):
      collection = db["Greetings"]

      post = {"server_id": ctx.message.guild.id, "message": message, "channel_id": ctx.message.channel.id}

      collection.delete_many({"server_id": ctx.message.guild.id})
      collection.insert_one(post) #magic 

      await ctx.send("✦ーWelcome message has been set in this channel! <a:bun:816363543174840320>")

    

# this is the end of the code, type all mod commands above this
def setup(client):
    client.add_cog(Miscellaneous(client))
