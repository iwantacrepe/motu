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
    open  = []
    closed = []
    initial_state = [
        [2,0,3],
        [1,8,4],
        [7,6,5]
        ]
    
    goal = [
        [1,2,3],
        [8,0,4],
        [7,6,5]
    ]


    open.insert(0,initial_state)

    while(len(open)!=0):
        
        current_state = open.pop(0)

        closed.append(current_state)

        if goal==current_state:
            break
        
        else:
                (row,column) = blank(current_state)

                if column!=0:
                    state3 = move_left(current_state,row,column)
                    if state3 not in closed and state3 not in open:
                        open.insert(0,state3)
                
                if column!=len(current_state[0])-1:
                    state4 = move_right(current_state,row,column)
                    if state4 not in closed and state4 not in open:
                        open.insert(0,state4)

                if row!=0:
                    state1 = move_up(current_state,row,column)
                    if state1 not in closed and state1 not in open:
                        open.insert(0,state1)

                if row!=len(current_state)-1:
                    state2 = move_down(current_state,row,column)
                    if state2 not in closed and state2 not in open:
                        open.insert(0,state2)

          
    print(closed)


if __name__ == "__main__":
      main()
