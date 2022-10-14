import random

DEAD = 0
ALIVE = 1


def random_state(width, height):
    return [[random.randint(0, 1) for i in range(width)] for i in range(height)]


def render(state):
    height = len(state)
    for i in range(height):
        print('|', end='')
        for number in state[i]:
            if number == ALIVE:
                print("#", end='')
            else:
                print(' ', end='')
        print('|')


def render_n(state):
    for row in state:
        print(*row)


# x = random_state(6, 4)
# render(x)
# render_n(x)
