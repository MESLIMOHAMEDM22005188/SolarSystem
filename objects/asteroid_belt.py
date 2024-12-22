import pygame
import random
import math


class AsteroidBelt:
    """
    Represents an asteroid belt in a solar system simulation.

    Attributes:
        center_x (int): The x-coordinate of the center of the belt (usually the sun).
        center_y (int): The y-coordinate of the center of the belt (usually the sun).
        inner_radius (float): The inner radius of the asteroid belt.
        outer_radius (float): The outer radius of the asteroid belt.
        count (int): The number of asteroids in the belt.
        color (tuple): The RGB color of the asteroids.
        asteroids (list): A list of tuples representing the positions of the asteroids.
    """

    def __init__(self, center_x, center_y, inner_radius, outer_radius, count, color):
        """
        Initializes a new asteroid belt.

        Args:
            center_x (int): The x-coordinate of the center of the belt (usually the sun).
            center_y (int): The y-coordinate of the center of the belt (usually the sun).
            inner_radius (float): The inner radius of the asteroid belt.
            outer_radius (float): The outer radius of the asteroid belt.
            count (int): The number of asteroids in the belt.
            color (tuple): The RGB color of the asteroids.
        """
        self.center_x = center_x
        self.center_y = center_y
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.count = count
        self.color = color
        self.asteroids = self.generate_asteroids()

    def generate_asteroids(self):
        """
        Generates random positions for the asteroids within the belt.

        Asteroids are distributed randomly between the inner and outer radii
        and along random angles around the center.

        Returns:
            list: A list of tuples (x, y) representing the asteroid positions.
        """
        asteroids = []
        for _ in range(self.count):
            radius = random.uniform(self.inner_radius, self.outer_radius)
            angle = random.uniform(0, 360)  # Random angle in degrees
            x = self.center_x + radius * math.cos(math.radians(angle))
            y = self.center_y + radius * math.sin(math.radians(angle))
            asteroids.append((x, y))
        return asteroids

    def draw(self, screen):
        """
        Draws the asteroids on the given pygame surface.

        Args:
            screen (pygame.Surface): The surface on which the asteroids will be drawn.
        """
        for x, y in self.asteroids:
            pygame.draw.circle(screen, self.color, (int(x), int(y)), 2)
