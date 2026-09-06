from fastapi import FastAPI, Path, Query, HTTPException
import json

app = FastAPI()


# help function to laod the data

def load_data():
    with open('players_db.json', 'r') as f:
        data = json.load(f)

        return data

@app.get('/')
def hello():
    return {'message': 'players info API'}


@app.get('/about')
def info():
    return {'message': 'functional api for player data management'}


# uvicorn <filename>:app --reload

# Path parameter

@app.get('/view/{player_id}')
def view_id_info(player_id: str = Path(..., description = 'id of the play', example = '101')):

    """
    gets the info of specific player
    
    """
    data = load_data()

    id = "user_" + str(player_id)

    if id in data:
        return data[id]
    raise HTTPException(status_code = 404, detail = "player not found")


# Query

@app.get('/sort')
def sort_players(sort_by: str = Query(..., description = 'sort on the basis of player name or player level'), order: str = Query('asc', description = "sort in ascending or descending order")):

    valid_fields = ['name', 'level']

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400,
                            details = f"invalid field select from {valid_fields}")

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code = 400,
                            details = f"invalid order. select between asc and desc")

    data = load_data()

    sort_order = True if order == 'desc' else False

    # sorting 
    sorted_data = sorted(data.values(),
                         key = lambda x: x.get(sort_by, 0),
                         reverse= sort_order)

    return sorted_data