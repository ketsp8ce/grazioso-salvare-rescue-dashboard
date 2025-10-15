from flask import Flask, jsonify
from PokemonCRUD import PokemonCRUD  # make sure the class name matches your file

app = Flask(__name__)

# Instantiate your CRUD class
crud = PokemonCRUD()

# route to call home
@app.route('/')
def home():
    # Get the first Pokémon document
    docs = crud.read({})
    if docs:
        first_doc = docs[0]
        first_doc['_id'] = str(first_doc['_id'])  # Convert ObjectId to string
        return jsonify(first_doc)
    else:
        return jsonify({"message": "No data found"})

# route to return all Pokémon
@app.route('/all')
def all_pokemon():
    docs = crud.read({})
    for doc in docs:
        doc['_id'] = str(doc['_id'])
    return jsonify(docs)

# route to return a single Pokémon by ID
@app.route('/pokemon/<int:pokemon_id>')
def get_pokemon(pokemon_id):
    docs = crud.read({"id": pokemon_id})
    if docs:
        doc = docs[0]
        doc['_id'] = str(doc['_id'])
        return jsonify(doc)
    else:
        return jsonify({"message": "Pokémon not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
