import pygame

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.font = pygame.font.SysFont("Arial", 28, bold=True)
        self.title_font = pygame.font.SysFont(
            "Arial", 52, bold=True
        )
        self.options = [
            ("Start Manual Game", "manual"),
            ("Start AI Snake", "ai"),
            ("Start ML Snake", "ml")
        ]
        self.option_rects = []
        self.selected = 0
        self.result = None
        self.bg_color = (210, 180, 140)
        self.text_color = (40, 30, 20)
        self.selected_color = (0, 100, 180)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected = (
                        self.selected - 1
                    ) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected = (
                        self.selected + 1
                    ) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    return self.options[self.selected][1]
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i, rect in enumerate(self.option_rects):
                        if rect.collidepoint(event.pos):
                            self.selected = i
                            return self.options[i][1]
        return None

    def draw(self):
        self.screen.fill(self.bg_color)
        title = self.title_font.render(
            "SNAKE GAME", True, self.text_color
        )
        self.screen.blit(
            title,
            title.get_rect(
                center=(self.width // 2, 130)
            )
        )

        for i, (label, value) in enumerate(self.options):
            y = 250 + i * 85

            rect = pygame.Rect(
                self.width // 2 - 190,
                y - 28,
                380,
                60
            )
            self.option_rects.append(rect)
            color = (
                self.selected_color
                if i == self.selected
                else self.text_color
            )
            if i == self.selected:
                pygame.draw.rect(
                    self.screen,
                    (245, 220, 180),
                    rect,
                    border_radius=10
                )
            text = self.font.render(label, True, color)
            self.screen.blit(
                text,
                text.get_rect(center=rect.center)
            )
