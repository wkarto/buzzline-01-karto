"""
basic_consumer_karto.py

Read a log file as it is being written and alert on special messages.
"""

import os
import time
from utils.utils_logger import logger, get_log_file_path

def process_message(log_file) -> None:
    with open(log_file, "r") as file:
        file.seek(0, os.SEEK_END)
        print("Consumer is ready and waiting for a new log message...")

        while True:
            line = file.readline()
            if not line:
                time.sleep(1)
                continue

            message = line.strip()
            print(f"Consumed log message: {message}")

            # Alert on any message with "crazy"
            if "crazy" in message:
                alert_text = f"ALERT: Crazy message detected! \n{message}"
                print(alert_text)
                logger.warning(alert_text)

def main() -> None:
    logger.info("START consumer...")

    log_file_path = get_log_file_path()
    logger.info(f"Reading file located at {log_file_path}.")

    try:
        process_message(log_file_path)
    except KeyboardInterrupt:
        print("User stopped the process.")

    logger.info("END consumer.....")

if __name__ == "__main__":
    main()
