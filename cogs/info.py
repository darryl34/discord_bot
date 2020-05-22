import time
import discord

from utils import default
from discord.ext import commands

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.get("config.json")

    @commands.command()
    async def ping(self, ctx):
        """ Pong! """
        before = time.perf_counter()
        before_ws = int(round(self.bot.latency * 1000, 1))
        message = await ctx.send("🏓 Pong!")
        ping = (time.perf_counter() - before) * 1000
        await message.edit(content=f"🏓 WS: {before_ws}ms  |  Ping: {int(ping)}ms")

    @commands.command()
    @commands.guild_only()
    async def profile(self, ctx, *, user: discord.Member = None):
        """ Gets info about a user """
        user = user or ctx.author

        show_roles = ', '.join(
            [f"<@&{x.id}>" for x in sorted(user.roles, key=lambda x: x.position, reverse=True) if x.id != ctx.guild.default_role.id]
        ) if len(user.roles) > 1 else 'None'

        embed = discord.Embed(colour=user.top_role.colour.value)
        embed.set_thumbnail(url=user.avatar_url)

        embed.add_field(name="Full name", value=user, inline=True)
        embed.add_field(name="Nickname", value=user.nick if hasattr(user, "nick") else "None", inline=True)
        embed.add_field(name="Account created", value=default.date(user.created_at), inline=True)
        embed.add_field(name="Joined this server", value=default.date(user.joined_at), inline=True)

        embed.add_field(name="Roles", value=show_roles, inline=False)

        await ctx.send(content=f"ℹ About **{user}**", embed=embed)

    @commands.group()
    @commands.guild_only()
    async def serverinfo(self, ctx):
        """ Checks info about current server """
        if ctx.invoked_subcommand is None:
            findbots = sum(1 for member in ctx.guild.members if member.bot)

            embed = discord.Embed()

            if ctx.guild.icon:
                embed.set_thumbnail(url=ctx.guild.icon_url)
            if ctx.guild.banner:
                embed.set_image(url=ctx.guild.banner_url_as(format="png"))

            embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
            embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
            embed.add_field(name="Members", value=ctx.guild.member_count, inline=True)
            embed.add_field(name="Bots", value=findbots, inline=True)
            embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
            embed.add_field(name="Region", value=ctx.guild.region, inline=True)
            embed.add_field(name="Created", value=default.date(ctx.guild.created_at), inline=True)
            await ctx.send(content=f"ℹ information about **{ctx.guild.name}**", embed=embed)

    @commands.command()
    async def source(self, ctx):
        """ Sends a link to repository on GitHub """
        await ctx.send("Oops, the repository is currently private. Please try again later.")

def setup(bot):
    bot.add_cog(Information(bot))