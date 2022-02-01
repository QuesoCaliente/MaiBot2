import os, sys
import datetime
sys.path.append(os.getcwd())
import discord
import twitch
from model.server import Server
from model.twitch_channel import twitch_channel
from discord.ext import commands, tasks

class Twitchmsg(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.twitchonline.start()

    @commands.group(invoke_without_command=True)
    async def twitch(self, ctx, canal:str, *, mensaje):
        twitch = twitch_channel(idservidor=str(ctx.guild.id), nombre=canal, mensaje=mensaje)
        if twitch.is_limit():
            await ctx.send("Ya haz alcanzado el **maximo** de Canales para mostrar en tu servidor")
        else:
            if twitch.existeCanal():
                await ctx.send("El canal que estas intentando agregar ya se encuentra en el servidor")
            else:
                twitch.agregarCanal()
                await ctx.send(f"**{twitch.nombre}** ha sido agregado exitosamente")

    @twitch.command()
    @commands.has_permissions(administrator=True)
    async def setbot(self, ctx):
        server = Server(idserver=str(ctx.guild.id))
        server.getServer()
        server.idchanneltwitch = ctx.message.channel.id
        server.updateChannelTwitch()
        await ctx.send('Canal para transmisiones de Twitch Actualizado')

    @twitch.command()
    @commands.has_permissions(administrator=True)
    async def delete(self, ctx, canal:str):
        twitchc = twitch_channel(nombre=f'{canal}', idservidor=str(ctx.guild.id))
        if twitchc.existeCanalTwitch():
            twitchc.eliminarCanal()
            await ctx.send(f'Se ha eliminado el canal **{twitchc.nombre}**')


    @twitch.command()
    @commands.has_permissions(administrator=True)
    async def resetbot(self, ctx):
        server = Server(idserver=str(ctx.guild.id))
        server.getServer()
        server.resetChannelTwitch()
        await ctx.send(f'Se ha eliminado el canal para transmisiones de *Twitch* vuelve a usar {server.prefijo}twitch setbot para configurar otro canal')

    @twitch.command()
    @commands.has_permissions(administrator=True)
    async def setfalse(self, ctx):
        canales = twitch_channel(idservidor=str(ctx.guild.id))
        for canal in canales.getCanales():
            canales.updateOnline(name=canal[0],onlain=False)
        await ctx.send('Online Twitch Set False')
            




    @tasks.loop(minutes=3.0)
    async def twitchonline(self):
        for server in self.client.guilds:
            serv = Server(idserver=str(server.id))
            canal = twitch_channel(idservidor=str(server.id))
            if serv.existe():
                serv.getServer()
                if serv.existeChannelTwitch():
                    if canal.existeCanal():
                        helix = twitch.Helix('xfansj2gne5s8r35jx6lxpd7aylz2f')
                        for user in canal.getCanales():
                            streamer = helix.user(user[0])
                            if streamer.is_live: 
                                if user[2]:
                                    pass
                                else:
                                    canal.updateOnline(user[0], True)
                                    
                                    stream = streamer.stream
                                    embed = discord.Embed(title=f'{stream.title}', url=f'https://www.twitch.tv/{user[0]}', description=f'{user[1]}' , timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
                                    embed.set_author(name=f'{user[0]}', icon_url=streamer.profile_image_url)
                                    embed.set_thumbnail(url=streamer.profile_image_url)
                                    urlimagen = stream.thumbnail_url
                                    urlimagen = urlimagen.replace('{width}', '600')
                                    urlimagen = urlimagen.replace('{height}', '300')
                                    embed.set_image(url=urlimagen)
                                    print(stream.thumbnail_url)
                                    embed.add_field(name='Viewers', value=f'{stream.viewer_count}')
                                    channel = self.client.get_channel(int(serv.idchanneltwitch))
                                    await channel.send(embed=embed)
                            else:
                                if user[2]:
                                    canal.updateOnline(user[0], False)
                                else:
                                    pass
                            


            


    

def setup(client):
    client.add_cog(Twitchmsg(client))