import pytest
from plane_data import random_plane_selector
from unittest.mock import mock_open, patch
from typing import Tuple

@pytest.fixture
def sample_planes_data() -> str:
    """Returns a sample content for planes.txt file."""
    return "Boeing 747 - Capacity: 416 seats\nAirbus A320 - Capacity: 180 seats\nEmbraer E190 - Capacity: 114 seats"

@patch("builtins.open", new_callable=mock_open)
@patch("os.path.join", return_value="dummy_path")
def test_get_random_plane(mock_path_join, mock_file, sample_planes_data: str) -> None:
    """
    Tests the get_random_plane function by mocking the file reading process.
    Ensures that the returned plane name and capacity are correctly parsed.
    """
    mock_file.return_value.readlines.return_value = sample_planes_data.split("\n")

    plane_name, plane_capacity = random_plane_selector.get_random_plane()

    expected_planes = {
        "Boeing 747": 416,
        "Airbus A320": 180,
        "Embraer E190": 114
    }

    assert plane_name in expected_planes, "Plane name should be one of the expected names."
    assert plane_capacity == expected_planes[plane_name], "Capacity should match the expected value."
