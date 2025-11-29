from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from auth import create_access_token, verify_token
from utils import get_user, verify_password

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#Define token endpoint
@app.post('/token')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = get_user(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Invalid Username")
    if not verify_password(form_data.password, user_dict['hashed_password']):
        raise HTTPException(status_code=400, detail="Invalid Password")
    
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}

#Define get user endpoint
@app.get('/users')
def read_users(token: str = Depends(oauth2_scheme)):
    username = verify_token(token)
    return {"username": username}