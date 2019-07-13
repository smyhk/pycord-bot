# pycord.py bot rewrite
# TODO: refactor into classes

import os
# import logging
import datetime
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix="!")

game = discord.Activity(name="Ass Blasters 7", type=3)


@bot.event
async def on_ready():
    print('Connected to Discord endpoint')
    # print('Username: ' + {0.user}).format()
    # print('ID: ' + {0.user.id}).format()
    print('Hello smyhk. How about a nice game of chess?')
    await bot.change_presence(status=discord.Status.idle, activity=game)
    # game=discord.Game(name="Ass Blasters 7", type=3)


@bot.event
async def on_member_join(ctx):
    print(str(ctx.member.mention) + " joined at: " + str(ctx.member.joined_at))
    msg = "Welcome to the server " + str(ctx.member.mention) + "! Type !help for more information."
    await ctx.send(msg)


@bot.event
async def on_member_remove(ctx):
    print(str(ctx.member.mention) + " left at: " + str(datetime.datetime.now()))
    # await bot.send_message(bot.get_channel("373673083854389249"), msg)


@bot.command()
async def ping(ctx):
    await ctx.send(":ping_pong: pong!! xSSS")
    print("user pinged the bot")


@bot.command()
async def info(ctx, user: discord.Member):
    mbed = discord.Embed(title="{}'s info".format(user.nick),
                         description="Here is the available info",
                         color=0x00ff00)
    mbed.add_field(name="Name", value=user.nick, inline=True)
    mbed.add_field(name="ID", value=user.id, inline=True)
    mbed.add_field(name="Status", value=user.status, inline=True)
    mbed.add_field(name="Top Role", value=user.top_role, inline=True)
    mbed.add_field(name="Joined", value=user.joined_at, inline=True)
    mbed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=mbed)


@bot.command()
async def serverinfo(ctx):
    mbed = discord.Embed(title="{}'s info".format(ctx.guild.name),
                         description="Here there be dragons.",
                         color=0x00ff00)
    mbed.add_field(name="Guild Name",
                   value=ctx.message.guild.name, inline=True)
    mbed.add_field(name="Guild ID",
                   value=ctx.message.guild.id, inline=True)
    mbed.add_field(name="Roles",
                   value=str(len(ctx.message.guild.roles)), inline=True)
    mbed.add_field(name="Members",
                   value=ctx.message.guild.member_count, inline=True)
    mbed.set_thumbnail(url=ctx.message.guild.icon_url)
    await ctx.send(embed=mbed)


@bot.command()
@commands.has_role("dumbass")
async def kick(ctx, user: discord.Member):
    await ctx.send(":boot: Cya, {}. Ya Motherfucker!".format(user.nick))
    await ctx.kick(user)


@bot.command()
async def embed(ctx):
    mbed = discord.Embed(title="test", description="test embed", color=0x00ff00)
    mbed.set_footer(text="this is a footer")
    mbed.set_author(name="Smyhk")
    mbed.add_field(name="this is a field", value="a field value", inline=True)
    await ctx.send(embed=mbed)


# Load the bot token from an environment variable
bot.run(os.environ.get('BOT_TOKEN'))
