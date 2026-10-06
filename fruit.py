import random
import pygame
from setting import CELL_SIZE, GRID_SIZE, FRUIT_COLOR


class Fruit:
    def __init__(self, occupied_cells):
        self.cell = self._pick_free_cell(occupied_cells)

    def respawn(self, occupied_cells):
        self.cell = self._pick_free_cell(occupied_cells)

    def draw(self, surface):
        col, row = self.cell
        rect = pygame.Rect(
            col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE
        )
        pygame.draw.rect(surface, FRUIT_COLOR, rect)

    @staticmethod
    def _pick_free_cell(occupied_cells):
        all_cells = {
            (col, row)
            for col in range(GRID_SIZE)
            for row in range(GRID_SIZE)
        }
        free_cells = all_cells - set(occupied_cells)
        return random.choice(list(free_cells))