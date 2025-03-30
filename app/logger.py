import logging
import os

LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger(name: str, log_file: str, level=logging.INFO):
    log_path = os.path.join(LOG_DIR, log_file)

    handler = logging.FileHandler(log_path, encoding="utf-8")
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.hasHandlers():
        logger.addHandler(handler)
    logger.propagate = False

    return logger
