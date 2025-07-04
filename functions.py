# functions.py

import requests
from box import Box

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_data(name):
    url = f"{base_url}pokemon/{name.lower()}"
    res = requests.get(url)
    return Box(res.json()) if res.status_code == 200 else -1

def pokemon_moves(data):
    if data == -1:
        print("Error Fetching Data")
        return []
    return [i.move.name for i in data.moves]

def filtering_moves(data):
    if data == -1:
        print("Error Fetching Data")
        return {}

    pmoves, npmoves = [], []
    for i in data:
        url = f"{base_url}move/{i}"
        res = requests.get(url)
        if res.status_code == 200:
            move_data = Box(res.json())
            if move_data.power:
                pmoves.append(i)
            else:
                npmoves.append(i)
    return {"pmoves": pmoves, "npmoves": npmoves}

def get_evolution_data(data):
    species_url = data.species.url
    res = requests.get(species_url)
    if res.status_code != 200:
        print("Error fetching species data")
        return None

    species_data = Box(res.json())
    color = species_data.color.name
    evo_url = species_data.evolution_chain.url
    evo_res = requests.get(evo_url)
    if evo_res.status_code == 200:
        evo_data = Box(evo_res.json())
        return [evo_data.chain, color]
    else:
        print("Error fetching evolution data")
        return None

def extract_evolution_chain(chain_node):
    evolution_info = []
    current = chain_node["species"]["name"]

    for evolution in chain_node["evolves_to"]:
        evolved = evolution["species"]["name"]

        for detail in evolution["evolution_details"]:
            trigger = detail["trigger"]["name"]
            item = detail["item"]["name"] if detail["item"] else None
            evo_str = f"{current} → {evolved} | Trigger: {trigger}"
            if item:
                evo_str += f", Item: {item}"
            evolution_info.append(evo_str)

        evolution_info += extract_evolution_chain(evolution)

    return evolution_info

def strong_annd_weaktypes(data):
    url = data.types[0].type.url
    res = requests.get(url)
    if res.status_code != 200:
        print("Error fetching type data")
        return {}

    type_data = Box(res.json())
    strong_against, weak_against = [], []

    for key in type_data.damage_relations:
        if "to" in key:
            d = type_data.damage_relations[key]
            strong_against += [x.name for x in d]
        if "from" in key:
            d = type_data.damage_relations[key]
            weak_against += [x.name for x in d]

    return {"strong_against": strong_against, "weak_against": weak_against}

def color_and_description(data):
    res = requests.get(data.species.url)
    if res.status_code != 200:
        print("Failed Gathering Species Data")
        return ["Unknown", "No description available"]

    species_data = Box(res.json())
    color = species_data.color.name
    description = species_data.flavor_text_entries[6].flavor_text.replace('\n', ' ').replace('\f', ' ')
    return [color, description]
