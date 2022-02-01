import traceback
import sys
from utility.utilidad import formatSeconds
from discord.ext import commands
import discord


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        """The event triggered when an error is raised while invoking a command.
        ctx   : Context
        error : Exception"""

        if hasattr(ctx.command, 'on_error'):
            return
        
        ignored = (commands.CommandNotFound, commands.UserInputError)
        error = getattr(error, 'original', error)
        
        if isinstance(error, ignored):
            return

        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f'{ctx.message.author.mention} Vuelve a intentar en {formatSeconds(int(error.retry_after))}')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(f'El comando {ctx.message.content} no existe')

        elif isinstance(error, commands.DisabledCommand):
            return await ctx.send(f'{ctx.command} ha sido desabilitado.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.author.send(f'{ctx.command} No se puede usar con mensajes privados.')
            except:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                return await ctx.send('I could not find that member. Please try again.')
            
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
    
    @commands.command(name='repeat', aliases=['mimic', 'copy'])
    async def do_repeat(self, ctx, *, inp: str):
        await ctx.send(inp)

    @do_repeat.error
    async def do_repeat_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'inp':
                await ctx.send("You forgot to give me input to repeat!")
                

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))