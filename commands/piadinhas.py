from imports import *

class piadinhas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name = 'piadinhas', description = '[Info] Piadas super engraçadas')
    @app_commands.checks.cooldown(1,2, key = lambda i: (i.user.id))
    async def on_ping(self, interaction: Interaction): 
        try:
            
            #pedir para o discord dar um tempinho pro bot pensar
            await interaction.response.defer()
             
            Piads = ['Toc Toc!', 'Caramba mermao']
            
            await interaction.followup.send(f'Tá preparado para a piada? {linesep} {choice(Piads)}')
                     
        except:
                
            #Caso algo não funcione, o terminal vai mostrar o erro, e o usuário recebe uma mensagem de erro no chat.
            print(traceback.format_exc())
            await interaction.followup.send('Deu errado essa bagaça ;-;')
        
        
async def setup(bot):
    await bot.add_cog(piadinhas(bot))