import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta_time):
        self.position += (self.velocity * delta_time)

    def split (self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20,50)
            asteroid1_velocity = self.velocity.rotate(new_angle)
            asteroid2_velocity = self.velocity.rotate(-new_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x - self.radius, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x + self.radius, self.position.y, new_radius)
            asteroid1.velocity = asteroid1_velocity * 1.2
            asteroid2.velocity = asteroid2_velocity * 1.2
