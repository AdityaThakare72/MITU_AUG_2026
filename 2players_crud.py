from fastapi import FastAPI
import json 


app = FastAPI()

# helper function to load the data

def load_data():
    with open('players_db.json', 'r') as f:
        data = json.load(f)

        return data

@app.get('/')
def hello():
    return {'message': 'CricMania Players info API'}

@app.get('/about')
def info():
    return {'message': 'functional api to manage the player info'}


# endpoint to view all player info

@app.get('/view')
def view():
    data = load_data()

    return data

# endpoint to see specific user info
# {} -> path variable

@app.get('/view/{player_id}')
def view_id_info(player_id: str):
    data = load_data()
    id = 'user_' + str(player_id)

    return data.get(id)