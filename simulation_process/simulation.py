import sys
import os
import random
import time
import logging
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logging_info.logging_config import setup_logging
from plane_data import get_random_plane
from plane_project import Plane
from data import (
    generate_fake_passengers, 
    random_passenger_count,
    max_speed
)

setup_logging()

# Get random plane details and initialize the plane
plane_name, plane_capacity = get_random_plane()
plane = Plane(plane_name, plane_capacity)

# Generate a random number of passengers and their names
passenger_count = random_passenger_count(plane_capacity)
passenger_names = generate_fake_passengers(passenger_count)

def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def board_passengers(plane: Plane, passengers: List[str]) -> None:
    """
    Boards the passengers onto the plane.
    """
    for passenger in passengers:
        plane.add_passenger(passenger)

        logging.info(f"Passenger {passenger} boarded the plane.")

def display_boarded_passengers(plane: Plane) -> None:
    """
    Displays the passengers who have boarded the plane.
    """
    if not plane.passengers:
        print("No passengers on board.")
        return

    for idx, passenger in enumerate(plane.passengers, start=1):
        clear_terminal()
        plane.current_status()
        logging.info(f"{idx}. Passenger: {passenger} boarded the plane.")
        print(f"{idx}. Passenger: {passenger} boarded the plane.")

def remove_random_passengers(plane: Plane, passengers: List[str]) -> None:
    """
    Removes passengers from the plane randomly until the list is empty.
    """
    while passengers:
        clear_terminal()
        passenger = random.choice(passengers)
        plane.remove_passenger(passenger)
        passengers.remove(passenger)
        print(f"Passenger {passenger} got off the plane.")
        plane.current_status()
        print()

    logging.info("All passengers have gotten off the plane.")
    print("All passengers have gotten off the plane.")

def simulate_plane_operations(plane: Plane, passengers: List[str]) -> None:
    """
    Simulates the boarding of passengers, plane operations (take off, speed change, landing),
    and the removal of passengers.
    """
    # Board passengers and display the list
    board_passengers(plane, passengers)
    display_boarded_passengers(plane)

    # Simulate plane operations
    logging.info("Plane is taking off.")
    print(plane.take_off())
    
    logging.info("Increasing speed.")
    print(plane.increase_speed())
    
    logging.info("Decreasing speed.")
    print(plane.decrease_speed())

    logging.info("Plane is landing.")
    print(plane.land())

    # Remove passengers randomly
    remove_random_passengers(plane, passengers)

