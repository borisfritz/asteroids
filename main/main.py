# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.ms = 0
        # Debug variables
        self.previous_keys = pygame.key.get_pressed()
        self.elapsed_time = 0

        # Create Groups
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()

        # Create Player
        Player.containers = (self.updatable, self.drawable)
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    def debug_framerate(self):
        if self.elapsed_time >= 5:
            print(f"Milliseconds per frame: {self.ms}")
            self.elapsed_time = 0

    def debug_keys(self):
        current_keys = pygame.key.get_pressed()
        if current_keys[pygame.K_w] and not self.previous_keys[pygame.K_w]:
            print("W pressed!")
        if current_keys[pygame.K_s] and not self.previous_keys[pygame.K_s]:
            print("S pressed!")
        if current_keys[pygame.K_a] and not self.previous_keys[pygame.K_a]:
            print("A pressed!")
        if current_keys[pygame.K_d] and not self.previous_keys[pygame.K_d]:
            print("D pressed!")
        self.previous_keys = current_keys

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            # Debug Framerate
            self.elapsed_time += self.delta_time
            self.debug_framerate()

            # Draw and Update
            self.screen.fill("black")
            for obj in self.drawable:
                obj.draw(self.screen)
            self.updatable.update(self.delta_time)

            # Debug Keys
            self.debug_keys()

            # Draw Frame
            pygame.display.flip()

            #set FPS, or tick
            self.ms = self.clock.tick(60)
            self.delta_time = self.ms / 1000

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
