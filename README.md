# MITU_AUG_2026

Code from the MITU August 2026 batch, starting with FastAPI.

## Contents

- `1hello_world_fastapi.py` to `5post.py`: FastAPI step by step: routes, a JSON-backed CRUD app (`players_db.json`), path and query parameters, Pydantic models (`4pydantic.ipynb`) and POST
- `ML-Fastapi/`: a trained model served through FastAPI (`app.py`) with a small frontend (`frontend.py`)
- `logistic_reg.ipynb`: logistic regression on `Social_Network_Ads.csv`
- `NLP-GEN-AI/`: unstructured text data and TF-IDF (SMS spam collection)

## Running the API examples

    pip install fastapi "uvicorn[standard]"
    uvicorn 3path_query:app --reload

Use the file name (without `.py`) and the app object name. FastAPI serves interactive docs at `/docs`.
