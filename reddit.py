import praw

import config


def reddit_connection():
    return praw.Reddit(client_id=config.CLIENT_ID,
                       client_secret=config.CLIENT_SECRET,
                       username=config.USERNAME,
                       password=config.PASSWORD,
                       user_agent=config.USER_AGENT)


def get_random_dbd_meme(number=1):
    if number == 0:
        raise Exception("Hey prout")

    reddit = reddit_connection()

    dbd_memes = reddit.subreddit('deadbydaylight').random_rising(limit=number, params={"search": "meme"})

    result = []
    for meme in dbd_memes:
        result.append((meme.title, meme.url))

    if len(result) > 0:
        return result

    return [("Aie je n'ai rien trouvé", ":(")]


def get_abrupt_chaos_vid(number=1):
    if number == 0:
        raise Exception("Hey prout")

    reddit = reddit_connection()

    abrupt_chaos = reddit.subreddit("AbruptChaos")

    result = []
    while len(result) != number:
        sub = abrupt_chaos.random()
        try:
            if sub.secure_media is not None:
                result.append((sub.title, sub.secure_media['reddit_video']['fallback_url']))

            else:
                result.append((sub.title, sub.crosspost_parent_list[0]['secure_media']['reddit_video']['fallback_url']))
        except Exception as e:
            continue
    return result


def get_cursed_image(number=1):
    if number == 0:
        raise Exception("Hey prout")

    reddit = reddit_connection()

    abrupt_chaos = reddit.subreddit("cursedimages")

    result = []
    while len(result) != number:
        sub = abrupt_chaos.random()
        try:
            result.append((sub.title, sub.url))
        except Exception as e:
            continue
    return result
