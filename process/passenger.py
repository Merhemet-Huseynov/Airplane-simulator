import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logging_info.logging_config import setup_logging

setup_logging()

class PassengerOperations:
    @staticmethod
    def add_passenger(plane, passenger_name: str) -> str:
        """
        Adds a passenger to the plane if there is enough capacity.
        """
        if len(plane.passengers) < plane.capacity:
            plane.passengers.append(passenger_name)
            logging.info(f"{passenger_name} boarded the plane.")
            return f"{passenger_name} boarded the plane."
        logging.warning("Not enough capacity to add passenger.")
        return "Not enough capacity"

    @staticmethod
    def remove_passenger(plane, passenger_name: str) -> str:
        """
        Removes a passenger from the plane if they are on board.
        """
        if passenger_name in plane.passengers:
            plane.passengers.remove(passenger_name)
            logging.info(f"{passenger_name} has been removed from the plane.")
            return f"{passenger_name} has been removed from the plane."
        logging.warning(f"{passenger_name} is not on the plane.")
        return f"{passenger_name} is not on the plane."
