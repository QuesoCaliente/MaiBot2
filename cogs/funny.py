import os, sys
import datetime
sys.path.append(os.getcwd())
import discord
from model.server import Server
from discord.ext import commands

class Funny(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kiss(self, ctx, user: discord.User):
        print(user.mention)
        print(type(user))
        print(f'@{self.client.user.name}')
        print(user.mention == f'@{self.client.user.name}')
        if  user.name is not self.client.user.name:
            await ctx.send(f'{ctx.author.mention} le dio un abrazo a {user}')
        elif user.name == self.client.user.name:
            await ctx.send(f'Aww {ctx.author.mention} un abrazo para mi? ')
    

def setup(client):
    client.add_cog(Funny(client))