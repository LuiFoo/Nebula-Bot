from imports import *

class helloworld(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name = 'hello', description = '[Info] Um hello amigavel')
    @app_commands.checks.cooldown(1,2, key = lambda i: (i.user.id))
    async def on_helloworld(self, interaction: Interaction):
        try:
            
            Mensagens = ['Olá, como vai?',' Bom dia, tudo bem?', 'Boa tarde, como está?', 'Saudações, como tem passado?', 'Oi, espero que esteja bem.', 'Bom dia, espero que seu dia seja ótimo.', 'Olá, é um prazer vê-lo.', 'Boa tarde, fico feliz em vê-lo.', 'Olá, como posso ajudá-lo hoje?', 'Saudações, como posso ser útil?',  'Olá, espero que você não seja um Baiter!']
            await interaction.response.send_message(choice(Mensagens))    
                  
        except:
            
            #Caso algo não funcione, o terminal vai mostrar o erro, e o usuário recebe uma mensagem de erro no chat.
            print(f'Não foi possivel carregar imagem: {traceback.format_exc()}')
            await interaction.followup.send('Deu errado essa bagaça ;-;')
        
        
async def setup(bot):
    await bot.add_cog(helloworld(bot))