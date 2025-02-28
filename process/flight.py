class FlightOperations:
    @staticmethod
    def take_off(plane) -> str:
        """
        Attempts to make the plane take off by checking if there are passengers 
        and sufficient speed. Returns a message indicating the result.
        """
        if len(plane.passengers) > 0 and plane.speed > 0:
            plane.is_flying = True
            return "The plane is flying."
        
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
        return (
            "The plane has successfully stopped.\n"
            "The stairs are opening for passengers to disembark."
        )
