import tensorflow as tf
import numpy as np
from setting import UP, DOWN, LEFT, RIGHT
from features import extract_features

class SnakeML:
    def __init__(self):
        self.model = tf.keras.models.load_model(
            'sajjad_saljoughi_snake_ml.h5',
            custom_objects={
                'softmax_v2': tf.nn.softmax
            }
        )

    def choose_direction(self, snake, fruit_cell):
        result = None
        features = extract_features(snake, fruit_cell)
        data = np.array(features,dtype=np.float32)
        data = data.reshape(1, 6)
        direction = self.model.predict(data)
        direction = np.argmax(direction)
        if direction == 0:
            result = RIGHT
        elif direction == 1:
            result = DOWN
        elif direction == 2:
            result = LEFT
        elif direction == 3:
            result = UP
        return result



