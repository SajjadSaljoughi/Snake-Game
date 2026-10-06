from setting import GRID_SIZE, UP, DOWN, LEFT, RIGHT

ALL_DIRECTIONS = [UP, DOWN, LEFT, RIGHT]


class SnakeAI:
    def choose_direction(self, snake, fruit_cell):
        candidates = self._preferred_directions(snake.head, fruit_cell) + ALL_DIRECTIONS
        for direction in candidates:
            if self._is_safe(snake, direction):
                return direction
        return snake.direction

    @staticmethod
    def _preferred_directions(head, fruit_cell):
        head_col, head_row = head
        fruit_col, fruit_row = fruit_cell
        preferred = []

        if fruit_col > head_col:
            preferred.append(RIGHT)
        elif fruit_col < head_col:
            preferred.append(LEFT)

        if fruit_row > head_row:
            preferred.append(DOWN)
        elif fruit_row < head_row:
            preferred.append(UP)

        return preferred

    @staticmethod
    def _is_safe(snake, direction):
        dx, dy = direction
        cur_dx, cur_dy = snake.direction
        if (dx + cur_dx, dy + cur_dy) == (0, 0):
            return False

        col, row = snake.head
        next_cell = (col + dx, row + dy)

        if not (0 <= next_cell[0] < GRID_SIZE and 0 <= next_cell[1] < GRID_SIZE):
            return False

        blocking_cells = snake.body if snake.pending_growth > 0 else snake.body[:-1]
        return next_cell not in blocking_cells