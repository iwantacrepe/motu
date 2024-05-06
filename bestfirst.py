import copy
import heapq

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

def manhattan_distance(state, goal):
    distance = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            num = state[i][j]
            if num != 0:
                for x in range(len(goal)):
                    for y in range(len(goal[0])):
                        if goal[x][y] == num:
                            distance += abs(x - i) + abs(y - j)
                            break
    return distance

def best_first_search(initial_state, goal):
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(initial_state, goal), initial_state, []))
    seen_states = set()

    while open_list:
        current_h, current_state, path = heapq.heappop(open_list)
        if current_state == goal:
            return path + [current_state]

        seen_states.add(tuple(map(tuple, current_state)))

        (row, column) = blank(current_state)
        neighbors = [
            move_up(current_state, row, column),
            move_down(current_state, row, column),
            move_left(current_state, row, column),
            move_right(current_state, row, column)
        ]

        for neighbor in filter(None, neighbors):
            if tuple(map(tuple, neighbor)) not in seen_states:
                h = manhattan_distance(neighbor, goal)
                heapq.heappush(open_list, (h, neighbor, path + [current_state]))

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
    solution_path = best_first_search(initial_state, goal)
    for state in solution_path:
        for row in state:
            print(row)
        print("->")
    print("Goal reached!")

if __name__ == "__main__":
    main()
