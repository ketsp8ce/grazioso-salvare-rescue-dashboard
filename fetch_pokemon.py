# NOTE TO USER:
# 1. Run this script only if you do NOT already have 'kanto_pokemon.json'.
# 2. This will fetch all Kanto Pokémon data from the PokéAPI.
# 3. If you already have 'kanto_pokemon.json', you can skip this script.

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
