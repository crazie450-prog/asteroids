# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    # Initialize pygame and create a window
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Create sprite groups and set up containers
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = updateable, drawable
    Asteroid.containers = updateable, drawable, asteroids
    AsteroidField.containers = updateable
    Shot.containers = updateable, drawable, shots
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = Clock.tick(60)/1000  # Limit to 60 FPS and get delta time
        
        screen.fill((0, 0, 0))  # Clear screen with black
        updateable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!")
                return
        for entity in drawable:
                entity.draw(screen)
            
        pygame.display.flip()
        
        
    # Debug output    
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)   


if __name__ == "__main__":
    main()
