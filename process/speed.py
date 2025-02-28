class SpeedOperations:
    @staticmethod
    def increase_speed(plane) -> str:
        """
        Increases the speed of the plane until it reaches 900 km/h.
        If the speed reaches 200 km/h and the plane is not flying, 
        it takes off.
        """
        while plane.speed < 900:
            if plane.speed >= 200 and not plane.is_flying:
                plane.is_flying = True
                return f"The plane took off. Speed: {plane.speed} km/h"
            plane.speed += 9
            return f"Speed: {plane.speed} km/h"
        return "Maximum speed reached!"
    
    @staticmethod
    def decrease_speed(plane) -> str:
        """
        Decreases the speed of the plane until it reaches 0 km/h.
        If the speed goes below 200 km/h and the plane is flying, it lands.
        """
        while plane.speed > 0:
            plane.speed -= 9
            if plane.speed < 200 and plane.is_flying:
                plane.is_flying = False
                return f"The plane landed. Speed: {plane.speed} km/h"
        return f"Speed: {plane.speed} km/h"
