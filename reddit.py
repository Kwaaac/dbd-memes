from random import randint

import praw

import config


def reddit_connection():
    return praw.Reddit(client_id=config.CLIENT_ID,
                       client_secret=config.CLIENT_SECRET,
                       username=config.USERNAME,
                       password=config.PASSWORD,
                       user_agent=config.USER_AGENT)


def get_random_dbd_meme(number=1):
    limit = 500
    reddit = reddit_connection()

    dbd_memes = reddit.subreddit('deadbydaylight').search('meme OR memes', limit=500)

    randomMeme = randint(0, limit // number)
    memeTaken = []
    result = []
    for i, meme in enumerate(dbd_memes):
        if i == randomMeme and i not in memeTaken and vars(meme).get('post_hint') == 'image':

            memeTaken.append(i)
            result.append((meme.title, meme.url))

            number -= 1
            if number == 0:
                break

            randomMeme = randint(i, limit // number)

        if i > randomMeme:
            randomMeme = randint(i, limit // number)

    if len(result) > 0:
        return result

    return [("Aie je n'ai rien trouvé", ":(")]
