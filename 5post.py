from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import Annotated, List

from fastapi.responses import JSONResponse

import json


app = FastAPI()



# helper function to load and save data

def load_data():
    with open('players_db.json', 'r') as f:
        data = json.load(f)

    return data

def save_data(data):
    with open('players_db.json', 'w') as f:
        json.dump(data, f, indent= 4)  # dumping into f


# create the pydantic schema

class Player(BaseModel):

    id: Annotated[str, Field(..., description = 'id of player', example = 'user_101')]

    name: Annotated[str, Field(..., description = 'name of player', max_length = 15)]

    region: Annotated[str, Field(...)]

    level:Annotated[int, Field(..., description = 'level of player', gt = 0, lt = 100)]

    dex:Annotated[List[str], Field(..., description = 'dex of player')]



@app.get('/')
def hello():
    return f"Hello to CricMania"

@app.get('/about')
def info():
    return {'message': 'functional  api to manage player data'}

# post endpoint for creating new user

@app.post('/create')
def create_user(player_info: Player):

    # load the data
    data = load_data()

    if player_info.id in data:
        raise HTTPException(status_code = 400, detail = 'trainer id already exists')

    data[player_info.id] = player_info.model_dump(exclude = ['id'])


    # save the above dict as the json file

    save_data(data)

    return JSONResponse(status_code = 201, content = {'message': 'player created successfully'})