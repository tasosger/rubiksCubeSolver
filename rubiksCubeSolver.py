from collections import deque


class RubiksCube:
    def __init__(self):
        
        self.solved_state = (
            ('W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'),  # Up face
            ('R', 'R', 'R', 'R', 'R', 'R', 'R', 'R', 'R'),  # Right face
            ('B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'),  # Front face
            ('O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'),  # Left face
            ('G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G'),  # Back face
            ('Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y')   # Down face
        )


    def rotate_face_clockwise(self, face):
        # Rotate a given face clockwise
        return [
            face[6], face[3], face[0],
            face[7], face[4], face[1],
            face[8], face[5], face[2]
        ]

    def rotate_face_counterclockwise(self, face):
        # Rotate a given face counterclockwise
        return [
            face[2], face[5], face[8],
            face[1], face[4], face[7],
            face[0], face[3], face[6]
        ]

    def apply_move(self, state, move):
        # Apply a move to the state and return the new state
        state = list(map(list, state))  # Convert each face from str to list
        
        if move == "U":
            state = self.rotate_U(state)
        elif move == "U'":
            state = self.rotate_U_prime(state)
        elif move == "D":
            state = self.rotate_D(state)
        elif move == "D'":
            state = self.rotate_D_prime(state)
        elif move == "R":
            state = self.rotate_R(state)
        elif move == "R'":
            state = self.rotate_R_prime(state)
        elif move == "L":
            state = self.rotate_L(state)
        elif move == "L'":
            state = self.rotate_L_prime(state)
        elif move == "F":
            state = self.rotate_F(state)
        elif move == "F'":
            state = self.rotate_F_prime(state)
        elif move == "B":
            state = self.rotate_B(state)
        elif move == "B'":
            state = self.rotate_B_prime(state)

        return tuple(map(tuple, state))  # Convert back to tuple of tuples

    def rotate_U(self, state):
        # Rotate the upper face clockwise
        state[0] = self.rotate_face_clockwise(state[0])
        state[1][0:3], state[2][0:3], state[3][0:3], state[4][0:3] = \
            state[2][0:3], state[3][0:3], state[4][0:3], state[1][0:3]
        return state

    def rotate_U_prime(self, state):
        # Rotate the upper face counterclockwise
        state[0] = self.rotate_face_counterclockwise(state[0])
        state[1][0:3], state[2][0:3], state[3][0:3], state[4][0:3] = \
            state[4][0:3], state[1][0:3], state[2][0:3], state[3][0:3]
        return state

    def rotate_D(self, state):
        # Rotate the down face clockwise
        state[5] = self.rotate_face_clockwise(state[5])
        state[1][6:9], state[2][6:9], state[3][6:9], state[4][6:9] = \
            state[4][6:9], state[1][6:9], state[2][6:9], state[3][6:9]
        return state

    def rotate_D_prime(self, state):
        # Rotate the down face counterclockwise
        state[5] = self.rotate_face_counterclockwise(state[5])
        state[1][6:9], state[2][6:9], state[3][6:9], state[4][6:9] = \
            state[2][6:9], state[3][6:9], state[4][6:9], state[1][6:9]
        return state

    def rotate_R(self, state):
        # Rotate the right face clockwise
        state[1] = self.rotate_face_clockwise(state[1])
        state[0][2::3], state[2][2::3], state[5][2::3], state[4][2::3] = \
            state[2][2::3], state[5][2::3], state[4][2::3], state[0][2::3]
        return state

    def rotate_R_prime(self, state):
        # Rotate the right face counterclockwise
        state[1] = self.rotate_face_counterclockwise(state[1])
        state[0][2::3], state[2][2::3], state[5][2::3], state[4][2::3] = \
            state[4][2::3], state[0][2::3], state[2][2::3], state[5][2::3]
        return state

    def rotate_L(self, state):
        # Rotate the left face clockwise
        state[3] = self.rotate_face_clockwise(state[3])
        state[0][0::3], state[4][0::3], state[5][0::3], state[2][0::3] = \
            state[4][0::3], state[5][0::3], state[2][0::3], state[0][0::3]
        return state

    def rotate_L_prime(self, state):
        # Rotate the left face counterclockwise
        state[3] = self.rotate_face_counterclockwise(state[3])
        state[0][0::3], state[4][0::3], state[5][0::3], state[2][0::3] = \
            state[2][0::3], state[0][0::3], state[4][0::3], state[5][0::3]
        return state

    def rotate_F(self, state):
        # Rotate the front face clockwise
        state[2] = self.rotate_face_clockwise(state[2])
        state[0][6:9], state[1][0::3], state[5][0:3], state[3][2::3] = \
            state[3][2::3][::-1], state[0][6:9][::-1], state[1][0::3], state[5][0:3]
        return state

    def rotate_F_prime(self, state):
        # Rotate the front face counterclockwise
        state[2] = self.rotate_face_counterclockwise(state[2])
        state[0][6:9], state[1][0::3], state[5][0:3], state[3][2::3] = \
            state[1][0::3][::-1], state[5][0:3], state[3][2::3][::-1], state[0][6:9]
        return state

    def rotate_B(self, state):
        # Rotate the back face clockwise
        state[4] = self.rotate_face_clockwise(state[4])
        state[0][0:3], state[1][2::3], state[5][6:9], state[3][0::3] = \
            state[1][2::3][::-1], state[5][6:9], state[3][0::3][::-1], state[0][0:3]
        return state

    def rotate_B_prime(self, state):
        # Rotate the back face counterclockwise
        state[4] = self.rotate_face_counterclockwise(state[4])
        state[0][0:3], state[1][2::3], state[5][6:9], state[3][0::3] = \
            state[3][0::3], state[0][0:3][::-1], state[1][2::3], state[5][6:9][::-1]
        return state

    def generate_moves(self, state):
        
        moves = []
        for move in ['U', 'U\'', 'D', 'D\'', 'R', 'R\'', 'L', 'L\'', 'F', 'F\'', 'B', 'B\'']:
            new_state = self.apply_move(state, move)
            moves.append((new_state, move))
        return moves

    def is_solved(self, state):
        
        return state == self.solved_state

def bfs_solve(scrambled_state):
    
    cube = RubiksCube()
    queue = deque([(scrambled_state, [])])
    visited = set()

    while queue:
        

        current_state, path = queue.popleft()
        
        if cube.is_solved(current_state):
            return path

        if current_state in visited:

            continue
        visited.add(current_state)
        #print(current_state)
        for next_state, move in cube.generate_moves(current_state):
            if next_state not in visited:
                
                queue.append((next_state, path + [move]))
                
        
        

    return None


def scramble_to_state(scramble):
    cube = RubiksCube()
    state = cube.solved_state
    moves = scramble.split()

    for move in moves:
        state = cube.apply_move(state, move)

    return state


scramble = "R U R' U'"
scrambled_state = scramble_to_state(scramble)




solution = bfs_solve(scrambled_state)
print("Solution:", solution)
print("moves: ",len(solution))