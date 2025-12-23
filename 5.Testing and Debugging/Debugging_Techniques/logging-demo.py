import logging
from fastapi import FastAPI

app = FastAPI()

#Configure Logging
logging.basicConfig(
    level = logging.INFO,
    format = "[%(asctime)s] ((line %(lineno)d) - %(levelname)s - %(message)s)",
    datefmt = "%m-%d-%Y %H:%M:%S"
)

#Define Endpoint
@app.get("/debug")
def debug_route():
    logging.info("Debug route accessed")
    return {"message": "Check Logs for Debugging Info!"}
