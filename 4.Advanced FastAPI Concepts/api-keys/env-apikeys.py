from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic_settings import BaseSettings

#Define class to read settings from .env file
class Settings(BaseSettings):
    api_key: str

    class Config:
        env_file = ".env"

#Instance of Settings
settings = Settings()

app = FastAPI()

#Function to get and validate API key
def get_api_key(api_key: str = Header(...)):
    if api_key != settings.api_key:
        raise HTTPException(status_code=403, detail="Could not validate API key")
    return api_key

#Define a protected endpoint
@app.get('/get-data')
def get_data(api_key: str = Depends(get_api_key)):
    return {"Output": "Access Granted!"}