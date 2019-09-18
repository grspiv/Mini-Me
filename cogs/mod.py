from discord.ext import commands
from discord import utils


class ModCog(commands.Cog):
    """Moderator Commands"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='clear', aliases=['purge', 'delete'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        """clears messages
        clear <amout of messages to delete>"""
        await ctx.channel.purge(limit=amount)


    @commands.command(name='kick')
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user):
        """kick a member from the server
        kick <member>"""
        await ctx.kick(user, reason=None)


    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user, amount):
        """ban a member from the server
        ban <member> [delete messages for x # of days]"""
        await ctx.ban(user, reason=None, delete_message_days=amount)


    @commands.command(name='unban')
    @commands.has_permissions(unban_members=True)
    async def unban(self, ctx, user):
        """unban a member from the server
        unban <member>"""
        await ctx.unban(user, reason=None)


def setup(bot):
    bot.add_cog(ModCog(bot))
