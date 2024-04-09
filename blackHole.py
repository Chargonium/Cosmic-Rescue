from settings import *

"""
Distance = size**2
Speed = TerminalSpeed-(x/2)**2
"""

class blackHole(pygame.sprite.Sprite):
    def __init__(self, pos, groups, color, radius, surface) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((radius, radius))
        self.image.fill(color)
        self.rect = self.image.get_frect(topleft=pos)
        self.oldRect = self.rect.copy()
        self.detectionSprite = pygame.sprite.Group()
        self.surface = surface
        self.detectionRange(radius**2, pos, self.detectionSprite, radius)
        
    class detectionRange(pygame.sprite.Sprite):
        def __init__(self, size, pos, group, sizeTwo) -> None:
            super().__init__(group)
            self.image = pygame.Surface((size, size))
            self.image.fill('purple')
            self.rect = self.image.get_frect(topleft=Vector(pos[0]-(size/2-sizeTwo/2), pos[1]-(size/2-sizeTwo/2)))

    def update(self):
        self.detectionSprite.update()
        self.detectionSprite.draw(self.surface)