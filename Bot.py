import discord
from discord.ext import commands
import praw
from webserver import keep_alive
import os
import random
import time

client = commands.Bot(command_prefix='u.')
game = discord.Game(name='u.help')
botid = 577140178791956500

@client.event
async def on_ready():
    print('ready')
    await client.change_presence(status =discord.Status.online, activity =  game)


reddite = praw.Reddit(client_id="client_id_here",
                      client_secret="SECRET ID HERE",
                      user_agent='somerandomthinggoeshere',
                      username='idk type yo username')


@client.event
async def on_guild_join(ctx):
    print(f'joined {ctx.guild.name}')
    embed = discord.Embed(description='Yo! names tortoise , thanks for adding me here .. use `t.` before a command',
                          color=0x3498db)


@client.event
async def on_guild_join(ctx):
    print(f'joined {ctx.guild.name}')
    embed = discord.Embed(description='Yo! names usagi , thanks for adding me here .. use `usagi.` before a command',
                          color=0x3498db)


@client.event
async def on_message(message):
    server = client.get_guild(id=581084433646616576)
    channel = client.get_channel(id =690919915464425492 )
    if message.guild == None:
        msg = discord.Embed(description=message.content,color=0x3498d)
        msg.set_author(name = message.author.display_name,icon_url=message.author.avatar_url)
        await channel.send(embed=msg)
    
    await client.process_commands(message)


@client.event
async def on_member_join(member: discord.Member):
    if member.guild.id == 577192344529404154:
      pass
    else:
        await member.guild.system_channel.send('Welcome to ' + member.guild.name +  + member.mention)


class admins(commands.Cog):
    """You will require admin permissions to use these commands """

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """kick a member , You will require the permissions to use this command"""
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} kicked {reason}')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Bans a member , You will require the permissions to use this command"""

        await member.ban(reason=reason)
        await ctx.say(f'{member.mention} +  banned {reason}')

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, role_: discord.Role, member: discord.Member):
        # adds a role to a member

        if member is None:
            await ctx.send('mention the member')
        else:
            await member.add_roles(role_)
            await ctx.send(f'{member.mention} is now a {role_.name}')

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        """clears messages, you will require the Manage messages permission to use this command"""

        if amount == None:
            await ctx.send('Please specify the number of messages you want to clear ... example ```t.clear 6```')
        else:
            await ctx.channel.purge(limit=amount+1)
            await ctx.send('**MESSAGES CLEARED** ' + ctx.message.author.mention)
            time.sleep(1)
            await ctx.channel.purge(limit=1)


class fun(commands.Cog):
   
    @commands.command()
    async def slap(self, ctx, *, member: discord.Member):
        """Slaps a member"""

        if member is None:
            await client.say('mention who you want to slap you fool' + ctx.message.author.mention)
        else:
            if member.id == ctx.message.author.id:
                await ctx.send(ctx.message.author.mention + " slapped him/her self LOL")
            elif member.id == 247292930346319872:
                embed = discord.Embed(
                    description=ctx.message.author.mention + "Nah you can't slap my dad!.....wait I will kick him in the balls for you ;-)")
                embed.set_image(url="https://media.giphy.com/media/3o7TKwVQMoQh2At9qU/giphy.gif")
                await ctx.send(embed=embed)

      
      

            else:
                embed = discord.Embed(
                    description=member.mention + " got slapped in the face by: " + ctx.message.author.mention + "!")
                embed.set_image(
                    url="https://66.media.tumblr.com/05212c10d8ccfc5ab190926912431344/tumblr_mt7zwazvyi1rqfhi2o1_400.gif")
                await ctx.send(embed=embed)

    @commands.command()
    async def shoot(self, ctx, *, member: discord.Member):
        """Shoots a member"""

        if member.id == 247292930346319872:
            embed = discord.Embed(description=ctx.message.author.mention + "Anyday!")
            embed.set_image(url="https://media.giphy.com/media/oQfhD732U71YI/giphy.gif")
            await ctx.send(embed=embed)

        elif ctx.message.author.id == 247292930346319872 and member.id == 247292930346319872:

            embed = discord.Embed(description=ctx.message.author.mention + ' DAD! DONT SHOOT YOURSELF')
            embed.set_image(url="https://media.giphy.com/media/f2fVSJWddYb6g/giphy.gif")
            await ctx.send(embed=embed)


        else:

            embed = discord.Embed(
                description=member.mention + ' shot by ' + ctx.message.author.mention + ' :gun: :boom: ')
            embed.set_image(url='https://i.gifer.com/XdhK.gif')
            await ctx.send(embed=embed)


