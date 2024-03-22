from imports import *

class profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_message(self, ctx):
        try:
                #pedir para o discord dar um tempinho pro bot pensar
            await interaction.response.defer()
            
            if not ctx.author.bot:
                with open('jsons/usuarios.json')

            
            embed = Embed(title = 'PROFILE', )         
            
        except:
                #Caso algo não funcione, o terminal vai mostrar o erro, e o usuário recebe uma mensagem de erro no chat.
            print(f'Não foi possivel carregar imagem: {traceback.format_exc()}')
            await interaction.followup.send('Deu errado essa bagaça ;-;')
        
        
async def setup(bot):
    await bot.add_cog(profile(bot))