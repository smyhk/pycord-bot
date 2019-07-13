import os
import discord

client = discord.Client()


@client.event
async def on_ready():
    print('Connected to endpoint')
    print('Logged in as {0.user}'.format(client))
    print('Hello smyhk. How about a nice game of chess?')


@client.event
async def on_message(message):

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    elif message.content == "cookie":
        await message.channel.send(":cookie:")
    elif message.content.upper().startswith("!PING"):
        msg = "{0.author.mention} Pong!".format(message)
        await message.channel.send(msg)
    elif message.content.upper().startswith("!SAY"):
        # only user with this id can execute the command
        if message.author.id == 351094569309306891:
            args = message.content.split(" ")
            msg = " ".join(args[1:]).format(message)
            await message.channel.send(msg)
        else:
            await message.channel.send("Ah ah ah, you didn't say the magic word!")
    elif message.content.upper().startswith("!AMIADMIN"):
        # user users with this role id can execute the command
        if 405241489292263424 in [role.id for role in message.author.roles]:
            await message.channel.send("You are an admin")
        else:
            await message.channel.send("You are not an admin")


# Load the bot token from an environment variable
client.run(os.environ.get('BOT_TOKEN'))
