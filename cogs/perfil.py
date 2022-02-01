import os, sys
import datetime
sys.path.append(os.getcwd())
import discord
from model.server import Server
from model.usuario import Usuario
from model.server import Server
from model.titulo import Titulo
from discord.ext import commands

class Perfil(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def perfil(self, ctx, *user: discord.Member):
        server = Server(idserver=str(ctx.guild.id))
        server.getServer()
        if ctx.message.content == f'{server.prefijo}perfil':
            usuario = Usuario(idusuario=str(ctx.message.author.id))
            if usuario.existe():
                if not usuario.existePerfilTitulos():
                    usuario.setTituloDefault()
                usuario.getUsuario()
                embed = discord.Embed(title=usuario.nombre, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
                embed.set_image(url=usuario.banner_url)
                embed.add_field(name='Titulo', value=usuario.getTitulo(), inline=False)
                embed.add_field(name='Biografia', value=usuario.biografia, inline=False)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                await ctx.send(embed=embed)
            else:
                usuario.idusuario = ctx.message.author.id
                usuario.nombre = ctx.message.author.name
                usuario.setUsuario()
                usuario.setTituloDefault()
                embed = discord.Embed(title=usuario.nombre, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
                embed.set_image(url=usuario.banner_url)
                embed.add_field(name='Titulo', value=usuario.getTitulo(), inline=False)
                embed.add_field(name='Biografia', value=usuario.biografia, inline=False)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                await ctx.send(embed=embed)
        else:
            usuario2 = Usuario(idusuario=str(user[0].id))
            if usuario2.existe():
                usuario2.getUsuario()
                embed = discord.Embed(title=usuario2.nombre, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
                embed.set_image(url=usuario2.banner_url)
                embed.add_field(name='Titulo', value=usuario2.getTitulo(), inline=False)
                embed.add_field(name='Biografia', value=usuario2.biografia, inline=False)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                embed.set_thumbnail(url=user[0].avatar_url)
                await ctx.send(embed=embed)
            else:
                await ctx.send(f'{user[0].mention} no tiene perfil')

    @perfil.command()
    async def setbiografia(self, ctx, *, biografia):
        usuario = Usuario(idusuario=str(ctx.message.author.id))
        if usuario.existe():
            usuario.getUsuario()
            usuario.biografia = biografia
            usuario.updateBiografia()
            await ctx.send(f'{ctx.author.mention} tu biografia a sido actualizada')

    @perfil.command()
    async def setbanner(self, ctx, url: str):
        if ".jpg" in url or ".png" in url or ".gif" in url:
            usuario = Usuario(idusuario=str(ctx.message.author.id))
            if usuario.existe():
                usuario.getUsuario()
                usuario.banner_url = url
                usuario.updateBanner()
                await ctx.send(f'{ctx.author.mention} tu banner a sido actualizado')
        else:
            await ctx.send(f'{ctx.author.mention} Error debe ser una imagen con formato .jpg .png .gif')

    @perfil.command()
    async def settitulo(self, ctx, id=2):
        server = Server(idserver=str(ctx.guild.id))
        server.getServer()
        usuario = Usuario(idusuario=str(ctx.message.author.id))
        
        print(ctx.message.content)
        if ctx.message.content == f'{server.prefijo}perfil settitulo':
            embed = discord.Embed(title='Tus Titulos:', color=discord.Color.red(), description='aqui podras encontrar tu lista de Titulos y su respectivo id', timestamp=datetime.datetime.utcnow())
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            for titulo in usuario.getTitulos():
                embed.add_field(name=f'ID: **{titulo[0]}**    Rareza: **{titulo[2]}**', value=f'**`{titulo[1].upper()}`**', inline=False)
            await ctx.send(embed=embed)
        else:
            titulo = Titulo(id=id)
            if titulo.existe():
                if usuario.existeTituloPerfil(id=id):
                    usuario.titulo_id=id
                    usuario.updateTitulo()
                    await ctx.send(f'{ctx.message.author.mention} tu Titulo a sido actualizado por **{usuario.getTitulo()}**')
                else:
                    title = Titulo(id=id)
                    await ctx.send(f'No posees el titulo **{title.getTitulo()}**')
            else:
                await ctx.send(f'{ctx.message.author.mention} Titulo no existe')
        
    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        usuario = Usuario(idusuario=str(ctx.message.author.id))
        if usuario.existe():
            usuario.getUsuario()
            usuario.maicoins = usuario.maicoins + 50
            usuario.updateMaiCoins()
            await ctx.send(f'{ctx.message.author.mention} haz obtenido 50 Maicoins ahora tienes {usuario.maicoins} Maicoins')


                
    

def setup(client):
    client.add_cog(Perfil(client))