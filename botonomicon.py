# pycord.py bot rewrite
# TODO: refactor into classes

import os
# import logging
import datetime
from flask import Flask, request
# import requests
import discord
from discord.ext import commands


app = Flask(__name__)
port = int(os.environ.get("PORT"))


@app.route("/")
def index():
    bot = commands.Bot(command_prefix="!")

    @bot.event
    async def on_ready():
        print('Connected to Discord endpoint')
        print('Username: ' + bot.user.name)
        print('ID: ' + bot.user.id)
        print('Hello smyhk. How about a nice game of chess?')
        await bot.change_presence(game=discord.Game(name="Ass Blasters 7", type=3))

    @bot.event
    async def on_member_join(member):
        print(str(member.mention) + " joined at: " + str(member.joined_at))
        msg = "Welcome to the server " + str(member.mention) + "! Type !help for more information."
        await bot.send_message(bot.get_channel("373673083854389249"), msg)

    @bot.event
    async def on_member_remove(member):
        print(str(member.mention) + " left at: " + str(datetime.datetime.now()))
        # await bot.send_message(bot.get_channel("373673083854389249"), msg)

    @bot.command(pass_context=True, description='Is bot listening?')
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


app.run(port=port, host="0.0.0.0")
