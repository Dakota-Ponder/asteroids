import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()


    
    # new clock object 
    clock = pygame.time.Clock()
    
    # delta time to track change in time since last frame was drawn 
    dt = 0
    
    # groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # add instances to the groups   
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    
    
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
        # print("Game loop running")
        
        for obj in updatable:
            obj.update(dt)
        
        # collision check between the player and asteroids
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!!!")
                pygame.quit()
                sys.exit()
                
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                    
        
                
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)
        
            
            
        pygame.display.flip() # refresh loop 
        dt = clock.tick(60)/1000  # limit framerate to 60 FPS
        
         


if __name__ == "__main__":
    main()
