import os, sys
import datetime
sys.path.append(os.getcwd())
import discord
from model.server import Server
from discord.ext import commands

class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @commands.command()
    async def leave(self, ctx):
        channel = ctx.author.voice.channel
        vc = ctx.guild.voice_client
        if vc.is_connected():
            await vc.disconnect()
    

def setup(client):
    client.add_cog(Music(client))