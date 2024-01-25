import discord
from discord import app_commands
from discord.ui import Button, View
from discord.ext import commands
import os
import asyncio
import json
from Commands.members import mView

with open("Data/config.json", "r+", encoding="utf-8") as f:
    config = json.load(f)
    token = config["token"]


class aclient(commands.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.default(),
                         command_prefix="!", help_command=None)
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        game = discord.Game(f"Coding | /help")
        await self.change_presence(status=discord.Status.online, activity=game)
        print(f"We have logged in as {self.user}.")
        self.add_view(mView())
        




client = aclient()


@client.event
async def on_guild_join(guild: discord.Guild):
    await client.tree.sync(guild=guild)


@client.event
async def setup_hook():
    logs = await client.tree.sync()
    print(f"[!] Synced {len(logs)} commands")


async def loadcogs():
    for files in os.listdir(f'Commands'):
        if files.endswith(".py"):
            await client.load_extension(f'Commands.{files[:-3]}')


async def startup():
    async with client:
        await loadcogs()
        await client.start(token)



asyncio.run(startup())
