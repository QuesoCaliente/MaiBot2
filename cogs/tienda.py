import os, sys
import asyncio
import datetime
sys.path.append(os.getcwd())
import discord
from model.paginator import Paginar
from model.paginator import getPaginas
from model.server import Server
from model.usuario import Usuario
from model.titulo import Titulo
from discord.ext import commands

class Tienda(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def tienda(self, ctx):
        server = Server(idserver=str(ctx.guild.id))
        server.getServer()
        embed = discord.Embed(title='Tienda', description='Elige la opcion(numero) que deseas acceder PD: tienes 10 segundos', color=discord.Color.blurple(), timestamp=datetime.datetime.utcnow())
        embed.add_field(name='**1.**', value='**Titulos**', inline=False)
        embed.add_field(name='**2**', value='**Multiplicadores**', inline=False)
        msg = await ctx.send(embed=embed)
        variable = 1
        variable2 = 1
        def check(response):
            return response.content =='1' or response.content == '2' and ctx.message.author.id == response.author.id
        def check2(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '➡️' or str(reaction.emoji) == '⬅️'
        try:
            response = await self.client.wait_for('message', check=check ,timeout=10)
        except asyncio.TimeoutError:
            await ctx.send('Se acabo el tiempo')
        else:
            await msg.delete()
            titulos = Titulo(id=1)
            if response.content == '1': #Titulos
                paginaActual = 1
                cantItem = 10
                paginaTotal = getPaginas(titulos.getAll(), cantItem)
                embedTitulos = discord.Embed(title='Tienda: Titulos', description=f'Elige el Titulo que deseas comprar y escribe **{server.prefijo}tienda titulo <ID>**', color=discord.Color.blurple(), timestamp=datetime.datetime.utcnow())
                tit = Paginar(titulos.getAll(), paginaActual, cantItem)
                for titulo in tit:
                    embedTitulos.add_field(name=f'**{titulo[0]}** Rareza: **{titulo[3]}**', value=f'**{titulo[1]}** precio: **{titulo[2]}**', inline=False)
                msg2 = await ctx.send(embed=embedTitulos)
                await msg2.add_reaction('⬅️')
                await msg2.add_reaction('➡️')
                while variable == 1:
                    try:
                        reaction, user = await self.client.wait_for('reaction_add', timeout=10, check=check2)
                    except asyncio.TimeoutError:
                        await ctx.send('Se acabo el tiempo para reaccionar')
                        variable = 2
                    else:
                        if str(reaction.emoji) == '➡️':
                            paginaActual= paginaActual+1
                            if paginaActual > paginaTotal:
                                await msg2.remove_reaction('➡️', ctx.message.author)
                                paginaActual = paginaActual-1
                            else:
                                tit = Paginar(titulos.getAll(), paginaActual, cantItem)
                                embedTitulosNext= discord.Embed(title='Tienda: Titulos', description=f'Elige el Titulo que deseas comprar y escribe **{server.prefijo}tienda titulo <ID>**', color=discord.Color.blurple(), timestamp=datetime.datetime.utcnow())
                                for titulo2 in tit:
                                    embedTitulosNext.add_field(name=f'**{titulo2[0]}** Rareza: **{titulo2[3]}**', value=f'**{titulo2[1]}** precio: **{titulo2[2]}**', inline=False)
                                await msg2.remove_reaction('➡️', ctx.message.author)
                                await msg2.edit(embed=embedTitulosNext)


                        elif str(reaction.emoji) == '⬅️':
                            if paginaActual == 1:
                                await msg2.remove_reaction('⬅️', ctx.message.author)
                            else:
                                paginaActual= paginaActual-1
                                tit = Paginar(titulos.getAll(), paginaActual, cantItem)
                                embedTitulosPrevious = discord.Embed(title='Tienda: Titulos', description=f'Elige el Titulo que deseas comprar y escribe **{server.prefijo}tienda titulo <ID>**', color=discord.Color.blurple(), timestamp=datetime.datetime.utcnow())
                                for titulo3 in tit:
                                    embedTitulosPrevious.add_field(name=f'**{titulo3[0]}** Rareza: **{titulo3[3]}**', value=f'**{titulo3[1]}** precio: **{titulo3[2]}**', inline=False)
                                await msg2.remove_reaction('⬅️', ctx.message.author)
                                await msg2.edit(embed=embedTitulosPrevious)
                    
    @tienda.command()
    async def titulo(self, ctx, id:int):
        usuario = Usuario(idusuario=str(ctx.message.author.id))
        titulo = Titulo(id=id)
        if usuario.existe() and usuario.existePerfilTitulos():
            usuario.getUsuario()
            if usuario.maicoins >= titulo.getPrecio():
                usuario.maicoins = usuario.maicoins - titulo.getPrecio()
                usuario.updateMaiCoins()
                usuario.titulo_id = id
                usuario.setTituloPerfil()
                await ctx.send(f'{ctx.message.author.mention} haz comprado el titulo **{titulo.getTitulo()}** ahora tienes {usuario.maicoins} Maicoins')
            else:
                await ctx.send(f'{ctx.message.author.mention} No tienes MaiCoins suficiente ({usuario.maicoins})')


def setup(client):
    client.add_cog(Tienda(client))