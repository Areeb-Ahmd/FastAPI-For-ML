import time
from fastapi import FastAPI

app = FastAPI()

# A sample function to be profiled
def computation(n: int):
    res = 0
    for i in range(n):
        res += (i * 2)
    time.sleep(1)
    return res

# Profile the function
@profile
def process_data(x: int):
    return computation(x)

#define endpoints
@app.get("/profiling")
def profiling(a: int):
    return {"result": process_data(a)}