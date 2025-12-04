from fastapi import FastAPI
from starlette.middleware.gzip import GZipMiddleware

app = FastAPI()

# Include GZip middleware
app.add_middleware(
    GZipMiddleware, 
    minimum_size=1000
    )

# Define endpoints
