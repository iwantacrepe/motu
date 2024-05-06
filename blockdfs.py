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

def dfs(current_state, goal_state, path, seen_states):
    if is_goal_state(current_state, goal_state):
        return path + [current_state]
    
    seen_states.add(tuple(map(tuple, current_state)))  # Mark this state as seen
    
    for next_state in generate_possible_moves(current_state):
        state_tuple = tuple(map(tuple, next_state))
        if state_tuple not in seen_states:
            result = dfs(next_state, goal_state, path + [current_state], seen_states)
            if result:
                return result
    
    return None  # No solution found from this state

def main():
    initial_state = [['A', 'B'], ['C'], []]  # Example initial configuration
    goal_state = [['A'], ['B'], ['C']]  # Example goal configuration

    seen_states = set()
    solution_path = dfs(initial_state, goal_state, [], seen_states)
    if solution_path:
        for state in solution_path:
            print(state)
            print("->")
        print("Goal reached!")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
