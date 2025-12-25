import sqlite3
import redis
import json
import hashlib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
redis_client = redis.Redis(host='localhost', port=6379, db=0)

#Method to establish connection to db
def get_db_connection():
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

#Initialize Database with Sample Data
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   age INTEGER
                   )
    ''')
    cursor.execute("INSERT OR IGNORE INTO users (id, name, age) VALUES (1, 'Michael', 45)")
    cursor.execute("INSERT OR IGNORE INTO users (id, name, age) VALUES (2, 'Jim', 35)")
    cursor.execute("INSERT OR IGNORE INTO users (id, name, age) VALUES (3, 'Pam', 27)")
    conn.commit()
    conn.close()
# Call the init_db function to set up the database
init_db()

# Define the input data model
class UserQuery(BaseModel):
    user_id: int

# Method to generate a unique cache key based on input data
def make_cache_key(user_id: int):
    raw =f"user: {user_id}"
    return hashlib.sha256(raw.encode()).hexdigest()

# Define User Retrieval Endpoint with Caching
@app.post('/get-user')
def get_user(query: UserQuery):
    cache_key = make_cache_key(query.user_id)
    cached_data = redis_client.get(cache_key)
    #check if user data is in cache
    if cached_data:
        print("Serving user data from Redis Cache!")
        return json.loads(cached_data)
    
    # Fetch user data from database if not in cache
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (query.user_id,))
    row = cursor.fetchone()
    conn.close()

    #If user not present in db
    if row is None:
        return {"message": "User not found."}
    
    #cache the user data
    result = {'id': row['id'], 'name': row['name'], 'age': row['age']}
    redis_client.set(cache_key, json.dumps(result), ex=3600)  # Cache for 1 hour
    print("Fetched from Database and cached the result.")
    return result