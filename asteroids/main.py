# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.ms = 0
        self.elapsed_time = 0

    def test(self):
        if self.elapsed_time >= 5:
            print(f"Milliseconds per frame: {self.ms}")
            self.elapsed_time = 0


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            # Test
            self.elapsed_time += self.delta_time
            self.test()

            self.screen.fill((0,0,0))
            pygame.display.flip()
            self.ms = self.clock.tick(60)
            self.delta_time = self.ms / 1000
            # self.delta_time = self.clock.tick(60) / 1000

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
