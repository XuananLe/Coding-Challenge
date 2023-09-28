"""
This file will push message to the queue
"""
import json
import os
import random
import time
from datetime import datetime
from uuid import uuid4

import dotenv
import redis

dotenv.load_dotenv()


def create_redis():
    r = redis.StrictRedis(os.environ.get("REDIS_HOST"), os.environ.get("REDIS_PORT"), 0, decode_responses=True)
    return r, os.environ.get("REDIS_QUEUE_NAME")


def push_message(db: redis.StrictRedis, queue_name: str, message: str):
    db.lpush(queue_name, message)


def main(num_messsages: int, delay: float):
    db, queue_name = create_redis()
    db.flushall()
    for i in range(num_messsages):
        message = {
            "id": str(uuid4()),
            "ts": datetime.utcnow().isoformat(),
            "data": {
                "message_number": i,
                "x": random.randrange(0, 100),
                "y": random.randrange(0, 100),
            },
        }
        message = json.dumps(message)
        push_message(db, queue_name, message)
        print("Pushed message to queue")
        time.sleep(delay)


if __name__ == "__main__":
    main(1000000, 0.1)
