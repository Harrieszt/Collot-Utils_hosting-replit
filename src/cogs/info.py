#[Info API]
import os
import json
import discord
from discord.ext import commands
from discord.ui import Button, View
from datetime import datetime
from discord.commands import Option, permissions, slash_command

with open('.././data/harry_website.json') as harry_web:
    web = json.load(harry_web)
    h_url = web["web"]

with open('.././data/collot_info.json') as collot_i:
    v = json.load(collot_i)
    version = v["version"]

#cmd var
sv = 'Server'
cobo = 'Collot Bot'
COLLOT_ID = os.environ['COLID']
BINARY = os.environ['BINARY']
CONSTLOG = os.environ['CONSTLOG']

class Help(discord.ui.View):
    def __init__(self, ctx):
        self.ctx = ctx
        super().__init__(timeout=60)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user == self.ctx.author:
            return True
        await interaction.response.send_message("You can't do this", ephemeral=True)
        return False
    
    async def on_timeout(self):
        if self.message:
            emBed = discord.Embed()
            emBed.title="Time out"
            emBed.color=0xa32424
            self.myselect.disabled = True
            await self.message.edit_original_message(view=self)
        
    @discord.ui.select(placeholder="Select a category", row=0, options=[
        discord.SelectOption(label="Information", emoji='ℹ️'),
        discord.SelectOption(label="Utility", emoji='⚛'),
        discord.SelectOption(label="Fun", emoji='🥳'),
        discord.SelectOption(label="Pirategames", emoji='🏴‍☠️')
    ])
    
    async def myselect(self, select: discord.ui.Select, interaction: discord.Interaction):
        if select.values[0] == "Information":
            info_head = '[ ℹ Information]'
            ###[Command]###
            about_ = f'> **`about`** : To get bot infromation\n'
            info_ = f'> **`info`** : To get user information\n'
            whois_ = f'> **`whois`** : To get user information search by using user ID\n'
            serverinfo_ = f'> **`serverinfo`** : To get server information\n'
            help_ = f'> **`help`** : To get help command\n'   
            ###
            info_assem = '{0}{1}{2}{3}{4}'.format(info_, about_, whois_, serverinfo_, help_)

            #[Embed]
            emBed = discord.Embed()
            emBed.title="Collot Utilities - Help"
            emBed.color=0x42f5a7

            #Embed content
            emBed.add_field(name=info_head, value=info_assem, inline=False)
            ###
            #emBed.set_thumbnail(url='https://static.wikia.nocookie.net/beastars-eng/images/b/bc/Collot_%28Anime%29.png/revision/latest/scale-to-width-down/259?cb=20190806180535')
            emBed.set_footer(text='Collot Utilities created by Harry HK', icon_url='https://i.imgur.com/4yrIv05.jpg')
        
            await self.message.edit_original_message(embed=emBed)

        elif select.values[0] == "Utility":
            uti_head = '[ ⚛ Utility]'
            ###[Command]###
            bin_ = f'> **`binary`** : To convert text to binary\n'      
            mor_ = f'> **`morse`** : To convert text to morse code\n'      
            ran_ = f'> **`random`** : To random number by give min and max number\n'       
            ###
            uti_assem = '{0}{1}{2}'.format(bin_, mor_, ran_)

            #[Embed]
            emBed = discord.Embed()
            emBed.title="Collot Utilities - Help"
            emBed.color=0x00fffb

            #Embed content
            emBed.add_field(name=uti_head, value=uti_assem, inline=False) 
            ###
            #emBed.set_thumbnail(url='https://static.wikia.nocookie.net/beastars-eng/images/b/bc/Collot_%28Anime%29.png/revision/latest/scale-to-width-down/259?cb=20190806180535')
            emBed.set_footer(text='Collot Utilities created by Harry HK', icon_url='https://i.imgur.com/4yrIv05.jpg')

            await self.message.edit_original_message(embed=emBed)
        
        elif select.values[0] == "Pirategames":
            pirate_head = '[ 🏴‍☠️ Pirate of Discord]'
            ###[Command]###
            bal_ = f'> **`balance`** : To check your balance\n'                   
            mer_ = f'> **`merchant`** : To buy voyage\n'                   
            voy_ = f'> **`voyage`** : To start voyage\n'                                 
            ###
            pirate_assem = '{0}{1}{2}'.format(bal_,mer_,voy_)

            #[Embed]
            emBed = discord.Embed()
            emBed.title="Collot Utilities - Help"
            emBed.color=0x5f57ff

            #Embed content
            emBed.add_field(name=pirate_head, value=pirate_assem, inline=False) 
            ###
            #emBed.set_thumbnail(url='https://static.wikia.nocookie.net/beastars-eng/images/b/bc/Collot_%28Anime%29.png/revision/latest/scale-to-width-down/259?cb=20190806180535')
            emBed.set_footer(text='Collot Utilities created by Harry HK', icon_url='https://i.imgur.com/4yrIv05.jpg')

            await self.message.edit_original_message(embed=emBed)
        
        elif select.values[0] == "Fun":
            fun_head = '[ 🥳 Fun]'
            ###[Command]###
            wan_ = f'> **`wanted`** : To send wanted poster with profile mentioned on it\n'         
            rip_ = f'> **`rip`** : To send RIP poster with profile mentioned on it\n'         
            bir_ = f'> **`bird`** : To random send bird picture\n'         
            cat_ = f'> **`cat`** : To random send cat picture\n'         
            dog_ = f'> **`dog`** : To random send dog picture\n'         
            ###
            fun_assem = '{0}{1}{2}{3}{4}'.format(wan_, rip_, bir_, cat_, dog_)

            #[Embed]
            emBed = discord.Embed()
            emBed.title="Collot Utilities - Help"
            emBed.color=0xffd500

            #Embed content
            emBed.add_field(name=fun_head, value=fun_assem, inline=False) 
            ###
            #emBed.set_thumbnail(url='https://static.wikia.nocookie.net/beastars-eng/images/b/bc/Collot_%28Anime%29.png/revision/latest/scale-to-width-down/259?cb=20190806180535')
            emBed.set_footer(text='Collot Utilities created by Harry HK', icon_url='https://i.imgur.com/4yrIv05.jpg')

            await self.message.edit_original_message(embed=emBed)

