import discord
from discord.ext import commands
from discord.commands import Option, slash_command
from datetime import datetime

import random

sv = 'Server'
cobo = 'Collot Bot'
BINARY = 871649185194184704

class utilitiesAPI(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('[{0}][{1}][cogs/info] Loaded : {2}'.format(sv, datetime.now(), self.__class__.__name__))
        print('[{0}][{1}][cogs/info/{2}] Command loaded : binary'.format(sv, datetime.now(), self.__class__.__name__))
        print('[{0}][{1}][cogs/info/{2}] Command loaded : morse'.format(sv, datetime.now(), self.__class__.__name__))
        print('[{0}][{1}][cogs/info/{2}] Command loaded : random'.format(sv, datetime.now(), self.__class__.__name__))
    
    @slash_command(guild_ids=[BINARY], description="To convert text to binary")
    async def binary(self, ctx, text : Option(str, "Input your text to convert")):
        
        #binary converter
        binary_converted = ' '.join(format(ord(i), 'b') for i in text)

        #embed
        emBed = discord.Embed()
        emBed.title="Binary coverted"
        emBed.color=0x00fffb

        emBed.add_field(name="Original text", value=f'**`{text}`**', inline=False)
        emBed.add_field(name="Binary", value=f'**`{binary_converted}`**', inline=False)

        #send message
        await ctx.respond(embed=emBed)
        #cmd
        print('[{0}][{1}][{2}] query "binary" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

    @slash_command(guild_ids=[BINARY], description="To convert text to morse code")
    async def morse(self, ctx, text : Option(str, "Input your text to convert")):
        
        #morse code dictionary
        code = {
            #Space
            ' ' : ' ',

            #lower
            'a' : '.-',
            'b' : '-...',
            'c' : '-.-.',
            'd' : '-..',
            'e' : '.',
            'f' : '..-.',
            'g' : '--.',
            'h' : '....',
            'i' : '..',
            'j' : '.---',
            'k' : '-.-',
            'l' : '.-..',
            'm' : '--',
            'n' : '-.',
            'o' : '---',
            'p' : '.--.',
            'q' : '--.-',
            'r' : '.-.',
            's' : '...',
            't' : '-',
            'u' : '..-',
            'v' : '...-',
            'w' : '.--',
            'x' : '-..-',
            'y' : '-.--',
            'z' : '--..',

            #UPPER
            'A' : '.-',
            'B' : '-...',
            'C' : '-.-.',
            'D' : '-..',
            'E' : '.',
            'F' : '..-.',
            'G' : '--.',
            'H' : '....',
            'I' : '..',
            'J' : '.---',
            'K' : '-.-',
            'L' : '.-..',
            'M' : '--',
            'N' : '-.',
            'O' : '---',
            'P' : '.--.',
            'Q' : '--.-',
            'R' : '.-.',
            'S' : '...',
            'T' : '-',
            'U' : '..-',
            'V' : '...-',
            'W' : '.--',
            'X' : '-..-',
            'Y' : '-.--',
            'Z' : '--..',

            #Number
            '1' : '.----',
            '2' : '..---',
            '3' : '...--',
            '4' : '....-',
            '5' : '.....',
            '6' : '-....',
            '7' : '--...',
            '8' : '---..',
            '9' : '----.',
            '0' : '-----',

            #Others
            ',' : '--..--',
            '.' : '.-.-.-',
            '?' : '..--..',
            '/' : '-..-.',
            '-' : '-....-',
            '_':'..--.-',
            '(' : '-.--.',
            ')' : '-.--.-',
            '!' : '-.-.--',
            '&':'.-...',
            ':':'---...',
            ';':'-.-.-.',
            '=':'-...-',
            '"':'.-..-.',
            '$':'...-..-',
            '@':'.--.-.'
        }

        #morse code converter
        morse_converted = ' '.join(code[i] for i in text)

        #embed
        emBed = discord.Embed()
        emBed.title="Morse code coverted"
        emBed.color=0x00fffb

        emBed.add_field(name="Original text", value=f'**`{text}`**', inline=False)
        emBed.add_field(name="Morse Code", value=f'**`{morse_converted}`**', inline=False)

        #send message
        await ctx.respond(embed=emBed)
        #cmd
        print('[{0}][{1}][{2}] query "morse" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

    @slash_command(guild_ids=[BINARY], description="Random numbeer by give min and max values")
    async def random(self, ctx, min : Option(int, "Input minimum number"), max : Option(int, "Input maximum number")):
        try :    
            random_num = random.randint(min, max)

            emBed = discord.Embed()
            emBed.title="Random Number"
            emBed.color=0x42f5a7

            emBed.add_field(name="Min and Max Value", value=f'Minimum value : **`{min}`**\nMaximum value: **`{max}`**', inline=False)
            emBed.add_field(name="Result Value", value=f'Result value : **`{random_num}`**', inline=False)

            #send message
            await ctx.respond(embed=emBed)
            #cmd
            
        except :
            await ctx.respond("Values error please try again")
    
        print('[{0}][{1}][{2}] query "random" server : {3} channel : {4}'
        .format(cobo, datetime.now(), ctx.author, ctx.guild, ctx.channel))

def setup(bot):
    bot.add_cog(utilitiesAPI(bot))