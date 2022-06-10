import os, sys
sys.path.append(os.getcwd())
import discord
from discord.ext import commands
from discord.utils import get
import datetime
import jsonread
import konachan
from model.usuario import Usuario
from model.server import Server
from decouple import config


def get_prefix(client, message):
    server = Server(idserver=str(message.guild.id))
    server.getServer()
    return server.prefijo


bot = commands.Bot(command_prefix=get_prefix, description='QuotesAnime Bot')
bot.remove_command('help')

bot.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'http://lava.link:80',
        'identifier' : 'MAIN',
        'region': 'singapore'
    }
]




#@bot.command()
#async def help(ctx):
    #print('soy el comando ayuda')


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def stats(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description='Bot de frases', timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_thumbnail(url='https://i.imgur.com/JEvAzTT.jpg')
    await ctx.send(embed=embed)




@bot.command()
async def perfiluser(ctx, user: discord.User):
    usuario2 = Usuario(idusuario=str(user.id))
    if usuario2.existe():
        usuario2.getUsuario()
        embed = discord.Embed(title=usuario2.nombre, timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_image(url=usuario2.banner_url)
        embed.add_field(name='Titulo', value=usuario2.getTitulo())
        embed.add_field(name='Biografia', value=usuario2.biografia)
        embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f'{user.mention} no tiene perfil')


        



@bot.event
async def on_guild_join(ctx):
    idope = str(ctx.id)
    server = Server(nombre=ctx.name, idserver=idope)
    if server.existe():
        pass
    else:
        server.setServer()

@bot.event
async def on_guild_remove(ctx):
    print('SE FUE DEL SERVIDOR')
    print(ctx.id)
    print(ctx.name)


@bot.check
async def canal_habilitado(ctx):
    server = Server(idserver=str(ctx.guild.id))
    if server.existe():
        server.getServer()
        if server.existeChannel():
            print(ctx.message.channel.id == int(server.idchannel) )
            return ctx.message.channel.id == int(server.idchannel) 
        else:
            return True
    return False




#eventos
@bot.event
async def on_ready():
    
    await bot.change_presence(activity=discord.Game(name=f'¡help | {len(list(bot.guilds))} servers'))
    await bot.load_extension('dismusic')
    print('Bot en linea')

for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(config('token'))