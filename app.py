from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['pokemon_dashboard']
collection = db['kanto_pokemon']

# Example: print one document
print(collection.find_one())

# route to call home
@app.route('/')
def home():
    # Example: return the first document in the collection
    first_doc = collection.find_one()
    if first_doc:
        first_doc['_id'] = str(first_doc['_id'])  # Convert ObjectId to string
        return jsonify(first_doc)
    else:
        return jsonify({"message": "No data found"})

# route to return all pokemon
@app.route('/all')
def all_pokemon():
    docs = list(collection.find())
    for doc in docs:
        doc['_id'] = str(doc['_id'])
    return jsonify(docs)

# route to return a single pokemon
@app.route('/pokemon/<int:pokemon_id>')
def get_pokemon(pokemon_id):
    doc = collection.find_one({"id": pokemon_id})
    if doc:
        doc['_id'] = str(doc['_id'])
        return jsonify(doc)
    else:
        return jsonify({"message": "Pokémon not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
