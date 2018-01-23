import os
import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('Hello smyhk. How about a nice game of chess?')


@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:")

    if message.content.upper().startswith("!PING"):
        user_id = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % user_id)

    if message.content.upper().startswith("!SAY"):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % " ".join(args[1:]))


client.run(os.environ.get('BOT_TOKEN'))
