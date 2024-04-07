from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Cosmic Rescue!")

        self.tmx_maps = [load_pygame(join('.', 'data', 'levels', 'omni.tmx'))]

        self.currentStage = Level(self.tmx_maps[0])

    def __runAll(self):
        self.currentStage.run()

    def run(self):
        while True:
            self.__runAll()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

if __name__ == "__main__":
    game = Game()
    game.run()
else:
    print("no, fuck off.")