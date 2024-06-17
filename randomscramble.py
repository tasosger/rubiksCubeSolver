import random
from rubiksCubeSolver import RubiksCube

def generate_random_scramble(length=20):
    moves = ["U", "U'", "D", "D'", "R", "R'", "L", "L'", "F", "F'", "B", "B'"]
    scramble = [random.choice(moves) for _ in range(length)]
    return " ".join(scramble)

def scramble_to_state(scramble):
    cube = RubiksCube()
    state = cube.solved_state
    moves = scramble.split()

    for move in moves:
        state = cube.apply_move(state, move)

    return state


