from circleshape import CircleShape
import pygame
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0  # in degrees
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.position.x -= 200 * dt
        if keys[pygame.K_RIGHT]:
            self.position.x += 200 * dt
        if keys[pygame.K_UP]:
            self.position.y -= 200 * dt
        if keys[pygame.K_DOWN]:
            self.position.y += 200 * dt

        # Keep player within screen bounds
        self.position.x = max(self.radius, min(SCREEN_WIDTH - self.radius, self.position.x))
        self.position.y = max(self.radius, min(SCREEN_HEIGHT - self.radius, self.position.y))