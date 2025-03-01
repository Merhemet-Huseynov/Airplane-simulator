import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logging_info.logging_config import setup_logging

setup_logging()

class FlightOperations:
    @staticmethod
    def take_off(plane) -> str:
        """
        Attempts to make the plane take off by checking if there are passengers 
        and sufficient speed. Returns a message indicating the result.
        """
        passengers_count = len(plane.passengers)
        
        if passengers_count > 0:
            plane.is_flying = True
            logging.info(f"Take off successful. Passenger count: {passengers_count}")
            return f"The plane is ready to fly. Passenger count: {passengers_count}"
        
        logging.warning("Take off failed. No passengers on board.")
        return (
            "The plane cannot take off.\n"
            "Please ensure there are passengers and sufficient speed."
        )

    @staticmethod
    def land(plane) -> str:
        """
        Lands the plane by setting the is_flying flag to False and speed to 0.
        Returns a message indicating the plane has landed and stairs are opening.
        """
        plane.is_flying = False
        plane.speed = 0
        logging.info("Plane has landed. Speed set to 0.")
        return (
            "The plane has successfully stopped.\n"
            "The stairs are opening for passengers to disembark."
        )