class other(commands.Cog):

    @commands.command()
    async def say(self, ctx, arg):
        """Says something"""
        await ctx.channel.purge(limit = 1)

        await ctx.send(arg)

    @commands.command()
    async def members(self, ctx):
        """returns the number of members in a server"""
        await ctx.send(f'```{ctx.guild.member_count}```')

    @commands.command()
    async def status(self, ctx, *, member: discord.Member):

        """Returns the status of a member"""


        roles_ = ""

        def rolls(rolelist):
            stuff = ""
            for i in rolelist:
                stuff += i.mention
            return stuff

        def activ(member):

            if member.activity == None:
                return None

            elif member.activity.type  != discord.ActivityType.custom:
                text = f"{member.activity.type.name} {member.activity.name}"
                return text
            else:
                return member.activity.name
            
            

        def stat(member):
            if member.status == discord.Status.dnd:
                return "DND 🔴"

            elif  member.status == discord.Status.online:
                return "ONLINE 🟢 "

            elif member.status == discord.Status.idle:
                return "IDLE 🌙 "

            elif member.status == discord.Status.offline:
                return "OFFLINE 💀 "

        async def custom_status(desc):
            if member.is_on_mobile() and member.status != discord.Status.offline:
                embed = discord.Embed(title=member.display_name,
                                      description=desc, color=member.top_role.color)
                embed.add_field(name='**DEVICE **', value='Phone: :iphone:  ')
                embed.add_field(name="|", value="_ _ ")
                # embed.set_author(member.display_name)
                embed.add_field(name='**STATUS**', value=stat(member=member))
                embed.add_field(name="**JOINED SERVER AT**", value=member.joined_at)
                embed.add_field(name="|", value="_ _ ")
                embed.add_field(name="**ROLES**", value=rolls(member.roles))
                embed.add_field(name="**ACTIVITY**", value=activ(member=member))

                embed.set_thumbnail(url=member.avatar_url)

                await ctx.send(embed=embed)

            elif member.status != discord.Status.offline:
                # await ctx.send(f"```{member} is {member.status}```")
                embed = discord.Embed(title=member.display_name,
                                      description=desc, color=member.top_role.color)
                embed.add_field(name='**DEVICE **', value='PC:  :desktop:  ')
                embed.add_field(name="|", value="_ _  ")
                embed.add_field(name='**STATUS**', value=stat(member=member))
                embed.add_field(name="**JOINED SERVER AT**", value=member.joined_at)
                embed.add_field(name="|", value="_ _ ")
                embed.add_field(name="**ROLES**", value=rolls(member.roles))
                embed.add_field(name="**ACTIVITY**", value=activ(member=member))
                embed.set_thumbnail(url=member.avatar_url)

                # embed.set_author(name=member.display_name,url=member.avatar_url)

                # embed.set_author(member.display_name)
                await ctx.send(embed=embed)

            elif member.status == discord.Status.offline:
                embed = discord.Embed(title=member.display_name,
                                      description=desc, color=member.top_role.color)
                embed.add_field(name='Device', value=':no_entry:  ')
                embed.add_field(name="|", value="_ _ ")
                embed.add_field(name='**STATUS**', value=stat(member=member))
                embed.add_field(name="**JOINED SERVER AT**", value=member.joined_at)
                embed.add_field(name="|", value="_ _ ")
                embed.add_field(name="**ROLES**", value=rolls(member.roles))
                embed.add_field(name="**ACTIVITY**", value=activ(member=member))
                embed.set_thumbnail(url=member.avatar_url)

                await ctx.send(embed=embed)

        if member.id == 577140178791956500:
            await custom_status(desc="bunny waifu")

        elif member.id == 268015754862002176:  
            await custom_status(desc="Filthy phone using infidel")

        elif member.id == 247292930346319872:  
            await custom_status(desc=" Usagis father ")

        elif member.id == 392686296860065792:  
            await custom_status(desc="Jayalitha dead sad song")

        elif member.id == 373089985403813888:
            await custom_status(desc="Puga the cupman")

        elif member.id == 266865822817845249:  
            await custom_status(desc=" captain of the sex industry")

        elif member.id == 303049066525491201:
           await custom_status(desc="karen please come back i miss the kids")
            



        elif member.is_on_mobile() and member.status != discord.Status.offline:
            embed = discord.Embed(title=member.display_name, color=member.top_role.color)
            embed.add_field(name='**DEVICE **', value='Phone: :iphone:  ')
            embed.add_field(name="|", value="_ _ ")
            # embed.set_author(member.display_name)
            embed.add_field(name='**STATUS**', value=stat(member=member))
            embed.add_field(name="**JOINED SERVER AT**", value=member.joined_at)
            embed.set_thumbnail(url=member.avatar_url)
            embed.add_field(name="|", value="_ _ ")
            embed.add_field(name="**ROLES**", value=rolls(member.roles))
            embed.add_field(name="**ACTIVITY**", value=activ(member=member))
            await ctx.send(embed=embed)





        elif member.status != discord.Status.offline:
            # await ctx.send(f"```{member} is {member.status}```")
            embed = discord.Embed(title=member.display_name, color=member.top_role.color)
            embed.add_field(name='**DEVICE **', value='PC:  :desktop:  ')
            embed.add_field(name="|", value="_ _ ")
            embed.add_field(name='**STATUS**', value=stat(member=member))
            embed.add_field(name="**JOINED SERVER AT**", value=member.joined_at)
            embed.add_field(name="|", value="_ _ ")
            embed.add_field(name="**ROLES**", value=rolls(member.roles))
            embed.add_field(name="**ACTIVITY**", value=activ(member=member))
            embed.set_thumbnail(url=member.avatar_url)

            # embed.set_author(name=member.display_name,url=member.avatar_url)

            # embed.set_author(member.display_name)
            await ctx.send(embed=embed)

        elif member.status == discord.Status.offline:
            embed = discord.Embed(title=member.display_name, color=member.top_role.color)
            embed.add_field(name='Device', value=':no_entry:  ')
            embed.add_field(name="|", value="_ _ ")
            embed.add_field(name='**STATUS**', value=stat(member=member))
            embed.add_field(name="**JOINED SERVER AT**", value=member.joined_at)
            embed.add_field(name="|", value="_ _ ")
            embed.add_field(name="**ROLES**", value=rolls(member.roles))
            embed.add_field(name="**ACTIVITY**", value=activ(member=member))
            embed.set_thumbnail(url=member.avatar_url)

            await ctx.send(embed=embed)


    @commands.command()
    async def pfp(self, ctx, *, member: discord.Member):
        """Displays the profile picture of a member"""

        if member.id == botid:
            await ctx.send(f' my avatar {member.avatar_url} ')

        await ctx.send(f'{member.mention} avatar {member.avatar_url} ')

    @commands.command()
    async def dm(self,ctx,msg,member : discord.Member):

      if ctx.author.id == 247292930346319872:
       await member.send(msg)
       await ctx.channel.purge(limit=1)
       await ctx.author.send(f"sent a message to {member.display_name}")

      elif ctx.author.id == 303049066525491201:
        await member.send(msg)
        await ctx.channel.purge(limit=1)
        await ctx.author.send(f"sent a message to {member.display_name}")

      elif ctx.author.id == 392686296860065792:
        await member.send(msg)
        await ctx.channel.purge(limit=1)
        await ctx.author.send(f"sent a message to {member.display_name}")

      elif ctx.author.id == 411563702526017536:
        await member.send(msg)
        await ctx.channel.purge(limit=1)
        await ctx.author.send(f"sent a message to {member.display_name}")
      
      else:
        await ctx.send("no")

    
    @commands.command()
    async def DmMember(self, ctx, msg, id: int):

        if ctx.author.id == 247292930346319872:
            guild = client.get_guild(411564918303752192)
            boi = guild.get_member(id)
            await boi.send(msg)
            await ctx.send("sheriffed him")

        elif ctx.author.id == 392686296860065792:
            guild = client.get_guild(411564918303752192)
            boi = guild.get_member(id)
            await boi.send(msg)
            await ctx.send("sheriffed him")

        elif ctx.author.id == 303049066525491201:
            guild = client.get_guild(411564918303752192)
            boi = guild.get_member(id)
            await boi.send(msg)
            await ctx.send("sheriffed him")

        else:
            await ctx.send("no")
