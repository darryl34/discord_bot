import discord
import time

from utils import default
from discord.ext import commands

config = default.get("config.json")

bot = commands.Bot(
    command_prefix = config.prefix,
    prefix = config.prefix)

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

    @commands.command()
    async def ping(self, ctx):
        """ Pong! """
        before = time.monotonic()
        before_ws = int(round(self.bot.latency * 1000, 1))
        message = await ctx.send("🏓 Pong")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")

def setup(bot):
    bot.add_cog(Discord_Info(bot))