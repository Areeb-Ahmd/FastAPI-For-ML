from fastapi import FastAPI, Depends

app = FastAPI()

#Define a dependency function
def get_db():
    db = {'connection': 'Mock Database Connection'}
    try:
        yield db
    finally:
        db.close()

# Endpoint that uses the dependency
@app.get("/home")
def home(db = Depends(get_db)):
    return {'db_status': db['connection'] }