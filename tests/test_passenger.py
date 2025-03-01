import sys
import os
import pytest
from unittest.mock import MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from process.passenger import PassengerOperations

@pytest.fixture
def mock_plane():
    """
    Fixture to create a mock plane object with capacity and passengers.
    """
    mock_plane = MagicMock()
    mock_plane.capacity = 3
    mock_plane.passengers = []
    return mock_plane

def test_add_passenger(mock_plane):
    """
    Test for adding a passenger to the plane.
    Ensures that a passenger can board if there is enough capacity.
    """
    passenger_name = "John Doe"
    result = PassengerOperations.add_passenger(mock_plane, passenger_name)
    assert result == "John Doe boarded the plane."
    assert passenger_name in mock_plane.passengers

def test_add_passenger_no_capacity(mock_plane):
    """
    Test for adding a passenger when there is no capacity.
    Ensures that an error message is returned when the plane is full.
    """
    # Filling the plane to its capacity
    mock_plane.passengers = ["Alice", "Bob", "Charlie"]
    passenger_name = "John Doe"
    result = PassengerOperations.add_passenger(mock_plane, passenger_name)
    assert result == "Not enough capacity"
    assert passenger_name not in mock_plane.passengers

def test_remove_passenger(mock_plane):
    """
    Test for removing a passenger from the plane.
    Ensures that a passenger can be removed if they are on board.
    """
    passenger_name = "John Doe"
    mock_plane.passengers = [passenger_name]
    result = PassengerOperations.remove_passenger(mock_plane, passenger_name)
    assert result == "John Doe has been removed from the plane."
    assert passenger_name not in mock_plane.passengers

def test_remove_passenger_not_on_board(mock_plane):
    """
    Test for removing a passenger who is not on the plane.
    Ensures that an error message is returned if the passenger is not on the plane.
    """
    passenger_name = "John Doe"
    result = PassengerOperations.remove_passenger(mock_plane, passenger_name)
    assert result == "John Doe is not on the plane."
    assert passenger_name not in mock_plane.passengers
