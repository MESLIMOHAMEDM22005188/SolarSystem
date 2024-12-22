import pygame
import math

class Planet:
    """
    Represents a planet in a solar system simulation.

    Attributes:
        name (str): The name of the planet.
        distance (int): The distance of the planet from the center (e.g., the sun) in pixels.
        radius (int): The radius of the planet in pixels.
        color (tuple): The RGB color of the planet.
        orbit_speed (float): The angular speed of the planet's orbit (degrees per frame).
        self_rotation_speed (float): The angular speed of the planet's self-rotation (degrees per frame).
        orbit_angle (float): The current angle of the planet's orbit (in degrees).
        self_rotation_angle (float): The current angle of the planet's self-rotation (in degrees).
        is_saturn (bool): Indicates if the planet is Saturn (used to draw rings).
    """

    def __init__(self, name, distance, radius, color, orbit_speed, self_rotation_speed, is_saturn=False):
        """
        Initializes a new instance of the Planet class.

        Args:
            name (str): The name of the planet.
            distance (int): The distance of the planet from the center (e.g., the sun) in pixels.
            radius (int): The radius of the planet in pixels.
            color (tuple): The RGB color of the planet.
            orbit_speed (float): The angular speed of the planet's orbit (degrees per frame).
            self_rotation_speed (float): The angular speed of the planet's self-rotation (degrees per frame).
            is_saturn (bool): Indicates if the planet is Saturn (default is False).
        """
        self.name = name
        self.distance = distance
        self.radius = radius
        self.color = color
        self.orbit_speed = orbit_speed
        self.self_rotation_speed = self_rotation_speed
        self.orbit_angle = 0  # Initial orbit angle
        self.self_rotation_angle = 0  # Initial self-rotation angle
        self.is_saturn = is_saturn

    def update_position(self):
        """
        Updates the angles for the planet's orbit and self-rotation.

        The orbit angle determines the planet's position along its orbit.
        The self-rotation angle determines the rotation of the planet itself.
        """
        self.orbit_angle += self.orbit_speed
        self.orbit_angle %= 360  # Keeps the orbit angle within [0, 360)

        self.self_rotation_angle += self.self_rotation_speed
        self.self_rotation_angle %= 360  # Keeps the self-rotation angle within [0, 360)

    def get_position(self, center_x, center_y):
        """
        Calculates the planet's position in Cartesian coordinates.

        Args:
            center_x (int): The x-coordinate of the orbit center (e.g., the sun's x-coordinate).
            center_y (int): The y-coordinate of the orbit center (e.g., the sun's y-coordinate).

        Returns:
            tuple: A tuple (x, y) representing the planet's current position in pixels.
        """
        x = center_x + self.distance * math.cos(math.radians(self.orbit_angle))
        y = center_y + self.distance * math.sin(math.radians(self.orbit_angle))
        return int(x), int(y)

    def draw(self, screen, center_x, center_y):
        """
        Draws the planet and, if applicable, additional features like Saturn's ring.

        Args:
            screen (pygame.Surface): The pygame surface on which to draw the planet.
            center_x (int): The x-coordinate of the orbit center (e.g., the sun's x-coordinate).
            center_y (int): The y-coordinate of the orbit center (e.g., the sun's y-coordinate).
        """
        # Get the planet's current position
        x, y = self.get_position(center_x, center_y)

        # Draw Saturn's ring if applicable
        if self.is_saturn:
            pygame.draw.ellipse(
                screen,
                (180, 180, 180),  # Color of the ring
                pygame.Rect(
                    x - self.radius * 2,  # Width adjustment
                    y - self.radius // 2,  # Height adjustment
                    self.radius * 4,  # Width of the ellipse
                    self.radius,  # Height of the ellipse
                ),
                2,  # Thickness of the ring
            )

        # Draw the planet
        pygame.draw.circle(screen, self.color, (x, y), self.radius)

        # Draw a line to visualize the self-rotation
        line_length = self.radius
        end_x = x + line_length * math.cos(math.radians(self.self_rotation_angle))
        end_y = y + line_length * math.sin(math.radians(self.self_rotation_angle))
        pygame.draw.line(screen, (255, 255, 255), (x, y), (end_x, end_y), 2)
