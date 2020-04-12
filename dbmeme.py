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

        if message.content.startswith("!dbdhelp"):
            msg = "Liste des commande disponibles: \n\n" \
                  "!dbdgit - Liens vers le github\n\n" \
                  "!dbdmeme - Balance un meme en provenance de r/deadbydaylight\n" \
                  "    !dbdmeme,[nombre de meme] - balance le nombre de meme donné\n\n" \
                  "!dbdbook - Donne une règle du livre des tueur fait par les survivants à l'égard des survivants\n" \
                  "    !dbdbook,[numéro de la règle] - Donne la règle donnée après la virgule (attention pas d'espace" \
                  " :( )\n" \
                  "    !dbdbook,count - donne les règles disponible\n\n"

            await channel.send(msg)

        if message.content.startswith("!dbdgit"):
            await channel.send("https://github.com/Kwaaac/dbd-memes")

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
            splitedMsg = message.content.split(",")

            if len(splitedMsg) > 1:
                memes = get_random_dbd_meme(int(splitedMsg[1]))
            else:
                memes = get_random_dbd_meme()

            print(memes)
            for meme in memes:
                print(meme)
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
