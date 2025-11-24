import joblib
import numpy as np
from typing import List

saved_model = joblib.load('model.joblib')
print('Loaded the Model.')

# Function to make a prediction
def make_prediction(data: dict) -> float:
    features = np.array([
        [
            data['longitude'],
            data['latitude'],
            data['housing_median_age'],
            data['total_rooms'],
            data['total_bedrooms'],
            data['population'],
            data['households'],
            data['median_income']
        ]
    ])
    return saved_model.predict(features)[0]

# Function to make batch predictions
def make_batch_prediction(data: List[dict]) -> np.array:
    batch_features = np.array([
        [
            item['longitude'],
            item['latitude'],
            item['housing_median_age'],
            item['total_rooms'],
            item['total_bedrooms'],
            item['population'],
            item['households'],
            item['median_income']
        ] 
        for item in data
    ])
    return saved_model.predict(batch_features)

