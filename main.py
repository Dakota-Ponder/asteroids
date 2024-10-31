import pygame
from constants import *
from player import Player


def main():
    pygame.display.init()


    
    # new clock object 
    clock = pygame.time.Clock()
    
    # delta time to track change in time since last frame was drawn 
    dt = 0
    
    # x,y coords to spawn player in middle of screen 
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)  # player object
    
    # Set up the screen and check for errors
    try:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print("Window initialized successfully.")
    except pygame.error as e:
        print(f"Error initializing window: {e}")
        return  # Exit the function if the window can't be created

    pygame.display.set_caption("Asteroids Game")
    
    
    # game loop 
    while True:
        
        # makes the close button on the pop up window work 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        print("Game loop running")
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip() # refresh loop 
        dt = clock.tick(60)/1000  # limit framerate to 60 FPS
        
         


if __name__ == "__main__":
    main()
