import pygame
from setting import CELL_SIZE, SNAKE_COLOR, SNAKE_HEAD_COLOR, RIGHT, GRID_SIZE


class Snake:
    def __init__(self, start_cell=(10, 10), length=1):
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.pending_growth = 0
        self.body = [
            (start_cell[0] - i, start_cell[1])
            for i in range(length)
        ]

    @property
    def head(self):
        return self.body[0]

    def grow(self, amount=1):
        self.pending_growth += amount

    def move(self):
        self.direction = self.next_direction
        head_col, head_row = self.head
        dx, dy = self.direction
        self.body.insert(0, (head_col + dx, head_row + dy))

        if self.pending_growth > 0:
            self.pending_growth -= 1
        else:
            self.body.pop()

    def draw(self, surface):
        for index, (col, row) in enumerate(self.body):
            color = SNAKE_HEAD_COLOR if index == 0 else SNAKE_COLOR
            rect = pygame.Rect(
                col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE
            )
            pygame.draw.rect(surface, color, rect)

    def set_direction(self, new_direction):
        dx, dy = self.direction
        new_dx, new_dy = new_direction
        is_reverse = (dx + new_dx, dy + new_dy) == (0, 0)
        if not is_reverse:
            self.next_direction = new_direction

    def hits_wall(self):
        col, row = self.head
        return not (0 <= col < GRID_SIZE and 0 <= row < GRID_SIZE)

    def hits_itself(self):
        return self.head in self.body[1:]

    def is_move_safe(self, direction):
        dx, dy = direction
        cur_dx, cur_dy = self.direction
        if (dx + cur_dx, dy + cur_dy) == (0, 0):
            return False

        col, row = self.head
        next_cell = (col + dx, row + dy)

        if not (0 <= next_cell[0] < GRID_SIZE and 0 <= next_cell[1] < GRID_SIZE):
            return False

        blocking_cells = self.body if self.pending_growth > 0 else self.body[:-1]
        return next_cell not in blocking_cells