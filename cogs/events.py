import discord
from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.errors.CommandNotFound):
            await ctx.send(embed=discord.Embed(description=f"**There is no such command with name `{ctx.message.content[2:]}`\n-----------------------------------------------------Use `{ctx.clean_prefix}help` for more info!**", color=discord.Color.red()))


def setup(bot):
    bot.add_cog(Events(bot))