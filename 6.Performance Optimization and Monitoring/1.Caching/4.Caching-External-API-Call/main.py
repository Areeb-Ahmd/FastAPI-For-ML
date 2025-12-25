import redis
import hashlib
import json
import httpx
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
# Initialize Redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

#Define data model
class PostRequest(BaseModel):
    post_id: int

# Function to generate a unique cache key
def make_cache_key(post_id: int):
    raw = f"external_api:post_{post_id}"
    return hashlib.sha256(raw.encode()).hexdigest()

# Function to fetch data from external API
@app.post("/get-post")
async def get_post(data: PostRequest):
    cache_key = make_cache_key(data.post_id)
    cached_data = redis_client.get(cache_key)
    # Check if data is in cache
    if cached_data:
        print("Served from Redis Cache")
        return json.loads(cached_data)
    
    # If not in cache, fetch from external API
    print("Calling External API...")
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://jsonplaceholder.typicode.com/posts/{data.post_id}")
        if response.status_code != 200:
            return {"error": "Post not found!"}
        
    post_data = response.json()
    redis_client.setex(cache_key, 300, json.dumps(post_data))  # Cache for 5 minutes
    print("Fetched from External API and Redis Cached")
    return post_data
