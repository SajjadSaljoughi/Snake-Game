import pygame
from color import Color

class Snake(pygame.sprite.Sprite):
    def __init__(self,width = 32,height = 32,
                 center_x = 0,center_y = 0,
                 color = (0,0,0)):
        super().__init__()
        self.width = width
        self.height = height
        self.center_x = center_x
        self.center_y = center_y
        self.color = color
        self.speed = 4
        self.direction = ""
        self.rect = pygame.Rect(self.center_x, self.center_y,
                             self.width, self.height)
        self.score = 0
        self.body = []

    def move(self):
        self.body.append({"x" : self.center_x,"y" : self.center_y})
        if len(self.body) > self.score / 10:
            self.body.pop(0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = "l"
        if keys[pygame.K_RIGHT]:
            self.direction = "r"
        if keys[pygame.K_UP]:
            self.direction = "u"
        if keys[pygame.K_DOWN]:
            self.direction = "d"

        
        if self.direction == "l":
            self.center_x -= self.speed
        elif self.direction == "r":
            self.center_x += self.speed
        elif self.direction == "d":
            self.center_y += self.speed
        elif self.direction == "u":
            self.center_y -= self.speed


        self.rect.topleft = (self.center_x, self.center_y)
    
    def eat(self,food):
        self.score += 10
        del food
        

    def check_wall(self,main):
        for part in self.body:
            if 0 > part['x']:
                self.center_x = 0
                return True
            elif part['x'] >= main.width - 32:
                self.center_x = main.width - self.width
                return True
            elif part['y'] < 0:
                self.center_y = 0
                return True
            elif part['y'] >= main.height - 32:
                self.center_y = main.height - self.width
                return True
            else:
                return False

    def draw(self,main):
        pygame.draw.rect(main,self.color,
                           self.rect)
        for part in self.body:
            pygame.draw.rect(main,self.color,
                           pygame.Rect(part['x'],part['y'],
                                       self.width,self.height))