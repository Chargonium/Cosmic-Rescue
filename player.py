from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups) -> None:
        super().__init__(groups)
        self.image = pygame.Surface((48, 56))
        self.image.fill('red')
        self.rect = self.image.get_frect(topleft=pos)
        
        self.direction = Vector(0, 0)
        self.speed = 200

    def input(self):
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

        self.direction = input_vector.normalize() if input_vector else input_vector

    def move(self, deltaTime):
        newPosition = Vector(self.rect.topleft)

        newPosition.x += self.direction.x * self.speed * deltaTime

        newPosition.y += self.direction.y * self.speed * deltaTime

        self.rect.topleft = newPosition
        

    def update(self, deltaTime):
        self.input()
        self.move(deltaTime)