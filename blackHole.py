from settings import *

"""
AffectionDistance = size**2
Speed = TerminalSpeed-(distance/2)**2
TerminalSpeed = affectionRadius**2/4
"""

class blackHole(pygame.sprite.Sprite):
    def __init__(self, pos, groups, color, radius, surface, players) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((radius, radius))
        self.image.fill(color)
        self.radius = radius
        self.rect = self.image.get_frect(topleft=pos)
        self.oldRect = self.rect.copy()
        self.detectionSprite = pygame.sprite.Group()
        self.surface = surface
        self.TerminalSpeed = (((radius+TILE_SIZE)**4)/4)
        print
        #self.TerminalSpeed = 100
        self.detectionRange(radius**2, pos, self.detectionSprite, radius, players, self)
        
        
    class detectionRange(pygame.sprite.Sprite):
        def __init__(self, size, pos, group, sizeTwo, objects, BlackHole) -> None:
            super().__init__(group)
            self.image = pygame.Surface((size, size))
            self.image.fill('purple')
            self.rect = self.image.get_frect(topleft=Vector(pos[0]-(size/2-sizeTwo/2), pos[1]-(size/2-sizeTwo/2)))
            self.objects = objects
            self.blackHole = BlackHole

        def calculateSpeed(self, distance):
            result = (self.blackHole.TerminalSpeed-(distance/2)**2)/2048
            if result < 0:
                print("NOOOOO")
                return 0
            return -result if distance < 0 else result

        def update(self, deltaTime):
            for sprite in self.objects:
                if sprite.rect.colliderect(self.rect):                    
                    Difference = Vector(self.blackHole.rect.center[0] - sprite.rect.center[0], self.blackHole.rect.center[1] - sprite.rect.center[1])
                    addedVelocity = Vector(self.calculateSpeed(Difference[0]), self.calculateSpeed(Difference[1]))
                    sprite.velocity += addedVelocity*deltaTime

    def update(self, deltaTime):
        self.detectionSprite.update(deltaTime)
        self.detectionSprite.draw(self.surface)