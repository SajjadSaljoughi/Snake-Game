import pygame

class Fruit(pygame.sprite.Sprite):
    def __init__(self,width = 32,height = 32,
                 center_x = 0,center_y = 0,
                 color = (0,0,0),radius = 16):
        super().__init__()
        self.width = width
        self.height = height
        self.center_x = center_x
        self.center_y = center_y
        self.color = color
        self.radius = radius
        self.rect = pygame.Rect(self.center_x - self.radius,
                                self.center_y - self.radius,
                                self.width, self.height)
        
    def draw(self,main):
        pygame.draw.circle(main,self.color,
                           (self.center_x, self.center_y)
                           ,self.radius)