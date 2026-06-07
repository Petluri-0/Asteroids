import pygame
import random
from logger import log_event
from constants import LINE_WIDTH
from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape
class Asteroids(CircleShape):
    def __init__(self, x:float,y:float,radius:float) ->None:
        super().__init__(x,y,radius)
    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    def update(self, dt:float):
        self.position+=self.velocity*dt
    
    def split(self):
        self.kill()
        if(self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20,50)
            first_asteroid_movement = self.velocity.rotate(angle)
            second_asteroid_movement = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroids(self.position.x,self.position.y,new_radius)
            asteroid2 = Asteroids(self.position.x,self.position.y,new_radius)
            asteroid1.velocity = first_asteroid_movement * 1.2
            asteroid2.velocity = second_asteroid_movement * 1.2

