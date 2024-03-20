from discord import app_commands, Interaction, File
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import traceback

class MemeMaker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name = 'meme', description = '[Info] Criador de Meme')
    @app_commands.checks.cooldown(1,2, key = lambda i: (i.user.id))
    async def on_ping(self, interaction: Interaction, texto: str):
        try:
            await interaction.response.defer()
            
            img = Image.open('images/urso-albino.jpg')
            
            dafont = ImageFont.truetype('fonts/insanibu.ttf', 50)
            
            draw = ImageDraw.Draw(img)
            draw.text((490, 90), texto, font = dafont, fill = (255, 255, 255), stroke_width = 2, stroke_fill = (0, 0, 0))
            
            img.save('images/img-save/urso-albino-edit.jpg')
            
            await interaction.followup.send(file = File('images/img-save/urso-albino-edit.jpg'))
            
        except:
            
            print(f'Não foi possivel carregar imagem: {traceback.format_exc()}')
            await interaction.followup.send('Deu errado essa bagaça ;-;')
        
        
async def setup(bot):
    await bot.add_cog(MemeMaker(bot))