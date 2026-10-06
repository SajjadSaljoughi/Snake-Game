from menu import Menu
from game import Game
from setting import *

class Main:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.mode = ""
        self.state = "menu"
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(MOVE_EVENT, MOVE_INTERVAL_MS)
        self.menu = Menu(self.screen)
        self.game = Game(self.screen)

    def handle_events(self):
        if self.state == "menu":
            result = self.menu.handle_events()
            if result == "quit":
                self.running = False
            elif result in ("manual", "ai", "ml"):
                self.mode = result
                self.game = Game(self.screen, self.mode)
                self.state = "game"
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == MOVE_EVENT:
                    self.game.update()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.state = "menu"
                    elif event.key == pygame.K_r:
                        self.game = Game(self.screen, self.mode)
                        self.state = "game"
                    else:
                        self.game.handle_key(event.key)

    def update(self):
        ...

    def draw(self):
        if self.state == "menu":
            self.menu.draw()
        else:
            self.game.draw()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)


if __name__ == "__main__":
    game = Main(640, 640)
    game.run()
    pygame.quit()
