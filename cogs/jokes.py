from discord.ext import commands
from random import  randint


with open('./jokes/dadjokes.txt', 'r') as djokeBotlist:
    djokelist = djokeBotlist.read().splitlines()

with open('./jokes/blondejokes.txt', 'r') as bjokeBotlist:
    bjokelist = bjokeBotlist.read().splitlines()

with open('./jokes/firefly.txt', 'r') as fireBotlist:
    firelist = fireBotlist.read().splitlines()


class JokesCog(commands.Cog):
    """Jokes"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='dadjoke')
    async def dadjoke(self, ctx):
        """Want to hear a dad joke?"""
        joke = bjokelist[randint(0, len(bjokelist)-1)]
        await ctx.send(joke)


    @commands.command(name='blondejoke')
    async def blonde(self, ctx):
        """I have tons of blonde jokes!"""
        joke = bjokelist[randint(0, len(bjokelist)-1)]
        await ctx.send(joke)


    @commands.command(name='firefly')
    async def firefly(self, ctx):
        """Feelin like a quote form the best gorram show in the 'verse?"""
        quote = firelist[randint(0, len(firelist)-1)]
        await ctx.send(quote)


def setup(bot):
    bot.add_cog(JokesCog(bot))
