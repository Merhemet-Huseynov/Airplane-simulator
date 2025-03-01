import random
import os
from typing import Tuple

def get_random_plane() -> Tuple[str, int]:
    """
    Reads a file "planes.txt" and returns a random plane's name and its capacity.
    """
    # Write the file path directly here
    file_path = os.path.join(os.path.dirname(__file__), "planes.txt")

    # Read the file
    with open(file_path, "r") as file:
        planes = file.readlines()

    # Separate each plane
    planes_info = []
    for plane in planes:
        name, capacity = plane.strip().split(" - Capacity: ")
        planes_info.append((name, int(capacity.split()[0]))) 

    # Choose a random plane
    random_plane = random.choice(planes_info)

    # Return the plane name and capacity in separate variables
    plane_name, plane_capacity = random_plane
    return plane_name, plane_capacity
