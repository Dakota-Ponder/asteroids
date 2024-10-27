import pygame
from constants import *


def main():
    pygame.display.init()
    # screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # screen = pygame.display.set_mode((800, 600))  # Simple window with set dimensions
    
    
    # Set up the screen and check for errors
    try:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Window initialized successfully.")
    except pygame.error as e:
        print(f"Error initializing window: {e}")
        return  # Exit the function if the window can't be created

    pygame.display.set_caption("Asteroids Game")
    
    
    while True:
        
        # makes the close button on the pop up window work 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        print("Game loop running")
        screen.fill("black")
        pygame.display.flip()


if __name__ == "__main__":
    main()
