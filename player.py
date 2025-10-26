from circleshape import CircleShape
import pygame
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0  # in degrees
        self.shoot_cooldown = 0.3  # seconds
        self.shoot_timer = 0.0
        
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

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360 # keep rotation within 0-359 degrees
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
            
    def shoot(self):
        if self.shoot_timer <= 0.0:
            self.shoot_timer = self.shoot_cooldown
            shot = Shot(self.position.x, self.position.y)
            forward = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            shot.velocity = forward
            return shot
        else:
            return None