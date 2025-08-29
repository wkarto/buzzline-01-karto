"""
Custom Producer - basic_producer_karto.py

This producer simulates delivery status messages and writes them
to the shared log file for streaming analytics.
"""

import os
import time
import random
from utils.utils_logger import logger

# Custom message pool for delivery status
DELIVERY_MESSAGES: list = [
    "Package scanned at warehouse",
    "Package loaded on truck",
    "Package in transit",
    "Traffic delay reported",
    "Package delivered successfully",
    "Temperature ALERT: freezer failure",
    "System check passed",
    "Driver break - short delay expected",
    "Route updated due to traffic",
    "Package ready for pickup"
]

def generate_messages():
    """
    Generator that yields random delivery messages continuously.
    Uses MESSAGE_INTERVAL_SECONDS environment variable for timing (default = 3).
    """
    while True:
        message = random.choice(DELIVERY_MESSAGES)
        yield message
        time.sleep(int(os.getenv("MESSAGE_INTERVAL_SECONDS", 3)))

def main() -> None:
    """
    Producer entry point: continuously log delivery messages.
    """
    logger.info("Producer started: generating delivery messages...")
    for msg in generate_messages():
        logger.info(msg)

if __name__ == "__main__":
    main()
