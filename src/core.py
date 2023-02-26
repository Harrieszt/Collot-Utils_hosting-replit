#[Main Script]
#[Discord Library]
import os
from keepAlive import keep_alive
import discord
from discord.ext import commands
from discord import Intents

token = os.environ['TOKEN']

#[Other Librarys]
from datetime import datetime
print(f'[Server][{datetime.now()}][info] Starting Collot discord bot')

class collot_bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        print(f'[Server][{datetime.now()}][info] Loading config')
        self.token = token
        super().__init__(command_prefix='c/', help_command=None, *args, **kwargs, intents=Intents.all())

#####[Main System]#####
bot = collot_bot(case_insensitive=True)

@bot.event
async def on_ready():
    print(f'[Server][{datetime.now()}][info] Logged on as {bot.user}')
    print(f'[Server][{datetime.now()}][info] Loading cogs')

if __name__ == "__main__":
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            bot.load_extension(f'cogs.{file[:-3]}')

    keep_alive()
    bot.run(token)