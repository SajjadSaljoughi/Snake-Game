from features import extract_features
from setting import GRID_SIZE, UP, DOWN, LEFT, RIGHT

ALL_DIRECTIONS = [UP, DOWN, LEFT, RIGHT]


class GenerateDataset:
    def __init__(self):
        self.dataset = []

    def choose_direction(self, snake, fruit_cell):
        candidates = self._preferred_directions(snake.head, fruit_cell) + ALL_DIRECTIONS
        for direction in candidates:
            if snake.is_move_safe(direction):
                features = extract_features(snake, fruit_cell)
                y = ""
                if direction == UP:
                    y = "u"
                elif direction == DOWN:
                    y = "d"
                elif direction == LEFT:
                    y = "l"
                elif direction == RIGHT:
                    y = "r"
                features.append(y)
                self.dataset.append(features)
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
