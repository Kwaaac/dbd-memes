import json
from random import choice


def get_json(part=None):
    with open("sentences.json", "r", encoding='utf-8') as jsonFile:
        if part is not None:
            return json.loads(jsonFile.read())[part]
        return json.loads(jsonFile.read())


def get_random_rule():
    return choice(get_json('book'))


def test():
    for _ in range(5):
        print(get_random_rule())


if __name__ == '__main__':
    test()
