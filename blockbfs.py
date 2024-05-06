
from collections import deque
import copy

def is_goal_state(current_state, goal_state):
    return current_state == goal_state

def generate_possible_moves(current_state):
    moves = []
    num_stacks = len(current_state)
    
    # Generate all possible moves of taking the top block from one stack
    # and placing it on another stack
    for i in range(num_stacks):
        if current_state[i]:  # There is at least one block in this stack
            for j in range(num_stacks):
                if i != j:  # Cannot move a block onto the same stack
                    new_state = copy.deepcopy(current_state)
                    block = new_state[i].pop()
                    new_state[j].append(block)
                    moves.append(new_state)
    
    return moves

def bfs(initial_state, goal_state):
    queue = deque([(initial_state, [])])  # Each element is a tuple (state, path)
    seen_states = set()
    seen_states.add(tuple(map(tuple, initial_state)))  # Store states as tuples of tuples for immutability

    while queue:
        current_state, path = queue.popleft()
        
        if is_goal_state(current_state, goal_state):
            return path + [current_state]

        for next_state in generate_possible_moves(current_state):
            state_tuple = tuple(map(tuple, next_state))
            if state_tuple not in seen_states:
                seen_states.add(state_tuple)
                queue.append((next_state, path + [current_state]))

    return None  # Return None if no solution found

def main():
    initial_state = [['A', 'B'], ['C'], []]  # Example initial configuration
    goal_state = [['A'], ['B'], ['C']]  # Example goal configuration

    solution_path = bfs(initial_state, goal_state)
    if solution_path:
        for state in solution_path:
            print(state)
            print("->")
        print("Goal reached!")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
