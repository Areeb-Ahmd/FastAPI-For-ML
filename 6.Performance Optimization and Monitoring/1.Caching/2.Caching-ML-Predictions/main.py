import redis
import json
import hashlib
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, db=0)

#load your pre-trained ML model
model = joblib.load('model.joblib')

# Define the input data model
class IrisFlower(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

    # Method to convert input data to a list
    def to_list(self):
        return [
            self.SepalLengthCm,
            self.SepalWidthCm,
            self.PetalLengthCm,
            self.PetalWidthCm
        ]
    # Method to generate a unique cache key based on input data
    def cache_key(self):
        raw_data = json.dumps(self.model_dump(), sort_keys=True)
        return f"iris_prediction:{hashlib.sha256(raw_data.encode()).hexdigest()}"
    
#Define Prediction Endpoint with Caching
@app.post("/predict")
async def predict(data: IrisFlower):
    key = data.cache_key()
    
    # Check if prediction is in cache
    cached_result = redis_client.get(key)
    if cached_result:
        print("Serving prediction from Cache!")
        return json.loads(cached_result) 
    # Make prediction if not in cache
    prediction = model.predict([data.to_list()])[0]
    result = {"prediction": int(prediction)}
    redis_client.set(key, json.dumps(result), ex=3600)  # Cache for 1 hour
    return result



