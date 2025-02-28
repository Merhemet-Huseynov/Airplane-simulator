class Plane:
    def __init__(self, name, capacity, speed, 
                 passengers=None, is_flying=False):

        self.name: str = str(name)
        self.capacity: int = int(capacity)
        self.speed: int = int(speed)
        self.passengers: list = []  
        self.is_flying: bool = is_flying

    def increase_speed(self) -> str:
        """
        Increases the plane's speed by 9 km/h and makes the plane take off 
        if speed is above 200 km/h.
        """
        if self.speed >= 900:
            return "Maximum speed reached!"
        
        self.speed += 9
        if self.speed >= 200 and not self.is_flying:
            self.is_flying = True
            return f"The plane took off. Speed: {self.speed} km/h"
        
        return f"Speed: {self.speed} km/h"

    def add_passenger(self, passenger_name: str) -> str:
        """
        Adds a passenger to the plane if there is enough capacity.
        """
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger_name)
            return f"{passenger_name} boarded the plane."

        return "Not enough capacity"

    def remove_passenger(self, passenger_name: str) -> str:
        """
        Removes a passenger from the plane if they are on board.
        """
        if passenger_name in self.passengers:
            self.passengers.remove(passenger_name)
            return f"{passenger_name} has been removed from the plane."

        return f"{passenger_name} is not on the plane."

    def take_off(self) -> str:
        """
        Takes off the plane if there are passengers and speed is above 0.
        """
        if len(self.passengers) > 0 and self.speed > 0:
            self.is_flying = True
            return "The plane is flying."

        return (
            "The plane cannot take off.\n"
            "Please ensure there are passengers and sufficient speed."
        )

    def land(self) -> str:
        """
        Lands the plane by reducing its speed to 0.
        """
        if not self.is_flying:
            return "The plane has already landed."
        
        while self.speed > 0:
            self.speed -= 9
            if self.speed < 100:
                return (
                    f"The plane landed successfully.\n"
                    f"Current speed {self.speed} km/h"
                )
        
        self.is_flying = False
        self.speed = 0
        return (
        "The plane has successfully stopped.\n"
        "The stairs are opening for passengers to disembark."
    )

    def __str__(self) -> str:
        """
        Returns a string representation of the plane including its name, 
        speed, passenger count, and flying status.
        """
        flying_status = "flying" if self.is_flying else "on the ground"
        return (
            f"Plane: {self.name}\n"
            f"Speed: {self.speed} km/h\n"
            f"Passengers: {len(self.passengers)}\n"
            f"out of {self.capacity}\n"
            f"Status: {flying_status}\n"
        )

    def current_status(self) -> None:
        """
        Prints the current status of the plane, including name, speed, 
        passenger count, and flying status.
        """
        print(f"Plane Name: {self.name}")
        print(f"Speed: {self.speed} km/h")
        print(f"Passengers: {len(self.passengers)}")
        print(f"Is Flying: {"Yes" if self.is_flying else "No"}")