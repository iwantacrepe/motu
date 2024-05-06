import heapq

def In_open(open,node):
    for i in range(0,len(open)):
        if(open[i][0]==node):
            return 1
    return 0

def In_closed(closed,node):
    for i in range(0,len(closed)):
        if(closed[i]==node):
            return 1
    return 0

def main():
    graph = [
        [0,9,4,0,0,0],
        [9,0,2,7,3,0],
        [4,2,0,1,6,0],
        [0,7,1,0,4,8],
        [0,3,6,4,0,2],
        [0,0,0,8,2,0],
    ]
    closed = []
    start = [0,0]
    # In the tuple the first value is the node and the second value is it's cost from the initial node
    goal = 5
    
    # maintaining the open list as a heap
    open = []
    # heapq.heappush(open , start)
    open.append(start)
    # print(open[0][0])
    state = True

    while(state):
        # current = heapq.heappop(open)
        current = open.pop(0)
        current_node = current[0]
        current_val = current[1]
        if(current_node == goal):
            state = False
            print(current_val)
            return
        closed.append(current_node)
        for j in range(0,len(graph[0])):
            node = j
            node_val = graph[current_node][j]
            if(node_val!=0):
                if(not In_open(open,node) and not In_closed(closed,node)):
                    # heapq.heappush(open , [node , current_val+node_val])
                    open.append([node ,current_val + node_val])
                    open = sorted(open , key = lambda x : x[1])
                if(In_open(open,node)):
                    last_cost = 0
                    last_index = 0
                    for i in range(0,len(open)):
                        if(open[i][0]==node):
                            last_cost = open[i][1]
                            last_index = i
                    new_cost = current_val + node_val
                    if(new_cost<last_cost):
                        open[last_index][1] = new_cost
                        open = sorted(open , key = lambda x : x[1])

    # ans = open[0][1]
    # print(ans)

if __name__ == "__main__":
    main()
