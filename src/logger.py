import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d')}.log"
LOG_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE)
LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

os.makedirs(LOG_PATH, exist_ok=True)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "%(levelname)s | %(asctime)s | Line: %(lineno)d | File: %(name)s | %(message)s",
    level = logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started.")
    