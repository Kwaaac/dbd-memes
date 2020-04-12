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

    try:
        if message.content.startswith("!dbdbook"):
            splitedMsg = message.content.split(",")

            if len(splitedMsg) > 1:
                if splitedMsg[1] == "count":
                    msg = "Voici les règles actuellement disponible au sein du livre:\n"
                    for i, rule in enumerate(get_nbr_rules()):
                        if i != len(get_nbr_rules()) - 1:
                            msg += rule + ", "
                        else:
                            msg += rule + "."

                    await channel.send(msg)
                    return

                rule = (splitedMsg[1], get_rule(splitedMsg[1]))

            else:
                rule = choice(list(get_random_rule()))

            await channel.send(
                "**Règle numéro " + rule[0] + " du livre de règle des tueurs à l'égard des survivants:** \n" +
                "*" + rule[1] + "*")

        elif message.content.startswith("!dbdmeme"):
            meme = get_random_dbd_meme()
            await channel.send(meme[0] + "\n" + meme[1])

        elif message.content.find("pigeon") != -1 or message.content.find("pigeons") != -1:
            msg = get_random_pigeon() + client.get_user(166557610948952065).mention
            await channel.send(msg)

    except Exception as e:
        print("aie y'a eu une bille: \n", e)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(config.TOKEN)
