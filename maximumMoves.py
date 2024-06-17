from rubiksCubeSolver import  bfs_solve
from randomscramble import scramble_to_state, generate_random_scramble
def find_max_moves(num_scrambles=100):
    max_moves = 0
    hardest_scramble = None

    for _ in range(num_scrambles):
        scramble = generate_random_scramble(4)
        scrambled_state = scramble_to_state(scramble)
        solution = bfs_solve(scrambled_state)
        num_moves = len(solution)

        if num_moves > max_moves:
            max_moves = num_moves
            hardest_scramble = scramble

    return max_moves, hardest_scramble

if __name__ == "__main__":
    max_moves, hardest_scramble = find_max_moves(3)
    print(f"Maximum number of moves required: {max_moves}")
    print(f"Hardest scramble: {hardest_scramble}")