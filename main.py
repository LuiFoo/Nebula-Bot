from discord.ext.commands import Bot
from dotenv import load_dotenv
from os import listdir, getenv
from discord import Intents
from asyncio import run
import traceback

load_dotenv()

bot = Bot(command_prefix = '!', intents = Intents.all(), help_command = None)

async def load(bot):
    try:
        await bot.load_extension('manager')
        
        for file in listdir('commands'):
            if file.endswith('.py'):
                cog = file[:-3]
                await bot.load_extension(f'commands.{cog}')
    except:
        print(f'Não foi possivel carregar os cogs: {traceback.format_exc()}')

async def main():
    Token = getenv("TOKEN")
    await load(bot)
    await bot.start(Token)
    
run(main())