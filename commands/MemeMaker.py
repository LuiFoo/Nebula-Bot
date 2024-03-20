from discord import app_commands, Interaction, File
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import traceback

class MemeMaker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name = 'meme', description = '[Info] Criador de Meme')
    @app_commands.checks.cooldown(1,2, key = lambda i: (i.user.id))
    async def on_ping(self, interaction: Interaction, texto: str = None):  #Quando colocamos "= None" depois do texto, significa que essa condição é opcional
        try:
                #pedir para o discord dar um tempinho pro bot pensar
            await interaction.response.defer()
            
            
                #Checar se o usuário não colocou texto, para assim, colocar um padrão
            if texto is None:
                texto = "Lorem Ipsum Dolor Sit Amet"
                
            
                #Checar se o texto é muito grande, se sim, fatie-o
            texto.strip()

            j = 0
            limite = 15
            a = 0
                        
            for i in texto:
                j += 1
                
                if j > limite and i == ' ':
                    texto = texto[:j] + "\n" + texto[j:]
                                
                    limite += a + 10
                    a = 0
                    
                if j > limite:
                    a += 1
            
                #Selecionar e editar a imagem
            img = Image.open('images/urso-albino.jpg')
            
            dafont = ImageFont.truetype('fonts/insanibu.ttf', 50)
            
            draw = ImageDraw.Draw(img)
            draw.text((200, 10), texto, font = dafont, fill = (255, 255, 255), stroke_width = 2, stroke_fill = (0, 0, 0))
            
            img.save('images/img-save/urso-albino-edit.jpg')
            
                #Enviar para o chat do Discord
            await interaction.followup.send(file = File('images/img-save/urso-albino-edit.jpg'))
            
        except:
                #Caso algo não funcione, o terminal vai mostrar o erro, e o usuário recebe uma mensagem de erro no chat.
            print(f'Não foi possivel carregar imagem: {traceback.format_exc()}')
            await interaction.followup.send('Deu errado essa bagaça ;-;')
        
        
async def setup(bot):
    await bot.add_cog(MemeMaker(bot))