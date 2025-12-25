import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port = 6379, db = 0)

#Test the connection
try:
    if r.ping():
        print("Connected to Redis server successfully!")
except redis.ConnectionError:
    print("Failed to connect to Redis server.")

# Set a sample key-value pair
r.set('framework', 'FastAPI')

# Retrieve the value for the sample key
value = r.get('framework')

# Print the retrieved value
print(f"The stored value for 'framework' is: {value.decode()}")