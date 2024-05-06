
import copy

def blank(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return (i, j)

def move_up(current_state, row, column):
    if row > 0:
        state = copy.deepcopy(current_state)
        state[row][column], state[row-1][column] = state[row-1][column], state[row][column]
        return state
    return None

def move_down(current_state, row, column):
    if row < len(current_state) - 1:
        state = copy.deepcopy(current_state)
        state[row][column], state[row+1][column] = state[row+1][column], state[row][column]
        return state
    return None

def move_left(current_state, row, column):
    if column > 0:
        state = copy.deepcopy(current_state)
        state[row][column], state[row][column-1] = state[row][column-1], state[row][column]
        return state
    return None

def move_right(current_state, row, column):
    if column < len(current_state[0]) - 1:
        state = copy.deepcopy(current_state)
        state[row][column], state[row][column+1] = state[row][column+1], state[row][column]
        return state
    return None

def dls(current_state, goal, depth):
    if depth == 0 and current_state == goal:
        return (True, [current_state])
    elif depth > 0:
        (row, column) = blank(current_state)
        neighbors = [
            move_up(current_state, row, column),
            move_down(current_state, row, column),
            move_left(current_state, row, column),
            move_right(current_state, row, column)
        ]
        for neighbor in filter(None, neighbors):
            found, path = dls(neighbor, goal, depth - 1)
            if found:
                return (True, [current_state] + path)
    return (False, [])

def iddfs(initial_state, goal):
    depth = 0
    while True:
        found, path = dls(initial_state, goal, depth)
        if found:
            return path
        depth += 1

def main():
    initial_state = [
        [2, 0, 3],
        [1, 8, 4],
        [7, 6, 5]
    ]
    goal = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]
    solution_path = iddfs(initial_state, goal)
    for state in solution_path:
        for row in state:
            print(row)
        print("->")
    print("Goal reached!")

if __name__ == "__main__":
    main()
