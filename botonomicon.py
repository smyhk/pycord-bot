# pycord.py bot rewrite

import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print('Connected to Discord endpoint')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('Hello smyhk. How about a nice game of chess?')


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: pong!! xSSS")
    print("user pinged the bot")


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    mbed = discord.Embed(title="{}'s info".format(user.name),
                         description="Here is the available info",
                         color=0x00ff00)
    mbed.add_field(name="Name", value=user.name, inline=True)
    mbed.add_field(name="ID", value=user.id, inline=True)
    mbed.add_field(name="Status", value=user.status, inline=True)
    mbed.add_field(name="Top Role", value=user.top_role, inline=True)
    mbed.add_field(name="Joined", value=user.joined_at, inline=True)
    mbed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=mbed)


@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Ya Motherfucker!".format(user.name))
    await bot.kick(user)


@bot.command(pass_context=True)
async def embed(ctx):
    mbed = discord.Embed(title="test", description="test embed", color=0x00ff00)
    mbed.set_footer(text="this is a footer")
    mbed.set_author(name="Smyhk")
    mbed.add_field(name="this is a field", value="a field value", inline=True)
    await bot.say(embed=mbed)


# Load the bot token from an environment variable
bot.run(os.environ.get('BOT_TOKEN'))