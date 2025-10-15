## Instructions

Follow these steps to run the Pokémon Dashboard locally on your machine.

---

### Prerequisites

Before starting, ensure you have the following installed:

- **Python 3.10+**  
  Download: [https://www.python.org/downloads/](https://www.python.org/downloads/)

- **MongoDB 8.x**  
  Download: [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)  

- **Git** (for cloning the repository)  
  Download: [https://git-scm.com/downloads](https://git-scm.com/downloads)

> Ensure Python and MongoDB executables are added to your system PATH so you can run them from the terminal.

---

### Repository Guidelines

#### Clone the Repository

```bash
git clone <your-repo-url>
cd grazioso-salvare-rescue-dashboard/grazioso-salvare-rescue-dashboard
```

#### Populate the database
From your project root, run:

```bash
python import_to_mongo.py
```
This will read kanto_pokemon.json and load it into MongoDB.


Optional: If the user wants fresh data from the API, you might want to modify the file fetch_pokemon.py, for example to obtain Pokemon from your prefered region instead of Kanto:
```bash
python fetch_pokemon.py
python import_to_mongo.py
```
This fetches from PokeAPI and then imports into MongoDB.

---

### System Environment Setup
- To use the contents of this repository, certain components must be configured on your machine. Follow these steps:
1. Create and activate a Python environment
```bash
python -m venv env
.\env\Scripts\Activate.ps1
```

#### Run MongoDB
- Ensure the mongod.exe executable is included in your system PATH. This is typically located in the bin folder of your MongoDB installation. Once configured, start the MongoDB server in a separate terminal
```bash
mongod
```

#### Start the Flask application
- From your Python environment, execute the project script to launch the Flask server:
```bash
python app.py
```

#### Workflow Overview
A typical development setup will use 3–4 terminals:
  -One for the Python environment
  -One for the Flask server (this can also be in the same terminal as the Python env)
  -One for the MongoDB server

  ![python environment](/screenshots/env)
  ![connect to flask](/screenshots/flask_start)
  ![connect mongoDB](/screenshots/mongod)

---

### **Open your web browser** and navigate to the following routes to test the dashboard functionality:

- [Home Page](http://127.0.0.1:5000/)
- [All Pokémon](http://127.0.0.1:5000/all)
- [Pikachu Details](http://127.0.0.1:5000/pokemon/25)

![Home test](/screenshots/route_home)
![All test](/screenshots/route_all)
![Pikachu Test](/screenshots/route_pikachu)

