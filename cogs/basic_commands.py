import discord

from utils import default
from discord.ext import commands

class Discord_Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command()
    async def add(self, ctx, left: int, right: int):
        #self.left = left
        #self.right = right
        await ctx.send(left + right)

    @commands.command()
    async def welcome(self, ctx):
        await ctx.send("Welcome!")

    
    

def setup(bot):
    bot.add_cog(Discord_Info(bot))