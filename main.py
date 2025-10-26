# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    # Initialize pygame and create a window
    pygame.init()
    Clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()
        dt = Clock.tick(60)/1000  # Limit to 60 FPS and get delta time
        
    # Debug output    
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)   


if __name__ == "__main__":
    main()
