import discord
from discord.ext import commands
import config
import os
import sqlite3


class SkyBlobsBot(commands.Bot):
    def __init__(self):
        self.db = sqlite3.connect("utils/databases/main.db")
        self.dbcursor = self.db.cursor()

        super().__init__(
            command_prefix='s!',
            intents=discord.Intents().all(),
            case_insensitive=True,
            strip_after_prefix=True
        )

        for filename in os.listdir('./cogs'):
            if filename.endswith(".py"):
                self.load_extension(f"cogs.{filename[:-3]}")

    async def on_ready(self):
        print(f"{self.user.name} is now online | ID: {self.user.id}")


bot = SkyBlobsBot()

bot.run(config.TOKEN)