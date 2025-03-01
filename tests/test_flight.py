import sys
import os
import pytest
from unittest.mock import MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from process.flight import FlightOperations

@pytest.fixture
def plane_mock():
    """
    Fixture to create a mock plane object for testing.
    """
    plane = MagicMock()
    plane.passengers = []
    plane.is_flying = False
    plane.speed = 0
    return plane

def test_take_off_with_passengers(plane_mock: MagicMock) -> None:
    """
    Test case for the take_off method when the plane has passengers.
    """
    plane_mock.passengers = ["Passenger 1"]
    result = FlightOperations.take_off(plane_mock)
    
    assert result == "The plane is ready to fly. Passenger count: 1"
    assert plane_mock.is_flying is True
    plane_mock.is_flying = True
    assert plane_mock.is_flying is True

def test_take_off_without_passengers(plane_mock: MagicMock) -> None:
    """
    Test case for the take_off method when the plane has no passengers.
    """
    plane_mock.passengers = [] 
    result = FlightOperations.take_off(plane_mock)
    
    assert result == (
        "The plane cannot take off.\n"
        "Please ensure there are passengers and sufficient speed."
    )
    assert plane_mock.is_flying is False
    plane_mock.is_flying = False
    assert plane_mock.is_flying is False

def test_land(plane_mock: MagicMock) -> None:
    """
    Test case for the land method when the plane is flying.
    """
    plane_mock.is_flying = True
    plane_mock.speed = 300
    result = FlightOperations.land(plane_mock)
    
    assert result == (
        "The plane has successfully stopped.\n"
        "The stairs are opening for passengers to disembark."
    )
    assert plane_mock.is_flying is False
    assert plane_mock.speed == 0
