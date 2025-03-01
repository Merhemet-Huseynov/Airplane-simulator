import sys
import os
import logging
import pytest
from typing import List, Tuple

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logging_info.logging_config import setup_logging
from plane_data.random_plane_selector import get_random_plane
from data import random_passenger_count, generate_fake_passengers  

setup_logging()

def mock_get_random_plane() -> Tuple[str, int]:
    """
    Mock function to simulate fetching a random plane and its capacity.
    """
    return "Mock Plane", 200

@pytest.fixture
def setup_mock(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Fixture to mock the get_random_plane function using monkeypatch.
    """
    monkeypatch.setattr(
        "plane_data.random_plane_selector.get_random_plane", 
        mock_get_random_plane
    )

def test_random_passenger_count(setup_mock: None) -> None:
    """
    Test the random passenger count generation to ensure it's within the 
    acceptable range based on the plane capacity.
    """
    plane_capacity = 200 
    passengers = random_passenger_count(plane_capacity)
    
    assert 0.8 * plane_capacity <= passengers <= plane_capacity
    logging.info(f"Tested random passenger count for plane capacity {plane_capacity}: {passengers}")

def test_generate_fake_passengers() -> None:
    """
    Test the generation of fake passengers to ensure the correct number 
    of passengers is generated.
    """
    passenger_count = 10 
    passengers = generate_fake_passengers(passenger_count)
    
    assert len(passengers) == passenger_count
    logging.info(f"Tested fake passenger generation: {passengers}")