import random


class reddit(commands.Cog):
    @commands.command()
    async def meme(self, ctx):
        """sends you the dankest of the dank memes from reddit"""
        subred = reddite.subreddit('memes')
        neewmeem = subred.hot(limit=100)
        lstmeem = list(neewmeem)
        randsub = random.choice(lstmeem)
        embed = discord.Embed(title=randsub.title,
                              description=f':thumbsup: {randsub.score} \n \n :speech_balloon:{len(randsub.comments)} ',
                              url=randsub.url, colour=0x3498d)
        embed.set_image(url=randsub.url)
        await ctx.send(embed=embed)

    @commands.command()
    async def newpost(self, ctx, subreddit):
        """sends you the fresh posts from a subreddit"""
        subred = reddite.subreddit(f'{subreddit}')
        neewmeem = subred.new(limit=10)
        lstmeem = list(neewmeem)
        randsub = random.choice(lstmeem)
        embed = discord.Embed(title=randsub.title,
                              description=f':thumbsup: {randsub.score} \n \n :speech_balloon: {len(randsub.comments)} ',
                              url=randsub.url, colour=0x3498d)
        embed.set_image(url=randsub.url)
        await ctx.send(embed=embed)

    @commands.command()
    async def hotpost(self, ctx, subreddit):
        """sends you the hottest posts from a subreddit"""
        subred = reddite.subreddit(f'{subreddit}')
        neewmeem = subred.hot(limit=10)
        lstmeem = list(neewmeem)
        randsub = random.choice(lstmeem)
        embed = discord.Embed(title=randsub.title,
                              description=f':thumbsup: {randsub.score} \n \n :speech_balloon: {len(randsub.comments)} ',
                              url=randsub.url,
                              colour=0x3498db)
        embed.set_image(url=randsub.url)
        await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f"```{error}```")

client.add_cog(admins(client))
client.add_cog(fun(client))
client.add_cog(other(client))
client.add_cog(reddit(client))


client.run(TOKEN)
