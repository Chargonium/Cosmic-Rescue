from settings import *
from sprites import Sprite
from player import Player
from GUI import HyperspeedMeter
from blackHole import blackHole

class Level:
    def __init__(self, tmx_map) -> None:
        self.display_surface = pygame.display.get_surface()

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.GUI_Sprites = pygame.sprite.Group()
        self.blackHoleSprites = pygame.sprite.Group()
        self.playerSprites = pygame.sprite.Group()

        self.setup(tmx_map)
    
    def setup(self, tmx_map):
        for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x*TILE_SIZE,y*TILE_SIZE), surf, (self.all_sprites, self.collision_sprites), 'black')
        blackHole((WINDOW_WIDTH/2, WINDOW_HEIGHT/8), self.blackHoleSprites, 'red', TILE_SIZE/8, self.display_surface, self.playerSprites)

        for obj in tmx_map.get_layer_by_name('Objects'):
            if obj.name == 'player':
                HyperspeedMeter((1216,16), Player((obj.x, obj.y), (self.all_sprites, self.GUI_Sprites, self.playerSprites), self.collision_sprites), self.GUI_Sprites, 'green', self.display_surface)

    def run(self, deltaTime):
        self.display_surface.fill('grey')
        self.blackHoleSprites.update(deltaTime)
        self.blackHoleSprites.draw(self.display_surface)
        self.all_sprites.update(deltaTime)
        self.all_sprites.draw(self.display_surface)
        self.GUI_Sprites.draw(self.display_surface)
        self.GUI_Sprites.update(deltaTime)
        