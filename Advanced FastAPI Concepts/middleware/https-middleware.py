from fastapi import FastAPI
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware

app = FastAPI()

# Include GZip middleware
app.add_middleware(HTTPSRedirectMiddleware)

# Define endpoints