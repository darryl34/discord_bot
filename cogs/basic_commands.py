import discord

from utils import default
from discord.ext import commands

class test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command(hidden=True)
    async def add(self, ctx, left: int, right: int):
        """Adds two numbers"""
        self.left = left
        self.right = right
        await ctx.send(left + right)

    @commands.command()
    async def hello(self, ctx):
        """ Hello """
        await ctx.send(f"Hello there **{ctx.author.nick}** ")


def setup(bot):
    bot.add_cog(test(bot))