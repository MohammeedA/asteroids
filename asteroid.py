import random
from circleshape import CircleShape
from pygame import draw
from constants import (
    ASTEROID_MIN_RADIUS
)

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        width = 2
        draw.circle(screen, "white", self.position, self.radius, width)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            velocity = self.velocity
            new_velocity1 = velocity.rotate(angle)
            new_velocity2 = velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x,self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x,self.position.y, new_radius)
            new_asteroid1.velocity = 1.2 * new_velocity1
            new_asteroid2.velocity = 1.2 * new_velocity2