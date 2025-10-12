from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Replace with your local MongoDB connection string if needed
client = MongoClient("mongodb://localhost:27017/")
db = client['rescue_dashboard']  # Use your database name
collection = db['animals']       # Use your collection name

@app.route('/')
def home():
    # Example: return the first document in the collection
    first_doc = collection.find_one()
    if first_doc:
        first_doc['_id'] = str(first_doc['_id'])  # Convert ObjectId to string
        return jsonify(first_doc)
    else:
        return jsonify({"message": "No data found"})

if __name__ == '__main__':
    app.run(debug=True)
