from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__():

        # Initialize Connection

        self.client = MongoClient(
            f'mongodb://{username}:{password}@{host}:{port}/{db}?authSource=admin',
            connectTimeoutMS=5000,
            serverSelectionTimeoutMS=5000
        )
        
        
        try:
            self.client.admin.command('ping')
            self.database=self.client[db]
            self.collection=self.database[col]
            print("connected to MongoDB")
        except ConnectionFailure as e:
            raise Exception(f"Connection failed: {str(e)}")
        except OperationFailure as e:
            raise Exception(f"Authenticagtion failed: {str(e)}")

# Create method (C in CRUD)
#Inserts a document into the 'animals' collection, returns true on success
    def create(self, data):
        if data is not None:
            try:
                result = self.animals.insert_one(data) #data should be dictionary
                print(f"debug: inserted document with id: {result.inserted_id}")
                return result.acknowledged
            except Exception as e:
                print(f"Error: insert failed - {str(e)}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Read method (R in CRUD)
#Queries documents and returns a list of content or an empty list if fails
    def read(self, query):
        try:
            cursor=self.animals.find(query)
            return list(cursor) #convert cursor to list of documents
        except Exception as e:
            print(f"Query failed: {e}") #error message
            return[] #return empty list

#Update method (U in CRUD)
#if document being checked matches query, updates that document with a new inputs 
    def update(self, query, update_data):
        if(query is None or update_data is None):
            raise Exception("parameters cannot be empty")
        
        try:
            result = self.animals.update_many(query, {"$set":update_data})
            return result.new_count
        except Exception as e:
            print(f"Update failed: {e}")
            return 0


#Delete method (D in CRUD)
#deletes document if it matches the query

    def delete(self, query):
        if query is None:
            raise Exception("query cannot be empty")
        try:
            result = self.animals.delete_many(query)
            return result.count_deleted
        except Exception as e:
            print(f"Delete failed: {e}")
            return 0
