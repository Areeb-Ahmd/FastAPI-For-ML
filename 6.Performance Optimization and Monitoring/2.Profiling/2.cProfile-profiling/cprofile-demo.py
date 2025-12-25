import os
import time
import cProfile
import datetime
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

#Create a folder called profiles to store the profiling results
PROFILES_DIR = "profiles"
os.makedirs(PROFILES_DIR, exist_ok=True)

app = FastAPI()

#middleware to profile each request
@app.middleware("http")
async def create_profile(request: Request, call_next):
    timestamp = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S_%f")
    path = request.url.path.strip("/").replace("/", "_") or "root" #if path is empty, use "root"
    profile_name = os.path.join(PROFILES_DIR, f"{path}_{timestamp}.prof") #naming convension of profile files

    profiler = cProfile.Profile()
    profiler.enable()

    response = await call_next(request)

    profiler.disable()
    profiler.dump_stats(profile_name)

    print(f"Profile saved: {profile_name}")

    return response

#Define endpoints
@app.get("/")
def home():
    return {"message": "Welcome to cProfile Demo!"}

@app.get("/compute")
async def compute():
    time.sleep(1)  # Simulate a time-consuming computation
    result = sum(i * 2 for i in range(10000))
    return JSONResponse({"result": result})