class infoAPI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('[{0}][{1}][cogs/info] Loaded : {2}'.format(sv, datetime.now(), self.__class__.__name__))
        print('[{0}][{1}][cogs/info/{2}] Command loaded : about'.format(sv, datetime.now(), self.__class__.__name__))
        print('[{0}][{1}][cogs/info/{2}] Command loaded : info'.format(sv, datetime.now(), self.__class__.__name__))
        print('[{0}][{1}][cogs/info/{2}] Command loaded : whois'.format(sv, datetime.now(), self.__class__.__name__))
        print('[{0}][{1}][cogs/info/{2}] Command loaded : serverinfo'.format(sv, datetime.now(), self.__class__.__name__))
        print('[{0}][{1}][cogs/info/{2}] Command loaded : help'.format(sv, datetime.now(), self.__class__.__name__))

        constlog = self.bot.get_channel(CONSTLOG)
        await constlog.send('[{0}][{1}][cogs/info] Loaded : {2}'.format(sv, datetime.now(), self.__class__.__name__))
        await constlog.send('[{0}][{1}][cogs/info/{2}] Command loaded : about'.format(sv, datetime.now(), self.__class__.__name__))
        await constlog.send('[{0}][{1}][cogs/info/{2}] Command loaded : info'.format(sv, datetime.now(), self.__class__.__name__))
        await constlog.send('[{0}][{1}][cogs/info/{2}] Command loaded : whois'.format(sv, datetime.now(), self.__class__.__name__))
        await constlog.send('[{0}][{1}][cogs/info/{2}] Command loaded : serverinfo'.format(sv, datetime.now(), self.__class__.__name__))
        await constlog.send('[{0}][{1}][cogs/info/{2}] Command loaded : help'.format(sv, datetime.now(), self.__class__.__name__))
    
    @slash_command(guild_ids=[BINARY], description="I'll show you how I come")
    async def about(self, ctx):       
        #int
        bot = ctx.bot 
        id = '513382486269624332'

        #fetch name
        collot = await bot.fetch_user(id)

        #embed
        emBed = discord.Embed()
        emBed.title = "Collot Utilities - Information"
        emBed.description = "This bot make for ultimate utilities"
        emBed.color = 0xa33243
        
        #embed content
        emBed.set_author(name="{0}  :  Harry HK".format(collot), icon_url="https://i.imgur.com/pDNLLcl.jpg")
        emBed.add_field(name="This is Harry's website", value=f"{h_url}", inline=False)
        emBed.set_thumbnail(url='https://static.wikia.nocookie.net/beastars-eng/images/b/bc/Collot_%28Anime%29.png/revision/latest/scale-to-width-down/259?cb=20190806180535')
        emBed.set_footer(text=f"Collot Utilities version : {version}", icon_url='https://i.imgur.com/4yrIv05.jpg')        
        
        #source link button
        button = Button(label="Bot invite link", url="https://discord.com/api/oauth2/authorize?client_id=965527760946733067&permissions=8&scope=bot%20applications.commands")
        #view
        view = View()
        view.add_item(button)

        #send embed
        await ctx.respond(embed=emBed, view=view)
        
        #cmd
        print('[{0}][{1}][{2}] query "about" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

        constlog = self.bot.get_channel(CONSTLOG)
        await constlog.send('[{0}][{1}][{2}] query "about" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))
    
    @slash_command(guild_ids=[BINARY], description="Show member profile that you mention")
    async def info(self, ctx, member : discord.Member=None):
        if not member:
            member = ctx.author

        #profile information
        name = f"> {str(member)}" #Name
        nick = f"> {str(member.display_name)}" #Nickname
        Id = f"> {str(member.id)}" #User ID
        created_at = member.created_at.strftime("> %A, %B %d, %Y\n> %H : %M : %S") #Created date and time
        joined_at = member.joined_at.strftime("> %A, %B %d, %Y\n> %H : %M : %S") #Joined date and time 

        #embed
        emBed = discord.Embed()
        emBed.title = "Information"
        emBed.add_field(name="NAME" , value=name, inline=False)
        emBed.add_field(name="NICK NAME" , value=nick, inline=False)
        emBed.add_field(name="USER ID" , value=Id, inline=False)
        emBed.add_field(name="CREATED" , value=created_at, inline=False)
        emBed.add_field(name="JOINED" , value=joined_at, inline=False)

        emBed.set_image(url=member.avatar)
        emBed.set_author(name=str(member) , icon_url=member.avatar)

        emBed.color = member.color

        #send embed
        await ctx.respond(embed=emBed)
        
        #cmd
        print('[{0}][{1}][{2}] query "info" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

        constlog = self.bot.get_channel(CONSTLOG)
        await constlog.send('[{0}][{1}][{2}] query "info" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

    @slash_command(guild_ids=[BINARY], description="Show user profile search by user ID")
    async def whois(self, ctx, user_id : Option(str, "Input user ID")):
        try :
            bot = ctx.bot
            user = await bot.fetch_user(user_id)
            
            #profile information
            name = f"> {str(user)}" #name
            nick = f"> {str(user.display_name)}" #nickname
            Id = f"> {str(user.id)}" #user ID
            created_at = user.created_at.strftime("> %A, %B %d, %Y\n> %H : %M : %S") #Created date and time

            #embed
            emBed = discord.Embed()
            emBed.title = "Information"
            emBed.add_field(name="NAME" , value=name, inline=False)
            emBed.add_field(name="NICK NAME" , value=nick, inline=False)
            emBed.add_field(name="USER ID" , value=Id, inline=False)
            emBed.add_field(name="CREATED" , value=created_at, inline=False)

            emBed.set_image(url=user.avatar)
            emBed.set_author(name=str(user) , icon_url=user.avatar)

            emBed.color = user.color

            #send embed
            await ctx.respond(embed=emBed)

        except :
            await ctx.respond("User not found please try again")
        #cmd
        print('[{0}][{1}][{2}] query "whois" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

        constlog = self.bot.get_channel(CONSTLOG)
        await constlog.send('[{0}][{1}][{2}] query "whois" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

    @slash_command(guild_ids=[BINARY], description="Show user profile search by user ID")
    async def serverinfo(self, ctx):

        #Server information
        sv_name = ctx.guild.name #Server name
        sv_id = str(ctx.guild_id) #Server ID
        sv_roles = str(len(ctx.guild.roles)) #Count Server Roles
        sv_verify = str(ctx.guild.verification_level) # Server verification level

        sv_total = ctx.guild.member_count #Count all member
        sv_member = len([member for member in ctx.guild.members if not member.bot]) #Count only Human
        sv_bots = len([Member for Member in ctx.guild.members if Member.bot]) #Count only bot
        sv_bot_list = [bot.mention for bot in ctx.guild.members if bot.bot] #Show and Mention All bot

        sv_channels = len(ctx.guild.channels) #Count all channels 
        sv_text_channels = len(ctx.guild.text_channels) #Count only text channel
        sv_voice_channels = len(ctx.guild.voice_channels) #Count only voice channel

        sv_boosts = ctx.guild.premium_subscription_count #Count boosts

        #Embed
        emBed = discord.Embed(color = ctx.author.color)
        emBed.add_field(name="Server Name", value=f"> {sv_name}", inline=True)
        emBed.add_field(name="Verification Level", value=f"> {sv_verify}", inline=True)
        emBed.add_field(name="Boosts", value=f"> {sv_boosts}", inline=True)
        emBed.add_field(name="Members", value="> Total : {0}\n> Members : {1}\n> Bots : {2}".format(sv_total, sv_member, sv_bots), inline=False)
        emBed.add_field(name="Channels", value="> Channels : {0}\n> Text Channels : {1}\n> Voice Channels : {2}".format(sv_channels, sv_text_channels, sv_voice_channels), inline=False)
        emBed.add_field(name="Number of Roles", value=f"> {sv_roles}", inline=False)
        emBed.add_field(name="Bots", value=", ".join(sv_bot_list), inline=False)

        emBed.set_thumbnail(url=ctx.guild.icon)
        emBed.set_footer(icon_url=ctx.guild.icon, text=f"Server ID : {sv_id}")

        #send embed
        await ctx.respond(embed=emBed)
        #cmd
        print('[{0}][{1}][{2}] query "serverinfo" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

        constlog = self.bot.get_channel(CONSTLOG)
        await constlog.send('[{0}][{1}][{2}] query "serverinfo" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

    @slash_command(guild_ids=[BINARY], description="I'm here to help you")
    async def help(self, ctx):
        
        basic_head = '[ Category ]'
        ###[Category]###
        info_ = f'• ℹ Information'
        uti_ = f'• ⚛ Utility'
        fun_ = f'• 🥳 Fun'
        gam_ = f'• 🏴‍☠️ Pirate games'
        ###
        basic_assem = '{0}\n{1}\n{2}\n{3}'.format(info_, uti_, fun_, gam_)

        #[Embed]
        emBed = discord.Embed()
        emBed.title="Collot's Utilities - Help"
        emBed.description="All available bot commands"
        emBed.color=0x42f5a7

        #Embed content
        emBed.add_field(name=basic_head, value=basic_assem, inline=False)
        ###
        #emBed.set_thumbnail(url='https://static.wikia.nocookie.net/beastars-eng/images/b/bc/Collot_%28Anime%29.png/revision/latest/scale-to-width-down/259?cb=20190806180535')
        emBed.set_footer(text='Collot assistant created by Harry HK', icon_url='https://i.imgur.com/4yrIv05.jpg')
        
        #respond
        view = Help(ctx)
        view.message = await ctx.respond(embed=emBed, view=view)
        
        #cmd
        print('[{0}][{1}][{2}] query "help" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

        constlog = self.bot.get_channel(CONSTLOG)
        await constlog.send(print('[{0}][{1}][{2}] query "help" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel)))

def setup(bot):
    bot.add_cog(infoAPI(bot))