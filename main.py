from discord.ext.commands import Bot
from discord import Intents
from os import listdir
from asyncio import run
import traceback

bot = Bot(command_prefix = '!', intents = Intents.all(), help_command = None)

botToken = input('Digite o seu Token Discord: ')

async def load(bot):
    try:
        for file in listdir('commands'):
            if file.endswith('.py'):
                cog = file[:-3]
                await bot.load_extensions(f'commands.{cog}')
    except:
        print(f'Não foi possivel carregar os cogs: {traceback.format_exc()}')

async def main():
    await load(bot)
    await bot.start(botToken)
    
run(main())