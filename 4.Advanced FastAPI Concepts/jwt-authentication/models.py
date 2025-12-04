from pydantic import BaseModel

#Define a user class
class User(BaseModel):
    username: str
    password: str

#Define a user in DB class
class UserInDB(User):
    hashed_password: str
