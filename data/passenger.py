from faker import Faker
import random
import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plane_data.random_plane_selector import get_random_plane
from logging_info.logging_config import setup_logging

setup_logging()

fake = Faker()
plane_name, plane_capacity = get_random_plane()

def random_passenger_count(plane_capacity: int) -> int:
    """
    Generates a random number of passengers based on the plane's capacity.
    The number of passengers is a random value between 80% and 100% of the 
    plane's capacity.
    """
    min_passenger_count = int(plane_capacity * 0.8)  
    max_passenger_count = plane_capacity
    passengers = random.randint(min_passenger_count, max_passenger_count)
    logging.info(
        f"Plane capacity: {plane_capacity}. Generated random passenger count: {passengers}"
    )
    return passengers

def generate_fake_passengers(count: int) -> list[str]:
    """
    Generates a list of fake passenger names.
    """
    passengers = [fake.name() for _ in range(count)]
    logging.info(f"Generated {count} fake passenger names.")
    return passengers
