from fastapi import FastAPI
from schemas import InputSchema, OutputSchema
from predict import make_prediction, make_batch_prediction
from typing import List

app = FastAPI()

# Define a root endpoint
@app.get('/')
def index():
    return {'message': 'Welcome to the ML Model Prediction API!'}

# Define a prediction endpoint
@app.post('/predict', response_model=OutputSchema)
def predict(user_input: InputSchema):
    prediction = make_prediction(user_input.model_dump())
    return OutputSchema(predicted_price = round(prediction, 2))

# Define a batch prediction endpoint
@app.post('/batch_prediction', response_model=List[OutputSchema])
def batch_predict(user_inputs: List[InputSchema]):
    predictions = make_batch_prediction([input.model_dump() for input in user_inputs])
    return [OutputSchema(predicted_price = round(pred, 2)) for pred in predictions]