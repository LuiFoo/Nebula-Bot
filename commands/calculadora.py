from imports import *
import traceback
from discord.ext import commands

class calculadora(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name = 'calcular', description = '[Info] Shows client latency')
    @app_commands.checks.cooldown(1,2, key = lambda i: (i.user.id))
    async def on_calculadora(self, interaction: Interaction, valor_01: float, valor_02: float, operacao: str):        

        try:
            resultado = {valor_01} {operacao} {valor_02}
            
            embed = Embed(title="Resultado da Calculadora", description=f"A expressão `{texto}` é igual a `{resultado}`", color=0x00ff00)
            
            await interaction.response.send_message(embed=embed)
            # ANTIGO
            # await interaction.response.send_message(f'O resultado de `{texto}` é: {resultado}')
            
            
        except:
            
            # Mostra o erro no terminal e envia uma mensagem de erro no chat do Discord.
            print(traceback.format_exc())
            await interaction.response.send_message('Ocorreu um erro ao calcular: ' + str(e))
        
        
async def setup(bot):
    await bot.add_cog(calculadora(bot))