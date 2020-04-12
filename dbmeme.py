import discord

from jsonSentencesHandler import *
from reddit import *

client = discord.Client()


@client.event
async def on_message(message):
    # the bot don't reply to itself
    if message.author == client.user:
        return

    channel = message.channel

    if message.content.startswith("!dbdrule"):
        await channel.send(get_random_rule())

    elif message.content.startswith("!dbdmeme"):
        meme = get_random_dbd_meme()
        await channel.send(meme[0] + "\n" + meme[1])

    elif message.content.find("pigeon") != -1 or message.content.find("pigeons") != -1:
        msg = get_random_pigeon() + client.get_user(166557610948952065).mention
        await channel.send(msg)


# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map',
# 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric',
# 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
# 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
# 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(config.TOKEN)
