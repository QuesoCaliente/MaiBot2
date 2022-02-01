import os, sys
import datetime
sys.path.append(os.getcwd())
import discord
from model.server import Server
from discord.ext import commands

class Configuracion(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def setchannel(self, ctx):
        server = Server(idserver=ctx.guild.id, idchannel=ctx.message.channel.id)
        server.updateChannel()
        await ctx.send(f'Canal Actualizado Exitosamente, nuestro nuevo canal para hablar es {ctx.message.channel.name}')


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def resetchannel(self, ctx):
        server = Server(idserver=ctx.guild.id)
        server.getServer()
        server.resetChannel()
        await ctx.send(f'Se ha reseteado nuestro canal, utiliza {server.prefijo}setchannel para configurar un nuevo canal')



    @commands.command()
    @commands.has_permissions(administrator=True)
    async def prefix(self, ctx, prefix):
        server = Server(idserver=str(ctx.guild.id))
        server.getServer()
        server.prefijo = prefix
        server.updatePrefix()
        await ctx.send(f'Prefijo Actualizado a {server.prefijo}')

    @prefix.error
    async def prefix_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send(f'{ctx.message.author.mention}  No tienes permisos de __**Administrador**__')

    

def setup(client):
    client.add_cog(Configuracion(client))