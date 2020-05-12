import json


def get_champion_name(champion_id):
    champ_json = json.load(open('champion.json', encoding='utf-8'))
    # each json is specified every time because the champion.json file
    # does not store the champions in an array and so forth
    for champ in champ_json['data']:
        if int(champ_json['data'][champ]['key']) == int(champion_id):
            return champ_json['data'][champ]['id']

    return None
