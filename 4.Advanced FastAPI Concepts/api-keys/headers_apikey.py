from fastapi import FastAPI, Depends, HTTPException, Header

app = FastAPI()

#Hardcode an API key for demonstration purposes
API_KEY = "my-secret-key"

#Function to get and validate API key
def get_api_key(api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate API key")
    return api_key

#Define a protected endpoint
@app.get('/get-data')
def get_data(api_key: str = Depends(get_api_key)):
    return {"Output": "Access Granted!"}