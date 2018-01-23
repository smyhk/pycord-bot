import os
import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Connected to endpoint')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)
    print('Hello smyhk. How about a nice game of chess?')


@client.event
async def on_message(message):

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")

    if message.content.upper().startswith("!PING"):
        msg = "{0.author.mention} Pong!".format(message)
        await client.send_message(message.channel, msg)

    if message.content.upper().startswith("!SAY"):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % " ".join(args[1:]))


# Load the bot token from an environment variable
client.run(os.environ.get('BOT_TOKEN'))
