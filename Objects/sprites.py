from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, color) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_frect(topleft=pos)
        self.oldRect = self.rect.copy()