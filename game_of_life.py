import random

DEAD = 0
ALIVE = 1


def random_state(width, height):
    """Create a new random matrix"""
    return [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]


def render(state):
    """Show the board in a legible way"""
    height = len(state)
    for y in range(height):
        print('|', end='')
        for x in state[y]:
            if x == ALIVE:
                print("#", end='')
            else:
                print(' ', end='')
        print('|')


def render_n(state):
    for row in state:
        print(*row, sep='')


# def new_cell_state(coords, state):
#
# def new_board_state(state):
