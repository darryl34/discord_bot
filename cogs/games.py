import discord
import random

from utils import default, lists
from discord.ext import commands

class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command(aliases = ['8ball'])
    async def eightball(self, ctx, *, question: commands.clean_content):
        """ Ask 8ball a question """
        answer = random.choice(lists.eightballresponse)
        await ctx.send(f"🎱 **Answer: ** {answer}")

    @commands.command(aliases = ['flip'])
    async def coinflip(self, ctx):
        """ Flip a coin! """
        coin = ["Heads", "Tails"]
        await ctx.send(f"You flipped a coin and got {random.choice(coin)}!")


def setup(bot):
    bot.add_cog(Games(bot))