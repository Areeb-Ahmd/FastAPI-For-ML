import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from model import model

app = FastAPI()

#Define Data Model
class IrisFlower(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

#Define Prediction Endpoint
@app.post("/predict")
def predict(data: IrisFlower):
    features = np.array([
        [
            data.SepalLengthCm, 
            data.SepalWidthCm, 
            data.PetalLengthCm, 
            data.PetalWidthCm
        ]
    ])
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}