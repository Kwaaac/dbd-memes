import discord
import praw
from jsonSentencesHandler import get_random_rule

# Bot's auth token
TOKEN = "Njk4NjUzMjcwMjYzOTg4MjI1.XpJEOA.A5DiCNrVCCPvh8tFlHmm2f8iQq4"

client = discord.Client()


@client.event
async def on_message(message):
    # the bot don't reply to itself
    if message.author == client.user:
        return

    channel = message.channel

    if message.content.statswith("!dbdrule"):
        await channel.send(get_random_rule())

    elif message.content.find("pigeon") != -1 or message.content.find("pigeons") != -1:
        msg = "Pigeon vous dites ? Encore un tour de " + client.get_user(166557610948952065).mention
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


client.run(TOKEN)
