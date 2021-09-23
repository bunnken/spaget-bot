import discord
from discord.ext import commands
import argparse
import os
import asyncio
import platform
from utils import getToken


def init():
    if platform.system() == "Windows": # fix for 'RuntimeError: Event loop is closed'
        print("Applying fixes for the Windows platform...")
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class Spaget(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="t ",
            help_commands=None,
            intents=discord.Intents.all()
        )

        for i in os.listdir("cogs/"):
            if i.endswith(".py"):
                self.load_extension("cogs." + i[:-3])

    async def close(self):
        print("Shutting down...")
        await super().close()

    def run(self, token: str = None):
        if not token:
            token = getToken()

        super().run(token, reconnect=True)


if __name__ == "__main__":
    init()

    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--token", type=str, help="The token that will be used to login with the bot.")
    token = parser.parse_args().token

    Spaget().run(token)
