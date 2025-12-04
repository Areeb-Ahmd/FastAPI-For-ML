from fastapi import FastAPI, Depends, Form, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

#Initialize FastAPI app
app = FastAPI()
#Initialize OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#Define Token endpoint
@app.post('/token')
def login(username: str = Form(...), password: str = Form(...)):
    if username == 'John' and password == 'pass123':
        return {'access_token': 'valid_token', 'token_type': 'bearer'}
    raise HTTPException(status_code=400, detail='Invalid Credentials')

#Define Function to decode token
def decode_token(token: str):
    if token == 'valid_token':
        return {'name': 'John'}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail='Invalid Authentication Credentials',
    )

#Define dependency to get current user
def get_current_user(token: str = Depends(oauth2_scheme)):
    return decode_token(token)


#Define profile endpoint
@app.get('/profile')
def get_profile(user = Depends(get_current_user)):
    return {'username': user['name']}