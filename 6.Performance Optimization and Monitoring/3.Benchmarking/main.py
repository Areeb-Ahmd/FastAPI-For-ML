from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#define a Pydantic model for input validation
class InputData(BaseModel):
    feature1: float
    feature2: float

#Define endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Locust Demo!"}

@app.post("/predict")
def predict(data: InputData):
    # Dummy prediction logic
    prediction = data.feature1 + data.feature2
    return {"Result": prediction}