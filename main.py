import operator

import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'

response = requests.get(url)
file = response.json()


def compare(heros):
    dict_ = {}
    for every_hero in heros:
        for dicts_ in file:
            if dicts_['name'] == every_hero:
                dict_[every_hero] = dicts_['powerstats']['intelligence']
                max_intelligence = max(dict_.items(), key=operator.itemgetter(1))
    return (max_intelligence)


print(compare(['Hulk', 'Captain America', 'Thanos']))
