#!/usr/bin/python3

class Drone:
    """
    Represents a drone that can take off, ascend, descend, and land.
    """

    def __init__(self, model, max_speed, battery_life):
        """
        Initialize a new drone.

        Args:
            model (str): The drone's model name.
            max_speed (int): The drone's maximum speed in kilometers per hour.
            battery_life (str): The drone's battery life duration.

        Attributes:
            model (str): The drone's model name.
            max_speed (int): The drone's maximum speed.
            battery_life (str): The drone's battery life.
            altitude (int): The current altitude of the drone.
            is_flying (bool): True if the drone is currently flying, False otherwise.
        """
        self.model = model
        self.max_speed = max_speed
        self.battery_life = battery_life
        self.altitude = 0
        self.is_flying = False

    def take_off(self):
        """
        Take off the drone.

        If the drone is not already flying, it becomes airborne.
        If the drone is already flying, it prints a message indicating that.
        """
        if not self.is_flying:
            print(f"{self.model} is taking off.")
            self.is_flying = True
        else:
            print(f"{self.model} is already flying.")

    def ascend(self, meters):
        """
        Ascend the drone to a specified altitude.

        Args:
            meters (int): The number of meters to ascend.

        If the drone is flying, it increases its current altitude.
        If the drone is grounded, it prints a message indicating that it cannot ascend.
        """
        if self.is_flying:
            self.altitude += meters
            print(f"{self.model} is ascending to {self.altitude} meters.")
        else:
            print(f"{self.model} cannot ascend while grounded.")

    def descend(self, meters):
        """
        Descend the drone to a specified altitude.

        Args:
            meters (int): The number of meters to descend.

        If the drone is flying, it decreases its current altitude.
        If the drone is grounded, it prints a message indicating that it cannot descend.
        """
        if self.is_flying:
            self.altitude -= meters
            print(f"{self.model} is descending to {self.altitude} meters.")
        else:
            print(f"{self.model} cannot descend while grounded.")

    def land(self):
        """
        Land the drone.

        If the drone is flying, it lands and sets its altitude to 0.
        If the drone is grounded, it prints a message indicating that it's already on the ground.
        """
        if self.is_flying:
            print(f"{self.model} is landing.")
            self.altitude = 0
            self.is_flying = False
        else:
            print(f"{self.model} is already on the ground.")

