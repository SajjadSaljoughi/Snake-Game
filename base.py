import pygame

class Base:
    def __init__(self, width=600, height=600, title="My Game"):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = True
        self.bg_color = (0, 0, 0)

    def show_text(self,font,text):
        text_font = font.render(text,True,(0,0,0))
        self.screen.blit(text_font , (10,10))
        
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass  

    def draw(self):
        self.screen.fill(self.bg_color)


# # کلاس اصلی که از BaseGame ارث‌بری می‌کنه
# class MyGame(BaseGame):
#     def __init__(self, width, height, title="My Pygame"):
#         super().__init__(width, height, title)
#         self.x = 100
#         self.y = 100

#     def update(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_RIGHT]:
#             self.x += 5
#         if keys[pygame.K_LEFT]:
#             self.x -= 5

#     def draw(self):
#         self.screen.fill((50, 50, 80))  # پس‌زمینه
#         pygame.draw.circle(self.screen, (255, 0, 0), (self.x, self.y), 30)


# if __name__ == "__main__":
#     game = MyGame(800, 600, "Arcade Style in Pygame")
#     game.run()
#     pygame.quit()
#     sys.exit()
