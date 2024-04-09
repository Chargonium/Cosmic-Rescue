from settings import *

class meter(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE/2, 0))
        self.rect = self.image.get_frect(topleft=(pos[0]+TILE_SIZE/4, pos[1]))
    
    def update(self, sizePercentage):
        self.image = pygame.Surface((TILE_SIZE/2, 64-sizePercentage*0.64))
        self.image.fill('red')

class HyperspeedMeter(pygame.sprite.Sprite):
    def __init__(self, pos, playerObject, groups, color, surface) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((TILE_SIZE/2, 64))
        self.image.fill(color)
        self.rect = self.image.get_frect(topleft=(pos[0]+TILE_SIZE/4, pos[1]))
        self.oldRect = self.rect.copy()
        self.player = playerObject
        self.surface = surface
        self.meterGroup = pygame.sprite.Group()
        meter(self.meterGroup, pos)
            
    def update(self, deltaTime):

        value = (100/self.player.hyperspeedMaxModifier)*self.player.hyperspeedModifier
        self.meterGroup.update(value)
        self.meterGroup.draw(self.surface)
        # value2 = 100-value 
        # self.image.fill((value2*2.55, value*2.55, 0))
        
