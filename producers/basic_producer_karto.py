"""
basic_producer_karto.py

Generate some unique streaming buzz messages.
"""

import os
import random
import time
from dotenv import load_dotenv
from utils.utils_logger import logger

load_dotenv()

def get_message_interval() -> int:
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", 3)
    interval: int = int(return_value)
    logger.info(f"Messages will be sent every {interval} seconds.")
    return interval

# Custom words for my unique producer
ADJECTIVES: list = ["amazing", "funny", "boring", "exciting", "weird", "crazy"]
ACTIONS: list = ["found", "saw", "tried", "shared", "loved", "hated"]
TOPICS: list = ["a movie", "a meme", "an app", "a trick", "a story", "a song"]

def generate_messages():
    while True:
        adjective = random.choice(ADJECTIVES)
        action = random.choice(ACTIONS)
        topic = random.choice(TOPICS)
        yield f"I just {action} {topic}! It was {adjective}."

def main() -> None:
    logger.info("START producer...")
    logger.info("Hit CTRL c (or CMD c) to close.")
    
    interval_secs: int = get_message_interval()
    for message in generate_messages():
        logger.info(message)
        time.sleep(interval_secs)

    logger.info("NOTE: See the `logs` folder to learn more.")
    logger.info("END producer.....")

if __name__ == "__main__":
    main()
