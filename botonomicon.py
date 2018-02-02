# pycord.py bot rewrite

import os
import logging
import datetime
import discord
from discord.ext import commands


# Creates a logfile to store debugging info
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print('Connected to Discord endpoint')
    print('Username: ' + bot.user.name)
    print('ID: ' + bot.user.id)
    print('Hello smyhk. How about a nice game of chess?')
    await bot.change_presence(game=discord.Game(name="with his robot balls"))


@bot.event
async def on_member_join(member):
    msg = "" + str(member.mention) + " joined at: " + str(member.joined_at)
    await bot.send_message(bot.get_channel("373673083854389249"), msg)


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
async def serverinfo(ctx):
    mbed = discord.Embed(title="{}'s info".format(ctx.message.server.name),
                         description="Here there be dragons.",
                         color=0x00ff00)
    mbed.add_field(name="Guild Name",
                   value=ctx.message.server.name, inline=True)
    mbed.add_field(name="Guild ID",
                   value=ctx.message.server.id, inline=True)
    mbed.add_field(name="Roles",
                   value=str(len(ctx.message.server.roles)), inline=True)
    mbed.add_field(name="Members",
                   value=ctx.message.server.member_count, inline=True)
    mbed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=mbed)


@bot.command(pass_context=True)
@commands.has_role("dumbass")
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
