# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
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

        # Create Player
        Player.containers = (self.updatable, self.drawable)
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        # Create Asteroids
        Asteroid.containers = (self.asteroids, self.updatable, self.drawable)

        # Create AsteroidField
        AsteroidField.containers = (self.updatable, )
        self.asteroid_field = AsteroidField()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            # Create Screen
            self.screen.fill("black")

            # Draw
            for obj in self.drawable:
                obj.draw(self.screen)

            # Update
            self.updatable.update(self.delta_time)

            # Debug Keys
            self.debugger.handle_debug_keys()

            # Refresh
            pygame.display.flip()

            # Set FPS
            self.ms = self.clock.tick(60)
            self.delta_time = self.ms / 1000

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
