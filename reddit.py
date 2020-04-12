from random import randint

import praw

import config


def reddit_connection():
    return praw.Reddit(client_id=config.CLIENT_ID,
                       client_secret=config.CLIENT_SECRET,
                       username=config.USERNAME,
                       password=config.PASSWORD,
                       user_agent=config.USER_AGENT)


def get_random_dbd_meme():
    reddit = reddit_connection()

    dbd_memes = reddit.subreddit('deadbydaylight').search('meme OR memes')

    randomMeme = randint(0, 99)

    for i, meme in enumerate(dbd_memes):
        if i == randomMeme and vars(meme).get('post_hint') == 'image':
            return meme.title, meme.url

        else:
            randomMeme = randint(i, 99)

    return "Aie, je n'ai rien trouvé, désolé :/"
