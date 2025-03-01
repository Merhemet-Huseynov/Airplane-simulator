import sys
import os
import pytest
from unittest.mock import MagicMock
import random
from typing import List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from plane_project import Plane
from data import generate_fake_passengers, random_passenger_count, max_speed
from plane_data import get_random_plane

@pytest.fixture
def plane_and_passengers() -> Tuple[Plane, List[str]]:
    """
    A fixture to create a plane and random passengers for testing.
    """
    plane_name, plane_capacity = get_random_plane()
    plane = Plane(plane_name, plane_capacity)
    passenger_count = random_passenger_count(plane_capacity)
    passengers = generate_fake_passengers(passenger_count)
    
    return plane, passengers

def test_board_passengers(plane_and_passengers: Tuple[Plane, List[str]]) -> None:
    """
    Test the boarding of passengers onto the plane.
    """
    plane, passengers = plane_and_passengers
    for passenger in passengers:
        plane.add_passenger(passenger)
    
    assert len(plane.passengers) == len(passengers)
    for passenger in passengers:
        assert passenger in plane.passengers

def test_remove_random_passengers(plane_and_passengers: Tuple[Plane, List[str]]) -> None:
    """
    Test the removal of a random passenger from the plane.
    """
    plane, passengers = plane_and_passengers
    for passenger in passengers:
        plane.add_passenger(passenger)

    random_passenger = random.choice(plane.passengers)
    plane.remove_passenger(random_passenger)  

    assert random_passenger not in plane.passengers
    assert len(plane.passengers) == len(passengers) - 1

def test_plane_operations(plane_and_passengers: Tuple[Plane, List[str]]) -> None:
    """
    Test the plane's operations including take-off.
    """
    plane, passengers = plane_and_passengers
    for passenger in passengers:
        plane.add_passenger(passenger)

    assert plane.decrease_speed() == f"Speed decreased to 0 km/h"