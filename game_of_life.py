import random

DEAD = 0
ALIVE = 1

# randomizer = random.choice([0, 1])


def random_state(width, height):
    return [[random.randint(0, 1) for i in range(width)] for i in range(height)]
