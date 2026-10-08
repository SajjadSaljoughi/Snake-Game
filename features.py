import numpy as np
from setting import UP, DOWN, LEFT, RIGHT

DIRECTION_ORDER = [RIGHT, DOWN, LEFT, UP]   #r=0, d=1, l=2, u=3

def extract_features(snake, fruit_cell):
    head_col, head_row = snake.head
    fruit_col, fruit_row = fruit_cell
    danger = [0 if snake.is_move_safe(d) else 1 for d in DIRECTION_ORDER]
    return [
        int(np.sign(fruit_col - head_col)),
        int(np.sign(fruit_row - head_row)),
        *danger,
    ]