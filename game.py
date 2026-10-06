import pygame
from pygame import Surface
from snake import Snake
from fruit import Fruit
from setting import (
    CELL_SIZE, GRID_SIZE, UP, DOWN, LEFT, RIGHT,
    OVERLAY_COLOR, GAME_OVER_TEXT_COLOR,
    SCORE_COLOR, SCORE_MARGIN,
    BOARD_DARK_COLOR, BOARD_LIGHT_COLOR, LIGHT_BROWN_COLOR
)

KEY_TO_DIRECTION = {
    pygame.K_UP: UP,
    pygame.K_DOWN: DOWN,
    pygame.K_LEFT: LEFT,
    pygame.K_RIGHT: RIGHT,
}
from snake_ai import SnakeAI


class Game:
    def __init__(self, screen: Surface, mode="manual"):
        self.mode = mode
        self.ai = SnakeAI() if mode == "ai" else None
        self.screen = screen
        self.snake = Snake(length=1)
        self.fruit = Fruit(self.snake.body)
        self.score = 0
        self.game_over = False
        self.title_font = pygame.font.SysFont("Arial", 52, bold=True)
        self.hint_font = pygame.font.SysFont("Arial", 24)
        self.score_font = pygame.font.SysFont("Arial", 28, bold=True)

    def draw_board(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                color = BOARD_LIGHT_COLOR if (row + col) % 2 == 0 else BOARD_DARK_COLOR

                pygame.draw.rect(
                    self.screen,
                    color,
                    (
                        col * CELL_SIZE,
                        row * CELL_SIZE,
                        CELL_SIZE,
                        CELL_SIZE
                    )
                )

    def handle_key(self, key):
        if self.mode != "manual":
            return
        direction = KEY_TO_DIRECTION.get(key)
        if direction is not None:
            self.snake.set_direction(direction)

    def draw(self):
        self.screen.fill(LIGHT_BROWN_COLOR)
        self.fruit.draw(self.screen)
        self.snake.draw(self.screen)
        self.draw_score()
        if self.game_over:
            self.draw_game_over()

    def draw_score(self):
        text = self.score_font.render(f"Score: {self.score}", True, SCORE_COLOR)
        self.screen.blit(text, (SCORE_MARGIN, SCORE_MARGIN))

    def update(self):
        if self.game_over:
            return

        if self.ai is not None:
            direction = self.ai.choose_direction(self.snake, self.fruit.cell)
            self.snake.set_direction(direction)

        self.snake.move()

        if self.snake.hits_wall() or self.snake.hits_itself():
            self.game_over = True
            return

        if self.snake.head == self.fruit.cell:
            self.snake.grow()
            self.fruit.respawn(self.snake.body)
            self.score += 1

    def draw_game_over(self):
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill(OVERLAY_COLOR)
        self.screen.blit(overlay, (0, 0))

        center_x, center_y = self.screen.get_rect().center
        lines = [
            (self.title_font, "GAME OVER", -50),
            (self.hint_font, f"Score: {self.score}", 10),
            (self.hint_font, "R: restart   ESC: menu", 50),
        ]
        for font, text, offset in lines:
            surface = font.render(text, True, GAME_OVER_TEXT_COLOR)
            rect = surface.get_rect(center=(center_x, center_y + offset))
            self.screen.blit(surface, rect)
