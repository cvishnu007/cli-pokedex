# main.py

from box import Box
import requests
from functions import *
import time
import sys

def slow_print(text, delay=0.01):
    for char in text:
        print(char, end='')
        sys.stdout.flush()
        time.sleep(delay)
    print()

print("==================================")
print("     BASIC CLI POKEDEX      ")
print("==================================\n")

name = input("Enter the name of the Pokemon: ").strip().lower()
pokemon_data = get_pokemon_data(name)

if pokemon_data == -1:
    slow_print("\n[!] Spelling Error or Pokemon not found.")
    exit()

slow_print(f"\nName       : {pokemon_data.name.title()}")
slow_print(f"Type       : {pokemon_data.types[0].type.name.title()}")

color, description = color_and_description(pokemon_data)
slow_print(f"Color      : {color.title()}")
slow_print(f"Description: {description}\n")

slow_print(f"Height     : {pokemon_data.height}")
slow_print(f"Weight     : {pokemon_data.weight}\n")

slow_print("Base Stats:")
stats = {i.stat.name: i.base_stat for i in pokemon_data.stats}
for stat, value in stats.items():
    slow_print(f"  {stat.title():<15}: {value}")

slow_print("\nType Effectiveness:")
type_data = strong_annd_weaktypes(pokemon_data)
for relation, types in type_data.items():
    slow_print(f"  {relation.replace('_', ' ').title()}: {', '.join(types).title() if types else 'None'}")

slow_print("\nEvolution Chain:")
evolution_chain = extract_evolution_chain(get_evolution_data(pokemon_data)[0])
if evolution_chain:
    for evo in evolution_chain:
        slow_print(f"  {evo}")
else:
    slow_print("  No further evolutions")

slow_print("\n======================")
slow_print("     END OF DATA     ")
slow_print("======================")