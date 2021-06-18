import discord
from StuffsWeNeed import defaultstuff
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
      print ('Help module is ready.')

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
      # initial embed
      em = discord.Embed(title = defaultstuff.texts()["helpEmbed1Title"], description = defaultstuff.texts()["helpEmbed1Descr"], color = 0xadcca6)

      em.set_footer(text = "https://tinyurl.com/invitekei ˚⊹", icon_url = "https://media.discordapp.net/attachments/819845888155058207/822567557595791380/Untitled58_20210319212933.png?width=665&height=665")
      em.set_thumbnail(url = "https://media.discordapp.net/attachments/817475729578262538/823605034046193754/image0.png?width=665&height=665")

      await ctx.send(embed = em)

    # MODULES
    @help.command()
    async def admin(self, ctx):
      em = discord.Embed(title = defaultstuff.texts()["helpTitleAdminModule"], description = defaultstuff.texts()["helpTextAdminModule"], color = 0xadcca6)

      await ctx.send(embed = em)
    
    @help.command()
    async def mod(self, ctx):
      em = discord.Embed(title = defaultstuff.texts()["helpTitleModModule"], description = defaultstuff.texts()["helpTextModModule"], color = 0xadcca6)

      await ctx.send(embed = em)

    @help.command()
    async def fun(self, ctx):
      em = discord.Embed(title = defaultstuff.texts()["helpTitleFunModule"], description = defaultstuff.texts()["helpTextFunModule"], color = 0xadcca6)

      await ctx.send(embed = em)

    @help.command()
    async def eco(self, ctx):
      em = discord.Embed(title = defaultstuff.texts()["helpTitleEcoModule"], description = defaultstuff.texts()["helpTextEcoModule"], color = 0xadcca6)

      await ctx.send(embed = em)

    @help.command()
    async def misc(self, ctx):
      em = discord.Embed(title = defaultstuff.texts()["helpTitleMiscModule"], description = defaultstuff.texts()["helpTextMiscModule"], color = 0xadcca6)

      await ctx.send(embed = em)
    
# doki did smort thing ^ oooo very smort indeed
# help commands for single commands

    @help.command()
    async def ping(self, ctx):
        em = discord.Embed(title = "``,ping`", description = "Displays Kaito's current latency.", color = 0xadcca6)
         # no perms needed = no mention in the embed
        em.add_field(name = "Usage", value = "`,ping`")

        await ctx.send(embed = em)

    @help.command()
    async def ban(self, ctx):
      em = discord.Embed(title = "`,ban` / `,b`", description = "Bans a member of the server.", color = 0xadcca6)
      em.add_field(name = "Permissions", value = "BanMembers Permission", inline=False)
      em.add_field(name = "Usage", value = "`,ban <user> {reason}`")

      await ctx.send(embed = em)

    @help.command()
    async def unban(self, ctx):
      em = discord.Embed(title = "`,unban` / `,ub`", description = "Unbans a member of the server.", color = 0xadcca6)
      em.add_field(name = "Permissions", value = "BanMembers Permission", inline=False)
      em.add_field(name = "Usage", value = "`,unban <user> {reason}`")

      await ctx.send(embed = em)

    @help.command()
    async def avatar(self, ctx):
        em = discord.Embed(title = "`,avatar` / `,av`", description = "Displays your avatar, provide a @Mention to get someone else's avatar.", color = 0xadcca6)
        # no perms needed = no mention in the embed
        em.add_field(name = "Usage", value = "`,avatar` or `,av @user`")

        await ctx.send(embed = em)

    @help.command()
    async def invite(self, ctx):
        em =discord.Embed(title = "`,invite`", description = "Sends Kei's invite link.", color = 0xadcca6)
        # no perms needed = no mention in de embed
        em.add_field(name ="Usage", value = "`,invite`")

        await ctx.send(embed = em)

    @help.command()
    async def kick(self, ctx):
      em = discord.Embed(title = "`,kick` / `,k`", description = "Kicks a member of the server.", color = 0xadcca6)
      em.add_field(name = "Permissions", value = "KickMembers Permission", inline=False)
      em.add_field(name = "Usage", value = "`,kick <user> {reason}`")

      await ctx.send(embed = em)

    @help.command()
    async def hug(self, ctx):
        em = discord.Embed(title = "`,hug`", description = "Sends a cute hug gif. Provide an @ mention to give them a virtual hug.", color = 0xadcca6)
        # no perms needed = no mention in the embed
        em.add_field(name = "Usage", value = "`,hug @user`")

        await ctx.send(embed = em)

    @help.command()
    async def kiss(self, ctx):
        em = discord.Embed(title = "`,kiss`", description = "Sends a cute kiss gif. Provide an @ mention to give them a virtual kiss.", color = 0xadcca6)
        # no perms needed = no mention in the embed
        em.add_field(name = "Usage", value = "`,kiss @user`")

        await ctx.send(embed = em)

    @help.command()
    async def pat(self, ctx):
        em = discord.Embed(title = "`,pat`", description = "Sends a cute pat gif. Provide an @ mention to give them a virtual pat.", color = 0xadcca6)
        # no perms needed = no mention in the embed
        em.add_field(name = "Usage", value = "`,pat @user`")

        await ctx.send(embed = em)

    @help.command()
    async def greetmsg(self, ctx):
        em = discord.Embed(title = "`,greetmsg`", description = "Set your server a greet message. Provide a text to set it as the automated greeting. Set the message in the channel you wish Kei to greet in.", color = 0xadcca6)
        # no perms needed = no mention in the embed
        em.add_field(name = "Usage", value = "`,greetmsg <text>`")

        await ctx.send(embed = em)




# this is the end of the code, type all commands above this
def setup(client):
    client.add_cog(Help(client))
