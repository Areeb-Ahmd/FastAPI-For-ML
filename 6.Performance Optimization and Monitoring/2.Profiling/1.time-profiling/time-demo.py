import time
import logging
from fastapi import FastAPI, Request

#Define login configurations
logging.basicConfig(
    level=logging.INFO,
    format = "[%(asctime)s] (line %(lineno)d) - %(levelname)s - %(message)s",
    datefmt="%m-%d-%Y %H:%M:%S" 
)
logger = logging.getLogger('profiler')

app = FastAPI()

#Define middleware
@app.middleware('http')
async def add_timing(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    time_taken = time.time() - start_time
    logger.info(f"Request to {request.url.path} took {time_taken:.3f} seconds")
    return response

#Define endpoints
@app.get('/')
def home():
    return {'message': 'Profiling using time demo.'}

@app.get('/slow')
async def slow_endpoint():
    time.sleep(2) # Simulate a slow operation
    return {'message': 'Slow endpoint executed.'} 

@app.get('/fast')
async def fast_endpoint():
    return {'message': 'Fast endpoint executed.'} 


