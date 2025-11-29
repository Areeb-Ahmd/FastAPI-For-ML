from passlib.context import CryptContext

#Instance of CryptContext for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Create Dummy Database
fake_users_db = {
    'areeb': {
        'username': 'areeb',
        'hashed_password': pwd_context.hash('areeb123')
    }
}

#Util Functions

#Function to return user data from dummy DB
def get_user(username: str):
    user = fake_users_db.get(username)
    return user

#Function to verify password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
