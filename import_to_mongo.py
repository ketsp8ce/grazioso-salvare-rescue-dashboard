# NOTE TO USER:
# 1. Run this script to import Pokémon data into MongoDB.
# 2. Make sure you already have 'kanto_pokemon.json' in the project folder.
# 3. If you do not have 'kanto_pokemon.json', first run 'fetch_pokemon.py'.
# 4. This script will insert all Pokémon from the JSON file into the 
#    'kanto_pokemon' collection in the 'pokemon_dashboard' database.

import requests
import json
import time

data = []

for i in range(1, 152):  # 1–151 = Kanto region
    url = f"https://pokeapi.co/api/v2/pokemon/{i}"
    res = requests.get(url)
    
    if res.status_code == 200:
        pokemon = res.json()
        
        # Keep only the fields you need
        simplified = {
            "id": pokemon["id"],
            "name": pokemon["name"],
            "height": pokemon["height"],
            "weight": pokemon["weight"],
            "types": [t["type"]["name"] for t in pokemon["types"]],
            "stats": {s["stat"]["name"]: s["base_stat"] for s in pokemon["stats"]},
        }
        
        data.append(simplified)
        print(f"Fetched {pokemon['name']}")
    else:
        print(f"Failed to fetch Pokémon #{i}")
    
    time.sleep(0.2)  # polite delay to avoid hammering the API

# Save the data to a JSON file
with open("kanto_pokemon.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ Saved kanto_pokemon.json")
