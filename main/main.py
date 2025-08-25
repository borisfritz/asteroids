# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from circleshape import CircleShape
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from debug import GameDebugger

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.ms = 0

        # debugger
        self.debugger = GameDebugger(self)
        self.debugger.debug_menu()

        # Create Groups
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

        # Create Player
        Player.containers = (self.updatable, self.drawable)
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        # Create Asteroid Group
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)

        # Create Shot Group
        Shot.containers = (self.shots, self.updatable, self.drawable)

        # Create AsteroidField
        AsteroidField.containers = (self.updatable, )
        self.asteroid_field = AsteroidField()

    def player_collision(self):
        for each_asteroid in self.asteroids:
            if self.player.collision_check(each_asteroid):
                print("==================================")
                print("=========== Game Over! ===========")
                print("==================================")
                sys.exit()

    def asteroid_collision(self):
        asteroids_to_check = list(self.asteroids)
        num_asteroids = len(asteroids_to_check)
        for i in range(num_asteroids):
            asteroid1 = asteroids_to_check[i]
            for j in range(i + 1, num_asteroids):
                asteroid2 = asteroids_to_check[j]
                if asteroid1.collision_check(asteroid2):
                    normal_vector = (asteroid1.position - asteroid2.position).normalize()
                    new_velocity_asteroid1 = asteroid1.velocity.reflect(normal_vector)
                    new_velocity_asteroid2 = asteroid2.velocity.reflect(-normal_vector)
                    asteroid1.velocity = new_velocity_asteroid1
                    asteroid2.velocity = new_velocity_asteroid2

    def asteroid_shot(self):
        for each_asteroid in self.asteroids:
            for each_shot in self.shots:
                if each_asteroid.collision_check(each_shot):
                    each_asteroid.split()
                    each_shot.kill()

    def run(self):
        while True:
            # Event Handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            # Debuger Inputs
            self.debugger.handle_debug_keys()

            # Update
            self.updatable.update(self.delta_time)
            self.asteroid_collision()
            self.player_collision()
            self.asteroid_shot()

            # Clear
            self.screen.fill("black")

            # Draw
            for obj in self.drawable:
                obj.draw(self.screen)

            # Display
            pygame.display.flip()

            # Set FPS
            self.ms = self.clock.tick(60)
            self.delta_time = self.ms / 1000

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
