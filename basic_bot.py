import os
import discord

from utils import default
from discord.ext import commands

config = default.get("config.json")
print("Logging in...")

bot = commands.Bot(
    command_prefix = config.prefix,
    prefix = config.prefix)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

for file in os.listdir("cogs"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"cogs.{name}")

bot.run(config.token)