import random
import pygame
from base import Base
from color import Color
from fruit import Fruit
from snake import Snake

class Main(Base):
    def __init__(self):
        super().__init__(600, 600, "Snake Game V1")
        self.bg_color = Color.Sandy_Brown
        self.apple = Fruit(center_x=random.randint(100,self.width),
                      center_y=random.randint(100,self.height),
                      color=Color.RED)
        self.snake = Snake(center_x=self.width // 2,
                           center_y=self.height // 2,
                           color=Color.BLUE)
        self.font = pygame.font.SysFont("Arial", 20)
        self.text = "Score = 0"

    

    def draw(self):
        super().draw()
        self.apple.draw(self.screen)
        self.snake.draw(self.screen)
        self.show_text(self.font,self.text)

    def update(self):
        
        self.snake.move()
        if self.snake.rect.colliderect(self.apple.rect):
            self.text = f"Score = {self.snake.score}"
            self.snake.eat(self.apple)
            self.apple = Fruit(center_x=random.randint(100,self.width),
                      center_y=random.randint(100,self.height),
                      color=Color.RED)
        if self.snake.check_wall(self):
            self.text = "Game Over"
            self.snake.speed = 0


game = Main()
game.run()
pygame.quit()


