import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time


client = discord.Client()
prefix = commands.Bot(command_prefix="!")


@client.event
async def on_ready():
    print("Bot ready...")


@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")

client.run(os.environ.get('BOT_TOKEN'))
