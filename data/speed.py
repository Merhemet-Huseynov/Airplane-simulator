import random
import logging
from logging_info.logging_config import setup_logging

setup_logging()

def max_speed() -> int:
    """
    This function generates a random speed between 600 and 900.
    """
    logging.debug("Generating a random speed between 600 and 900.")
    speed = random.randint(600, 900)
    logging.debug(f"Generated speed: {speed}")
    return speed
