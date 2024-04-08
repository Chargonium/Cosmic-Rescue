from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collisionSprites):
        super().__init__(groups)
        self.image = pygame.Surface((48, 56))
        self.image.fill('red')

        # Rects
        self.rect = self.image.get_frect(topleft=pos)
        self.oldRect = self.rect.copy()
        
        # Movement
        self.direction = Vector(0, 0)
        self.speed = 400
        self.hyperspeedMaxModifier = 16000
        self.hyperspeedModifier = 0
        self.hyperspeedChargeRateModifier=4000

        # Collision
        self.collisionSprites = collisionSprites

        #return self

    def input(self, deltaTime):
        keys = pygame.key.get_pressed()
        input_vector = Vector(0,0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            input_vector.x += 1

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            input_vector.x -= 1

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            input_vector.y += 1

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            input_vector.y -= 1

        hyperspeedChargeRate = (self.hyperspeedMaxModifier - self.hyperspeedModifier) / self.hyperspeedMaxModifier

        if keys[pygame.K_LSHIFT]:
            self.hyperspeedModifier += (hyperspeedChargeRate*self.hyperspeedChargeRateModifier)*deltaTime
        else:
            self.hyperspeedModifier -= ((1-hyperspeedChargeRate)*self.hyperspeedChargeRateModifier)*deltaTime

        if self.hyperspeedModifier > self.hyperspeedMaxModifier:
            self.hyperspeedModifier = self.hyperspeedMaxModifier
        if self.hyperspeedModifier < 0:
            self.hyperspeedModifier = 0

        #print(self.hyperspeedModifier)

        self.direction = input_vector.normalize() if input_vector else input_vector

    def move(self, deltaTime):
        self.rect.x += self.direction.x * (self.speed + self.hyperspeedModifier) * deltaTime
        self.collision('horizontal')

        self.rect.y += self.direction.y * (self.speed + self.hyperspeedModifier) * deltaTime
        self.collision('vertical')

    def collision(self, axis):
        for sprite in self.collisionSprites:
            if sprite.rect.colliderect(self.rect):
                if axis == 'horizontal':
                    # left
                    if self.rect.left <= sprite.rect.right and self.oldRect.left >= sprite.oldRect.right:
                        self.rect.left = sprite.rect.right
                    # right
                    if self.rect.right >= sprite.rect.left and self.oldRect.right <= sprite.oldRect.left:
                        self.rect.right = sprite.rect.left
                else:
                    # up
                    if self.rect.top <= sprite.rect.bottom and self.oldRect.top >= sprite.oldRect.bottom:
                        self.rect.top = sprite.rect.bottom
                    # bottom
                    if self.rect.bottom >= sprite.rect.top and self.oldRect.bottom <= sprite.oldRect.top:
                        self.rect.bottom = sprite.rect.top
        

    def update(self, deltaTime):
        self.oldRect = self.rect.copy()
        self.input(deltaTime)
        self.move(deltaTime)