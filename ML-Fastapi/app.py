# fastapi for iris flower classification

import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated
import pandas as pd
import numpy as np
from fastapi.responses import JSONResponse

# load the model and scaler files

model = joblib.load("ML-Fastapi/log-model.pkl")

scaler = joblib.load("ML-Fastapi/scaler-model.pkl")

app = FastAPI()


# build the validation for input fields

class UserInput(BaseModel):

    sepal_length: Annotated[float, Field(..., gt = 0, description = "sepal_length of the flower")]

    sepal_width: Annotated[float, Field(..., gt = 0, description = "sepal_width of the flower")]

    petal_length: Annotated[float, Field(..., gt = 0, description = "petal_length of the flower")]

    petal_width: Annotated[float, Field(..., gt = 0, description = "petal_width of the flower")]


@app.get('/')
def home():
    return {'message': "Iris Flower Species Predictor"}


# machine readable - health check (for health check -> necessay for deployment on services like AWS)

MODEL_VERSION = '1.0.0'  # ideally will be from mlflow/kubeflow

@app.get('/health')
def health_check():
    return {
        'status': 'ok',
        'model_loaded': model is not None,
        'version': MODEL_VERSION
    }


@app.post('/predict')
def predict_species(data: UserInput):

    df = pd.DataFrame({
        'sepal_length': [data.sepal_length],
        'sepal_width': [data.sepal_width],
        'petal_length': [data.petal_length],
        'petal_width': [data.petal_width]
    })

    scaled_df = scaler.transform(df)

    pred = model.predict(scaled_df)

    return {'predicted_species': str(pred[0])}