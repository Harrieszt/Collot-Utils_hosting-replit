import os
import re
import discord
from discord.ext import commands
from discord.ui import Button, View
from discord.commands import Option, slash_command
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont, ImageChops
from io import BytesIO
import json
import random

with open('./data/random_img/bird.json') as bird:
    b_img = json.load(bird)

with open('./data/random_img/cat.json') as cat:
    c_img = json.load(cat)

with open('./data/random_img/dog.json') as dog:
    d_img = json.load(dog)

sv = 'Server'
cobo = 'Collot Bot'
BINARY = os.environ['BINARY']
CONSTLOG = os.environ['CONSTLOG']

def circle(pfp,size = (215,215)):
    
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new('L', bigsize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

class funAPI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('[{0}][{1}][cogs/info] Loaded : {2}'.format(sv, datetime.now(), self.__class__.__name__))
        print('[{0}][{1}][cogs/info/{2}] Command loaded : wanted'.format(sv, datetime.now(), self.__class__.__name__))
        print('[{0}][{1}][cogs/info/{2}] Command loaded : rip'.format(sv, datetime.now(), self.__class__.__name__))
        print('[{0}][{1}][cogs/info/{2}] Command loaded : bird'.format(sv, datetime.now(), self.__class__.__name__))
        print('[{0}][{1}][cogs/info/{2}] Command loaded : cat'.format(sv, datetime.now(), self.__class__.__name__))
        print('[{0}][{1}][cogs/info/{2}] Command loaded : dog'.format(sv, datetime.now(), self.__class__.__name__))

        constlog = self.bot.get_channel(CONSTLOG)
        await constlog.send('[{0}][{1}][cogs/info] Loaded : {2}'.format(sv, datetime.now(), self.__class__.__name__))
        await constlog.send('[{0}][{1}][cogs/info/{2}] Command loaded : wanted'.format(sv, datetime.now(), self.__class__.__name__))
        await constlog.send('[{0}][{1}][cogs/info/{2}] Command loaded : rip'.format(sv, datetime.now(), self.__class__.__name__))
        await constlog.send('[{0}][{1}][cogs/info/{2}] Command loaded : bird'.format(sv, datetime.now(), self.__class__.__name__))
        await constlog.send('[{0}][{1}][cogs/info/{2}] Command loaded : cat'.format(sv, datetime.now(), self.__class__.__name__))
        await constlog.send('[{0}][{1}][cogs/info/{2}] Command loaded : dog'.format(sv, datetime.now(), self.__class__.__name__))
    
    @slash_command(guild_ids=[BINARY], description="This command is in delopment")
    async def wanted(self, ctx, user : discord.Member = None):
        if not user:
            user = ctx.author

        wanted = Image.open('./data/image/wanted.PNG')
        draw = ImageDraw.Draw(wanted)
        
        random_reward = [

                        '1,000,000', '1,500,000', '2,000,000', '2,500,000',
                        '3,000,000', '3,500,000', '4,000,000', '4,500,000',
                        '5,000,000', '5,500,000', '6,000,000', '6,500,000',
                        '7,000,000', '7,500,000', '8,000,000', '8,500,000',
                        '9,000,000', '9,999,999', '1'
                        
                        ]
        random_ = random.choice(random_reward)

        normal_reward = f"${random_}"
        hundred_million = "$100,000,000"

        asset = user.avatar
        data = BytesIO(await asset.read())
        pfp = Image.open(data).convert('RGBA')
        pfp = pfp.resize((330,330))
        rewardfont = ImageFont.truetype("./data/font/western.otf", 100)

        if  random_ == '1' :
            draw.text((50,530), hundred_million, fill = "black", font = rewardfont)
            wanted.paste(pfp, (61,162))
            wanted.save('./data/pfp_cache/wanted_cache.PNG')

        else :
            draw.text((80,530), normal_reward, fill = "black", font = rewardfont)
            wanted.paste(pfp, (61,162))
            wanted.save('./data/pfp_cache/wanted_cache.PNG')

        #respond
        await ctx.respond(file = discord.File('.././data/pfp_cache/wanted_cache.PNG'))
        #cmd
        print('[{0}][{1}][{2}] query "wanted" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

        constlog = self.bot.get_channel(CONSTLOG)
        await constlog.send('[{0}][{1}][{2}] query "wanted" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))
    
    @slash_command(guild_ids=[BINARY], description="This command is in delopment")
    async def rip(self, ctx, user : discord.Member = None):
        if not user:
            user = ctx.author

        rip = Image.open('./data/image/rip.png')
        draw = ImageDraw.Draw(rip)

        asset = user.avatar
        data = BytesIO(await asset.read())
        pfp = Image.open(data).convert('RGBA')
        pfp = pfp.resize((369,355))
        pfp = circle(pfp, (360, 360))
        ripfont = ImageFont.truetype("./data/font/western.otf", 80)

        rip.paste(pfp, (225,407), pfp)
        draw.text((250,755), str(user.display_name), fill = "black", font = ripfont)
        rip.save('./data/pfp_cache/rip_cache.png')

        #respond
        await ctx.respond(file = discord.File('./data/pfp_cache/rip_cache.png'))
        #cmd
        print('[{0}][{1}][{2}] query "rip" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

        constlog = self.bot.get_channel(CONSTLOG)
        await constlog.send('[{0}][{1}][{2}] query "rip" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

    @slash_command(guild_ids=[BINARY], description="Send random bird image")
    async def bird(self, ctx):
        #random num
        random_num = random.randint(1, 100)
        #get image with random
        img = b_img[str(random_num)]

        #embed
        emBed = discord.Embed()
        emBed.title = "Tweet!"
        emBed.color = 0x00fffb
        emBed.set_image(url=img)

        #source link button
        button = Button(label="Source", url=img)
        #view
        view = View()
        view.add_item(button)

        #respond
        await ctx.respond(embed=emBed, view=view)
        #cmd
        print('[{0}][{1}][{2}] query "bird" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

        constlog = self.bot.get_channel(CONSTLOG)
        await constlog.send('[{0}][{1}][{2}] query "bird" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))
    
    @slash_command(guild_ids=[BINARY], description="Send random cat image")
    async def cat(self, ctx):
        #random num
        random_num = random.randint(1, 100)
        #get image with random
        img = c_img[str(random_num)]

        #embed
        emBed = discord.Embed()
        emBed.title = "Meow!"
        emBed.color = 0xff85f9
        emBed.set_image(url=img)

        #source link button
        button = Button(label="Source", url=img)
        #view
        view = View()
        view.add_item(button)

        #respond
        await ctx.respond(embed=emBed, view=view)
        #cmd
        print('[{0}][{1}][{2}] query "cat" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

        constlog = self.bot.get_channel(CONSTLOG)
        await constlog.send('[{0}][{1}][{2}] query "cat" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))
    
    @slash_command(guild_ids=[BINARY], description="Send random dog image")
    async def dog(self, ctx):
        #random num
        random_num = random.randint(1, 100)
        #get image with random
        img = d_img[str(random_num)]

        #embed
        emBed = discord.Embed()
        emBed.title = "Woof!"
        emBed.color = 0xffa44a
        emBed.set_image(url=img)

        #source link button
        button = Button(label="Source", url=img)
        #view
        view = View()
        view.add_item(button)

        #respond
        await ctx.respond(embed=emBed, view=view)
        #cmd
        print('[{0}][{1}][{2}] query "dog" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

        constlog = self.bot.get_channel(CONSTLOG)
        await constlog.send('[{0}][{1}][{2}] query "dog" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

def setup(bot):
    bot.add_cog(funAPI(bot))