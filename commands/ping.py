from imports import *

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name = 'ping', description = '[Info] Shows client latency')
    @app_commands.checks.cooldown(1,2, key = lambda i: (i.user.id))
    async def on_ping(self, interaction: Interaction):
        
        botping = str(self.bot.latency)
        botping = botping[:4]
        
        await interaction.response.send_message(f'🛜 Ping! \n Ping está em {botping}')

async def setup(bot):
    await bot.add_cog(ping(bot))