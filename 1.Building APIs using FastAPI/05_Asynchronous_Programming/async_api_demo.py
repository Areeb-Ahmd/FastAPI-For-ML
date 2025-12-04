import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/wait")
async def wait():
    await asyncio.sleep(3) #Non-blocking sleep for 3 seconds
    return {"message": "Finsihed waiting for 3 seconds!"}
