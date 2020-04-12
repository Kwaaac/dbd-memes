import json
from random import choice


def get_json(part=None, rule=None):
    with open("sentences.json", "r", encoding='utf-8') as jsonFile:
        if part is not None:
            if rule is not None:
                return json.loads(jsonFile.read())[part][rule]

            return json.loads(jsonFile.read())[part]
        return json.loads(jsonFile.read())


def get_random_rule():
    return get_json('book').items()


def get_rule(rule):
    return get_json('book', rule)


def get_nbr_rules():
    return get_json('book').keys()


def get_random_pigeon():
    return choice(get_json('pigeon'))


def test():
    for _ in range(5):
        print(get_random_rule())


if __name__ == '__main__':
    test()
