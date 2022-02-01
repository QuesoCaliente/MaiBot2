import os, sys
import datetime
sys.path.append(os.getcwd())
import discord
import jsonread
from model.server import Server
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.group(invoke_without_command=True)
    async def help(self, ctx):
        server = Server(idserver=ctx.guild.id)
        server.getServer()
        if ctx.message.content == f'{server.prefijo}help':
            server = Server(idserver=str(ctx.guild.id))
            server.getServer()
            embed = discord.Embed(title='Ayuda', description=f'Utiliza {server.prefijo}help <modulo> para obtener mas informacion sobre el modulo correspondiente', timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
            embed.set_author(name='Ayuda', icon_url=self.client.user.avatar_url)
            embed.add_field(name='Diversion', value=f'`{server.prefijo}help diversion`')
            embed.add_field(name='Perfil', value=f'`{server.prefijo}help perfil`')
            embed.add_field(name='Configuracion', value=f'`{server.prefijo}help configuracion`')
            embed.add_field(name='Twitch', value=f'`{server.prefijo}help twitch`')
            await ctx.send(embed=embed)
            

    @help.command()
    async def diversion(self, ctx):
        server = Server(idserver=str(ctx.guild.id))
        server.getServer()
        embed = discord.Embed(title='Diversion', timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name=f'{server.prefijo}quote', value='Devuelve una frase aleatoria de Anime', inline=False)
        embed.add_field(name=f'{server.prefijo}emoji <emoji>', value='Remplaza <emoji> por un Emoji y obten la url de la imagen', inline=False)
        embed.set_author(name='Ayuda', icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)

    @help.command()
    async def perfil(self, ctx):
        server = Server(idserver=str(ctx.guild.id))
        server.getServer()
        embed = discord.Embed(title='Perfil', timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name=f'{server.prefijo}perfil', value='Muestra tu perfil', inline=False)
        embed.add_field(name=f'{server.prefijo}perfil @usuario', value='Muestra el perfil del usuario mencionado', inline=False)
        embed.add_field(name=f'{server.prefijo}perfil settitulo', value='Muestra todos los titulos adquiridos `Tienda para adquirirlos en proceso`', inline=False)
        embed.add_field(name=f'{server.prefijo}perfil settitulo <id>', value='Remplaza <id> por un id de titulo que poseas para establecer', inline=False)
        embed.add_field(name=f'{server.prefijo}perfil setbiografia <biografia>', value='Remplaza <biografia> por tu nueva descripcion para mostrar', inline=False)
        embed.add_field(name=f'{server.prefijo}perfil setbanner <url>', value='Remplaza <url> por un enlace para tu nuevo banner solo se admite (jpg,png,gif)', inline=False)
        embed.set_author(name='Ayuda', icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)

    @help.command()
    async def configuracion(self, ctx):
        server = Server(idserver=str(ctx.guild.id))
        server.getServer()
        embed = discord.Embed(title='Configuracion', timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name=f'{server.prefijo}prefix <prefijo>', value='Cambia <prefijo> por el nuevo prefijo para el bot', inline=False)
        embed.add_field(name=f'{server.prefijo}setchannel', value='Solo podras usar el Bot en el canal que ejecutes este comando', inline=False)
        embed.add_field(name=f'{server.prefijo}resetchannel', value=f'Resetea la configuracion de {server.prefijo}setchannel para configurar un nuevo canal para el Bot', inline=False)
        embed.set_author(name='Ayuda', icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)


    @help.command()
    async def twitch(self, ctx):
        server = Server(idserver=str(ctx.guild.id))
        server.getServer()
        embed = discord.Embed(title='Twitch', timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name=f'{server.prefijo}twitch setbot', value='Establece el canal de chat en donde anunciare cuando un Streamer este Online', inline=False)
        embed.add_field(name=f'{server.prefijo}twitch <usuario> <*mensaje>', value='Remplaza <usuario> por un usuario de twitch y  <*mensaje> por el mensaje que quieres mostrar cuando haga stream PD: el mensaje puede contener espacios', inline=False)
        embed.add_field(name=f'{server.prefijo}¡twitch delete <usuario>', value='Remplaza <usuario> por el usuario de twitch que desees eliminar de las Alertas', inline=False)
        embed.add_field(name=f'{server.prefijo}¡twitch resetbot', value='Elimina el canal para anunciar cuando el Streamer este Onlines', inline=False)
        embed.set_author(name='Ayuda', icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)



    

    @commands.command()
    async def emoji(self, ctx, emoji: discord.PartialEmoji):
        await ctx.send(f'`:{emoji.name}:` {emoji.url}')

def setup(client):
    client.add_cog(Help(client))