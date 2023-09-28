import json
import os
import random

import dotenv
import redis

dotenv.load_dotenv()


def create_redis():
    r = redis.StrictRedis(os.environ.get("REDIS_HOST"), os.environ.get("REDIS_PORT"), 0, decode_responses=True)
    r.ping()
    return r, os.environ.get("REDIS_QUEUE_NAME")


# Incase the worker somehow can not process the message, we can push it back to the queue
def push_message(db: redis.StrictRedis, queue_name: str, message: str):
    db.lpush(queue_name, message)


def pop_message(db: redis.StrictRedis, queue_name: str) -> str:
    # pop from the right of the queue
    # wait until the message become available, blocking until have message to process
    # block the pop until có gì đó để pop
    _, message_json = db.brpop(queue_name)
    # Có thể nhét lại cái message json này vào redis khác :v nhiều tác dụng
    return message_json


def process_message(db, message_json: str):
    message = json.loads(message_json)
    print(f"Message received: id={message['id']}, message_number={message['data']['message_number']}")

    # mimic potential processing errors
    processed_ok = random.choices((True, False), weights=(5, 1), k=1)[0]
    if processed_ok:
        print(f"\tProcessed successfully")
    else:
        print(f"\tProcessing failed - requeuing...")
        push_message(db, "queue", message_json)


def main():
    """
    Consume items from the Redis queue
    :return:
    """
    db, queuename = create_redis()
    while True:
        message = pop_message(db, queue_name=queuename)  # bị block cho đến khi
        process_message(db, message)


if __name__ == "__main__":
    main()
