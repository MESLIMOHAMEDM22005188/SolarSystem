import pygame
from objects.sun import Sun
from objects.planet import Planet
from objects.asteroid_belt import AsteroidBelt
from utils.color import YELLOW, ORANGE, GREEN, BLUE, RED, WHITE, LIGHT_GRAY

# Window dimensions
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")

# Sun
sun = Sun(WIDTH // 2, HEIGHT // 2, 30, YELLOW)

# Planets with scaled distances and sizes
planets = [
    Planet("Mercury", 50, 3, ORANGE, 2, 5),
    Planet("Venus", 80, 5, GREEN, 1.5, 3),
    Planet("Earth", 110, 6, BLUE, 1, 2),
    Planet("Mars", 140, 4, RED, 0.8, 1),
    Planet("Jupiter", 180, 8, WHITE, 0.5, 0.8),
    Planet("Saturn", 220, 7, LIGHT_GRAY, 0.4, 0.6),
    Planet("Uranus", 260, 6, GREEN, 0.3, 0.4),
    Planet("Neptune", 300, 6, BLUE, 0.25, 0.3),
]

# Moon (orbiting Earth)
moon = Planet("Moon", 15, 2, LIGHT_GRAY, 4, 0)  # Relative distance from Earth

# Asteroid belt
asteroid_belt = AsteroidBelt(sun.x, sun.y, 150, 170, 30, LIGHT_GRAY)

def main():
    """
    Main function to simulate and render the solar system.

    This function initializes the game loop, manages event handling, updates
    the positions of planets and the moon, and renders all objects on the screen.

    Objects Rendered:
    - Sun
    - Planets (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune)
    - Moon orbiting Earth
    - Asteroid belt between Mars and Jupiter
    """
    clock = pygame.time.Clock()  # Controls the frame rate
    running = True  # Game loop control

    while running:
        # Clear the screen with a black background
        screen.fill((0, 0, 0))

        # Handle user events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Render the sun
        sun.draw(screen)

        # Update and render planets
        for planet in planets:
            planet.update_position()
            planet.draw(screen, sun.x, sun.y)

        # Update and render the moon orbiting Earth
        earth_x, earth_y = planets[2].get_position(sun.x, sun.y)  # Earth = 3rd planet
        moon.update_position()
        moon.draw(screen, earth_x, earth_y)

        # Render the asteroid belt
        asteroid_belt.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # Limit the frame rate to 60 FPS
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    """
    Entry point for the program.
    This script starts the solar system simulation by calling the `main` function.
    """
    main()
