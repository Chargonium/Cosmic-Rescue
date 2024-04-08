from settings import *
from sprites import Sprite
from player import Player
from GUI import HyperspeedMeter

class Level:
    def __init__(self, tmx_map) -> None:
        self.display_surface = pygame.display.get_surface()

        # groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.GUI_Sprites = pygame.sprite.Group()

        self.setup(tmx_map)
    
    def setup(self, tmx_map):
        for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
            Sprite((x*TILE_SIZE,y*TILE_SIZE), surf, (self.all_sprites, self.collision_sprites), 'black')
        # Sprite((1280-64,0), None, self.GUI_Sprites, 'red')

        for obj in tmx_map.get_layer_by_name('Objects'):
            if obj.name == 'player':
                HyperspeedMeter((1216,16), Player((obj.x, obj.y), (self.all_sprites, self.GUI_Sprites), self.collision_sprites), self.GUI_Sprites, 'green', self.display_surface)

    def run(self, deltaTime):
        self.all_sprites.update(deltaTime)
        self.display_surface.fill('grey')
        self.all_sprites.draw(self.display_surface)
        self.GUI_Sprites.draw(self.display_surface)
        self.GUI_Sprites.update(deltaTime)