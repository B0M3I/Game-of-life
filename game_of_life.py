import random

DEAD = 0
ALIVE = 1


def dead_state(width, height):
    """Create a new matrix filled with zeros."""
    return [[DEAD for _ in range(width)] for _ in range(height)]


def random_state(width, height):
    """Create a new random matrix."""
    return [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]


def render(state):
    """Show the board in a legible way."""
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


def new_cell_value(coords, state):
    """Get the new value of a cell in a state."""
    width = len(state)
    height = len(state[0])
    x = coords[0]
    y = coords[1]
    n_live_neighbors = 0

    # Iterate around this cell's neighbors
    for x1 in range((x - 1), (x + 1) + 1):
        # Make sure we don't go off the edge of the board
        if x1 < 0 or x1 >= width:
            continue

        for y1 in range((y - 1), (y + 1) + 1):
            # Make sure it doesn't go off the edge of the board
            if y1 < 0 or y1 >= height:
                continue
            # Make sure we don't count the cell as a neighbor
            if x1 == x and y1 == y:
                continue

            if state[x1][y1] == ALIVE:
                n_live_neighbors += 1

    if state[x][y] == ALIVE:
        if n_live_neighbors <= 1:
            return DEAD
        elif n_live_neighbors <= 3:
            return ALIVE
        else:
            return DEAD
    else:
        if n_live_neighbors == 3:
            return ALIVE
        else:
            return DEAD


def new_board_state(init_state):
    """New board with new cells."""
    width = len(init_state)
    height = len(init_state[0])
    next_state = dead_state(height, width)

    for x in range(0, width):
        for y in range(0, height):
            next_state[x][y] = new_cell_value((x, y), init_state)

    return next_state


def run(init_state):
    """Runs the game."""
    next_state = init_state
    while True:
        user = input('Input q to finish or any key to continue: ')
        if user == 'q':
            break
        else:
            render(next_state)
            next_state = new_board_state(next_state)


if __name__ == "__main__":
    start = random_state(100, 50)
    run(start)
