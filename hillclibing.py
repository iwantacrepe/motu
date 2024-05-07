import copy

def calculate_heuristic(state):
    goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    misplaced = sum(1 for i in range(3) for j in range(3) if state[i][j] != goal_state[i][j] and state[i][j] != 0)
    return misplaced

def blank(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return (i, j)

def move_up(state, row, column):
    new_state = copy.deepcopy(state)
    new_state[row][column], new_state[row-1][column] = new_state[row-1][column], new_state[row][column]
    return new_state

def move_down(state, row, column):
    new_state = copy.deepcopy(state)
    new_state[row][column], new_state[row+1][column] = new_state[row+1][column], new_state[row][column]
    return new_state

def move_left(state, row, column):
    new_state = copy.deepcopy(state)
    new_state[row][column], new_state[row][column-1] = new_state[row][column-1], new_state[row][column]
    return new_state

def move_right(state, row, column):
    new_state = copy.deepcopy(state)
    new_state[row][column], new_state[row][column+1] = new_state[row][column+1], new_state[row][column]
    return new_state

def bfs_solver(initial_state):
    queue = [initial_state]
    closed = set()
    parent_map = {tuple(map(tuple, initial_state)): None}
    goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    while queue:
        current_state = queue.pop(0)
        state_tuple = tuple(map(tuple, current_state))
        if state_tuple in closed:
            continue
        closed.add(state_tuple)

        if current_state == goal_state:
            return reconstruct_path(current_state, parent_map)

        row, column = blank(current_state)
        if row > 0:
            add_to_queue(parent_map, queue, move_up(current_state, row, column), current_state)
        if row < 2:
            add_to_queue(parent_map, queue, move_down(current_state, row, column), current_state)
        if column > 0:
            add_to_queue(parent_map, queue, move_left(current_state, row, column), current_state)
        if column < 2:
            add_to_queue(parent_map, queue, move_right(current_state, row, column), current_state)

    return False  # No solution found

def add_to_queue(parent_map, queue, new_state, current_state):
    new_state_tuple = tuple(map(tuple, new_state))
    if new_state_tuple not in parent_map:
        parent_map[new_state_tuple] = current_state
        queue.append(new_state)

def reconstruct_path(state, parent_map):
    path = []
    while state:
        path.append(state)
        state = parent_map[tuple(map(tuple, state))]
    return path[::-1]

def print_solution(solution):
    if solution:
        for state in solution:
            for row in state:
                print(row)
            print()
    else:
        print("No solution found")

initial_state = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
solution = bfs_solver(initial_state)
print_solution(solution)
