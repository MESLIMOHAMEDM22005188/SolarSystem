import pygame

class Sun:
    """
    Represents the sun in a solar system simulation.

    Attributes:
        x (int): The x-coordinate of the sun's position on the screen.
        y (int): The y-coordinate of the sun's position on the screen.
        radius (int): The radius of the sun in pixels.
        color (tuple): The RGB color of the sun.
    """

    def __init__(self, x, y, radius, color):
        """
        Initializes a new Sun object.

        Args:
            x (int): The x-coordinate of the sun's position on the screen.
            y (int): The y-coordinate of the sun's position on the screen.
            radius (int): The radius of the sun in pixels.
            color (tuple): The RGB color of the sun.
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, screen):
        """
        Draws the sun on the given pygame surface.

        Args:
            screen (pygame.Surface): The surface on which the sun will be drawn.
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
