import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from simulation_process import simulate_plane_operations
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

# Now call the function
simulate_plane_operations(plane, passenger_names)