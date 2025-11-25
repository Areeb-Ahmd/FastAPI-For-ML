import time
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

# Define a custom middleware
class TimerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        duration = time.time() - start_time
        print(f'Request: {request.url.path} processed in {duration:.5f} seconds')
        return response

# Include the custom middleware
app.add_middleware(TimerMiddleware)

# Define endpoints
@app.get('/welcome')
async def welcome():
    for _ in range(1000000):
        pass # Simulate a time-consuming operation
    return {'message': 'Welcome to FastAPI using custom middleware!'}