from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Include CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'https://my-frontend.com', 'http://localhost:3000'
    ],
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=['*']
)

# Define endpoints