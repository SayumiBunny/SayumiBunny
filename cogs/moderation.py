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

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
      print ('Moderation module is ready.')

    # kick command
    @commands.command()
    @commands.has_permissions(kick_members=True) # check if the user has kick perms
    @commands.bot_has_permissions(kick_members=True) # check if the bot has kick perms
    async def kick(self, ctx, user: discord.Member, *, reason=None):
       await ctx.guild.kick(user, reason=reason)
       em = discord.Embed(title = f"✦ ー __**Kick !!**__", description = f"╭ ₊˚`🌿`ฅ︰**{user.name}** was kicked. ꒷꒦\n┊₊˚୨`🌱`ɞ﹒**Reason:** {reason}. ꒷꒦\n╰ฅ`🍃`๑︰**Moderator:** {ctx.author.display_name}. ꒷꒦",  color = 0xadcca6)
       await ctx.send(embed = em)
       await ctx.message.delete()
    # @kick.error()
    # async def kick(self, ctx, user: discord.Member, *, reason=None):
    #   await ctx.send("Insuff perms test")

    #ban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self, ctx, id: int, *, reason=" - "):
         user = await self.client.fetch_user(id)
         actualReason = ctx.author.name + " | " + str(reason)
         await ctx.guild.ban(user, reason=reason)
         em = discord.Embed(title = f"✦ ー __**Ban !!**__", description = f"╭ ₊˚`🌿`ฅ︰**{user.name}** was banned. ꒷꒦\n┊₊˚୨`🌱`ɞ﹒**Reason:** {reason}. ꒷꒦\n╰ฅ`🍃`๑︰**Moderator:** {ctx.author.display_name}. ꒷꒦",  color = 0xadcca6)
         await ctx.send(embed = em)
         await ctx.message.delete()
        
    #ban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self, ctx, id: int, *, reason=" - "):
         user = await self.client.fetch_user(id)
         actualReason = ctx.author.name + " | " + str(reason)
         await ctx.guild.ban(user, reason=reason)
         em = discord.Embed(title = f"✦ ー __**Unban !!**__", description = f"╭ ₊˚`🌿`ฅ︰**{user.name}** was unbanned. ꒷꒦\n┊₊˚୨`🌱`ɞ﹒**Reason:** {reason}. ꒷꒦\n╰ฅ`🍃`๑︰**Moderator:** {ctx.author.display_name}. ꒷꒦",  color = 0xadcca6)
         await ctx.send(embed = em)
         await ctx.message.delete()

    # warn command
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason):

			# check if warned person is yourself
      if member.id == ctx.author.id:
        return await ctx.send("✦ ー you cannot warn yourself.")

      # check if warned person is Kei
      if member.id == self.client.user.id:
        return await ctx.send("✦ ー you cannot warn Kei.")

      # check if warned person is lower in the role hierarchy
      if member.top_role >= ctx.author.top_role:
        return await ctx.send("✦ ー You can't use this command on users with a role higher or equal to yours in the role hierarchy.")

      embed = discord.Embed(title = "✦ ー __**Warning !!**__", description = f"╭ ₊˚`🌿`ฅ︰**{member.name}**'s warning. ꒷꒦\n┊₊˚୨`🌱`ɞ﹒**Reason:** {reason}. ꒷꒦\n╰ฅ`🍃`๑︰**Moderator:** {ctx.author.display_name}. ꒷꒦", color = 0xadcca6)

      embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
      embed.set_footer(text="✦ ー please follow our rules in the future.")

      # database
      collection = db["Warnings"]
      post = {"server_id": ctx.message.guild.id, "warn_user": member.id, "warn_msg": reason, "warn_mod": ctx.author.id}
      collection.insert_one(post)

      try:
        await member.send(embed=embed)
        await ctx.send("✦ ー user has been warned in DMs!")
      except:
        await ctx.send("✦ ー user has been warned, I couldn't DM them.")


# this is the end of the code, type all mod commands above this
def setup(client):
    client.add_cog(Moderation(client))
