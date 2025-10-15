from pymongo import MongoClient

class PokemonCRUD:
    """Minimal CRUD for Kanto Pokémon in MongoDB"""

    def __init__(self, uri="mongodb://localhost:27017/", db_name="pokemon_dashboard", col_name="kanto_pokemon"):
        self.client = MongoClient(uri)
        self.collection = self.client[db_name][col_name]

    def create(self, data):
        if data:
            return self.collection.insert_one(data).acknowledged
        return False

    def read(self, query=None): 
        query = query or {}
        return list(self.collection.find(query))

    def update(self, query, update_data):
        if query and update_data:
            return self.collection.update_many(query, {"$set": update_data}).modified_count
        return 0

    def delete(self, query):
        if query:
            return self.collection.delete_many(query).deleted_count
        return 0
