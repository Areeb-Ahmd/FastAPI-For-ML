from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

Instrumentator().instrument(app).expose(app)

#Define a sample endpoint
@app.get("/home")
def home():
    return {"message": "Welcome to the FastAPI application with Prometheus monitoring!"}

