import random 
from components.obstacle.obstacle import Obstacle

class SmallCactus(Obstacle):
    def __init__(self, image):
        self.index = random.randint(0,2)
        super().__init__(image, self.index)
        self.rect.y = 320

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.index = random.randint(0,2)
        super().__init__(image, self.index)
        self.rect.y = 295

class Bird_low(Obstacle):
    def __init__(self, image):
        self.index = 0
        super().__init__(image, self.index)
        self.rect.y = 260
        self.type = 0

    def draw(self, screen):
        if self.type >= 9:
            self.type = 0
        screen.blit(self.image[self.type // 5], self.rect)
        self.type +=1

class Bird_high(Obstacle):
    def __init__(self, image):
        self.index = 0
        super().__init__(image, self.index)
        self.rect.y = 230
        self.type = 0

    def draw(self, screen):
        if self.type >= 9:
            self.type = 0
        screen.blit(self.image[self.type // 5], self.rect)
        self.type +=1



        
