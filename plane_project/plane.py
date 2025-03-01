from process import FlightOperations, SpeedOperations, PassengerOperations

class Plane:
    """
    Represents a plane with attributes such as name, capacity, speed, 
    passengers, and flight status.
    """

    def __init__(self, name="Unknown", capacity=0, speed=0, passengers=None, is_flying=False):
        """
        Initializes the plane with the provided name, capacity, 
        speed, passengers, and flight status.
        """
        self.name: str = str(name)
        self.capacity: int = int(capacity)
        self.speed: int = int(speed)
        self.passengers: list = []  
        self.is_flying: bool = is_flying

    def increase_speed(self) -> str:
        """
        Increases the plane's speed using SpeedOperations.
        """
        return SpeedOperations.increase_speed(self)
    
    def decrease_speed(self) -> str:
        """
        Decreases the plane's speed using SpeedOperations.
        """
        return SpeedOperations.decrease_speed(self)

    def add_passenger(self, passenger_name: str) -> str:
        """
        Adds a passenger to the plane.
        """
        return PassengerOperations.add_passenger(self, passenger_name)

    def remove_passenger(self, passenger_name: str) -> str:
        """
        Removes a passenger from the plane.
        """
        return PassengerOperations.remove_passenger(self, passenger_name)

    def take_off(self) -> str:
        """
        Makes the plane take off using FlightOperations.
        """
        return FlightOperations.take_off(self)

    def land(self) -> str:
        """
        Makes the plane land using FlightOperations.
        """
        return FlightOperations.land(self)

    def __str__(self) -> str:
        """
        Returns a string representation of the plane's current status.
        """
        flying_status = "flying" if self.is_flying else "on the ground"
        return (
            f"Plane: {self.name}\n"
            f"Speed: {self.speed} km/h\n"
            f"Passengers: {len(self.passengers)}\n"
            f"Capacity: {self.capacity}\n"
            f"Status: {flying_status}\n"
        )

    def current_status(self) -> None:
        """
        Prints the current status of the plane including name, 
        speed, passengers, and flying status.
        """
        print(f"Plane Name: {self.name}")
        print(f"Speed: {self.speed} km/h")
        print(f"Passengers: {len(self.passengers)}")
        print(f"Is Flying: {"Yes" if self.is_flying else "No"}")
