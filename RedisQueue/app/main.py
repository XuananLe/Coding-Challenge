"""
This file will push message to the queue
"""
import dotenv
import os
import random
import redis

dotenv.load_dotenv()


def create_redis():
    r = redis.StrictRedis(os.environ.get("REDIS_HOST"), os.environ.get("REDIS_PORT"), 0, decode_responses=True)
    return r, os.environ.get("REDIS_QUEUE_NAME")


def push_message(db: redis.StrictRedis, queue_name: str, message: str):
    db.lpush(queue_name, message)


def main(num_messsages: int, delay: float):
    db, queue_name = create_redis()
    print(queue_name)

if __name__ == "__main__":
    main(12, 1)
