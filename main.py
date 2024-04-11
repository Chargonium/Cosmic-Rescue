from settings import *
from Logic.level import Level
from pytmx.util_pygame import load_pygame
from os.path import join

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Cosmic Rescue!")
        self.clock = pygame.time.Clock()

        self.tmx_maps = [load_pygame(join('.', 'data', 'levels', 'omni.tmx'))]

        self.currentStage = Level(self.tmx_maps[0])


    def run(self):
        while True:
            deltaTime = self.clock.tick(240) / 1000
            self.currentStage.run(deltaTime)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                    

            if pygame.key.get_pressed()[pygame.K_r]:
                return True

            pygame.display.update()

if __name__ == "__main__":
    run = True
    while run:
        game = Game()
        run = game.run()

    print("Exiting now!")
    sys.exit()
    
else:
    print("no, fuck off.")