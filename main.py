from settings import *
from level import Level

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Cosmic Rescue!")

        self.currentStage = Level()

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