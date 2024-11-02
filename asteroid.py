import pygame
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