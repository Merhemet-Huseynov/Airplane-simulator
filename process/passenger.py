class PassengerOperations:
    @staticmethod
    def add_passenger(plane, passenger_name: str) -> str:
        """
        Adds a passenger to the plane if there is enough capacity.
        """
        if len(plane.passengers) < plane.capacity:
            plane.passengers.append(passenger_name)
            return f"{passenger_name} boarded the plane."
        return "Not enough capacity"

    @staticmethod
    def remove_passenger(plane, passenger_name: str) -> str:
        """
        Removes a passenger from the plane if they are on board.
        """
        if passenger_name in plane.passengers:
            plane.passengers.remove(passenger_name)
            return f"{passenger_name} has been removed from the plane."
        return f"{passenger_name} is not on the plane."
