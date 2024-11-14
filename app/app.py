from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "localhost")
cache = redis.Redis(host=redis_host, port=6379, db=0)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f"Hello, World! You've visited this page {count} times."

if __name__ == "__main__":
    app.run(host="0.0.0.0")

