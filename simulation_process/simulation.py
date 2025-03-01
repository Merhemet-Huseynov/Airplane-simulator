import sys
import os
import random
import time
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plane_data import get_random_plane
from plane_project import Plane
from data import (
    generate_fake_passengers, 
    random_passenger_count,
    max_speed
)

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
        print(f"{idx}. Passenger: {passenger} boarded the plane.")


def remove_random_passengers(plane: Plane, passengers: List[str]) -> None:
    """
    Removes passengers from the plane randomly until the list is empty.
    """
    while passengers:
        clear_terminal()
        passenger = random.choice(passengers)
        print(f"Passenger {passenger} is getting off the plane.")
        plane.remove_passenger(passenger)
        passengers.remove(passenger)
        plane.current_status()
        print()

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
    print(plane.take_off())
    print(plane.increase_speed())
    print(plane.decrease_speed())
    print(plane.land())

    # Remove passengers randomly
    remove_random_passengers(plane, passengers)


