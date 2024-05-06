import copy
def blank(start):
    for i in range(len(start)):
        for j in range(len(start[0])):
            if start[i][j]==0:
                return (i,j)

def move_up(current_state,row,column):
    
        start=copy.deepcopy(current_state)
        start[row][column],start[row-1][column] = start[row-1][column],start[row][column]
        return start
    
def move_down(current_state,row,column):
    
        start=copy.deepcopy(current_state)
        start[row][column],start[row+1][column] = start[row+1][column],start[row][column]
        return start
    
def move_left(current_state,row,column):
    
        start=copy.deepcopy(current_state)
        start[row][column],start[row][column-1] = start[row][column-1],start[row][column]
        return start
    
def move_right(current_state,row,column):
    
        start=copy.deepcopy(current_state)
        start[row][column],start[row][column+1] = start[row][column+1],start[row][column]
        return start
    

def main():
    print("hello")
    start = [[2,0,3],
            [1,8,4],
            [7,6,5]]
    goal = [[1,2,3],
     [8,0,4],
     [7,6,5]]
    
    queue = []
    closed = []

    search = 0

    # add the initial node to the queue

    queue.append(start)

    #  jab tak queue khaali nhi hoti
 
    while(len(queue)!=0):
        current_state = queue.pop(0)
        print(current_state)
        # this is our current state 

        # adding it to the closed list
        closed.append(current_state)
        

        # checking if our current state is the goal node or not

        # if goal node return success and break loop

        if current_state==goal:
            # return True
            search = 1
            break

        # elif current_state==None:
        #     continue

        else:
            # since our current_state was not the goal node
            # we will generate all the possible states 
            # and then add them to the queue
                
            
                (row,column) = blank(current_state)

                if column!=0:
                    state3 = move_left(current_state,row,column)
                    if state3 not in closed and state3 not in queue:
                        queue.append(state3)
                
                if column!=len(start[0])-1:
                    state4 = move_right(current_state,row,column)
                    if state4 not in closed and state4 not in queue:
                        queue.append(state4)

                if row!=0:
                    state1 = move_up(current_state,row,column)
                    if state1 not in closed and state1 not in queue:
                        queue.append(state1)

                if row!=len(start)-1:
                    state2 = move_down(current_state,row,column)
                    if state2 not in closed and state2 not in queue:
                        queue.append(state2)

            
    print(search)
    print(closed)


if __name__ == "__main__":
    main()




