import pytest
from process import FlightOperations, SpeedOperations, PassengerOperations
from plane_project import Plane

@pytest.fixture
def plane():
    """
    Creates a Plane instance for testing purposes.
    """
    return Plane(
        name="Test Plane",
        capacity=100, 
        speed=0, 
        passengers=[], 
        is_flying=False
    )

def test_decrease_speed(plane: Plane) -> None:
    """
    Tests if the plane's speed decreases correctly.
    """
    plane.speed = 300
    SpeedOperations.decrease_speed(plane)
    assert plane.speed < 300

def test_add_passenger(plane: Plane) -> None:
    """
    Tests if a passenger is added correctly.
    """
    passenger_name = "John Doe"
    PassengerOperations.add_passenger(plane, passenger_name)
    assert passenger_name in plane.passengers

def test_remove_passenger(plane: Plane) -> None:
    """
    Tests if a passenger is removed correctly.
    """
    passenger_name = "Jane Doe"
    plane.passengers.append(passenger_name)
    PassengerOperations.remove_passenger(plane, passenger_name)
    assert passenger_name not in plane.passengers

def test_take_off(plane: Plane) -> None:
    """
    Tests if the plane takes off correctly.
    """
    plane.passengers.append("Test Passenger")
    FlightOperations.take_off(plane)
    assert plane.is_flying is True

def test_land(plane: Plane) -> None:
    """
    Tests if the plane lands correctly.
    """
    plane.is_flying = True
    FlightOperations.land(plane)
    assert plane.is_flying is False
