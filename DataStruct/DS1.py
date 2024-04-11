### Vertical horizon (15 points) ###

def solve(array):
    
    solution = []
    
    for x in range(0, len(array[0])):
        
        solution.append([])
        
        for y in range(0, len(array)):
            
            if (len(solution[x]) == y):
                solution[x].append(y)

            solution[x][y] = array[y][x]
        
    return solution
    
    pass

