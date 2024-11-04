import pygame
import random
from constants import * 
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
    # override the draw method 
    def draw(self, screen):
        # draw the asteroid as a pygame.draw.circle. Use its position, radius, and a width of 2
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
        
    def update(self, dt):
        # moves in a straight line at constant speed. 
        # On each frame, it should add (velocity * dt) to its position.
        self.position += self.velocity * dt 
        
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            # spawn 2 new asteroids 
            random_angle = random.uniform(20, 50)
            
            vector_one = self.velocity.rotate(random_angle) 
            vector_two = self.velocity.rotate(-random_angle)
            
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            # create two new asteroid objects at the current radius 
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            
            # set the new asteroids velocities to the new random vectors 
            asteroid1.velocity = vector_one * 1.2
            asteroid2.velocity = vector_two * 1.2 
            
            