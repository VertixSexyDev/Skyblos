import discord
from discord.ext import commands
import config


class SkyBlobsBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='s!',
            intents=discord.Intents().all(),
            case_insensitive=True,
            strip_after_prefix=True
        )

bot = SkyBlobsBot()


bot.run(config.TOKEN)