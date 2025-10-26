from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        """
        Splits the asteroid into two smaller asteroids if possible.

        Returns:
            list[Asteroid] | None: A list of two new Asteroid objects if the asteroid can be split,
            otherwise None.
        """
        # Remove this asteroid from the game externally after splitting
        if self.radius < ASTEROID_MIN_RADIUS * 2:
            return
        split_angle = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(split_angle)
        new_velocity2 = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity2 * 1.2
        return [asteroid1, asteroid2]
        