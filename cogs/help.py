import discord
from discord.ext import commands
from discord.commands import slash_command, Option


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Help(bot))