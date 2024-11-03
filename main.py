import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.display.init()


    
    # new clock object 
    clock = pygame.time.Clock()
    
    # delta time to track change in time since last frame was drawn 
    dt = 0
    
    # groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    # asteroidfield = pygame.sprite.Group()
    
    # add the player instances to both groups 
    Player.containers = (updatable, drawable)
    
    # add the asteroid instances to all groups 
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    
    
    # x,y coords to spawn player in middle of screen 
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x,y)  # player object
    asteroid_field = AsteroidField()
    
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
        # player.draw(screen)
        # player.update(dt)
        # Change the game loop to use the new groups instead of the Player object directly.
        # In other words, iterate over all "updatables" and .update() them, then iterate over
        # all "drawables" and .draw() them.
        for obj in updatable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!!!")
                pygame.quit()
                sys.exit()
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
            
            
        pygame.display.flip() # refresh loop 
        dt = clock.tick(60)/1000  # limit framerate to 60 FPS
        
         


if __name__ == "__main__":
    main()
