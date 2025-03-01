import sys
import os
from typing import List

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plane_data import get_random_plane
from plane_project import Plane
from data import (
    generate_fake_passengers, 
    random_passenger_count,
    max_speed
)


plane_name, plane_capacity = get_random_plane()
plane = Plane(plane_name, plane_capacity)
passenger_count = random_passenger_count(plane_capacity)
passenger_names = generate_fake_passengers(passenger_count)

def board_passengers(plane: Plane, passengers: List[str]) -> None:
    """Boards the passengers onto the plane."""
    for passenger in passengers:
        plane.add_passenger(passenger)

def display_boarded_passengers(plane: Plane) -> None:
    """Displays the passengers who have boarded the plane."""
    if not plane.passengers:
        print("No passengers on board.")

    for idx, passenger in enumerate(plane.passengers, start=1):
        print(f"{idx}. Passenger: {passenger} boarded the plane.")


# Board passengers and display the list
board_passengers(plane, passenger_names)
display_boarded_passengers(plane)
print(plane.increase_speed())
print(plane.decrease_speed())
