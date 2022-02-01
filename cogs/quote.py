import os, sys
import datetime
sys.path.append(os.getcwd())
import discord
import jsonread, konachan
from model.frase import Frase
from discord.ext import commands

class Quote(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def quote(self, ctx):
        frase = Frase()
        frase.getRandomQuote()
        imagenes = konachan.getKonaImage(frase.anime)
        imagen = jsonread.getRandom(imagenes)
        embed = discord.Embed(title=frase.anime, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_thumbnail(url=frase.imagen)
        embed.add_field(name=frase.autor, value=frase.frase)
        embed.set_image(url=imagen)
        embed.set_footer(text='creado por Queso', icon_url='https://images.vexels.com/media/users/3/160051/isolated/preview/f9ce5cb5a15cc2cd4d5df19c4aff2858-queso-plano-by-vexels.png')
        await ctx.send(embed=embed)
    


def setup(client):
    client.add_cog(Quote(client))

