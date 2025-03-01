import pytest
from data.speed import max_speed

def test_max_speed() -> None:
    """Test max_speed function to ensure the speed is within the expected range."""
    for _ in range(100):
        speed = max_speed()
        assert 600 <= speed <= 900, f"Speed {speed} is out of range"
