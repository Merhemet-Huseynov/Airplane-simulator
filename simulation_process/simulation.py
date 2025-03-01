import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data import generate_fake_passengers, random_passenger_count
from plane_data import get_random_plane
from plane_project import Plane


plane_name, plane_capacity = get_random_plane()
plane = Plane(plane_name, plane_capacity)
passenger_count = random_passenger_count(plane_capacity)
passenger_name = generate_fake_passengers(passenger_count)

def plane_added_passenger():
    return plane.add_passenger(passenger_name)