from fastapi import FastAPI, Depends

app = FastAPI()

# Config management class
class Settings:
    def __init__(self):
        self.api_key = 'my_secret'
        self.debug = True

# Define a dependency function for config
def get_settings():
    return Settings()        

#Endpoint that uses the config dependency
@app.get('/config')
def get_config(settings: Settings = Depends(get_settings)):
    return {'api_key': settings.api_key, 'debug': settings.debug}