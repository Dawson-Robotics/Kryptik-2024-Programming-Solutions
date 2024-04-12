### 2D2 Connect the dots (30 points) ###
import re

# IZZYS SUFF EXPLANATION
# convert strings, 1 if theres a queeen 0 if theres none
# array = [[1, 0, 0, 0, 1],
#  [0, 1, 0, 0, 0]]

# Get the x y of each thing, and if its a queen add the coord to a list
# for x in range(0, len(array)):
#     for y in range(0, len(array[x])):
#         x, y
# compare the coords ! 
# list = [[0,0], [4,0]]
# def diagonal(coord, coord2):
#     return coord[0] - coord2[0] == coord[1] == coord2[1]



def solve(board):
    pass



### helper function to visualize the board ###
def print_board(board):
    coordinates=[]
    for line in board:
        row = []
        for el in line:
            if(el == 'x'):
                row.append(1)
            else:
                row.append(0)
            #print(el, end=' ')
        coordinates.append(row)
    print()
    
    queen_locations=[]
    for x in range(0, len(coordinates)):
        for y in range(0, len(coordinates[x])):
            if coordinates[x][y] == 1:
                location=[x,y]
                queen_locations.append(location)
    for i in range(0, len(queen_locations)):
        for j in range(0, len(queen_locations)-i-1):
            if (queen_locations[j][1] > queen_locations[j + 1][1]):
                tempo = queen_locations[j]
                queen_locations[j] = queen_locations[j + 1]
                queen_locations[j + 1] = tempo
    
    for queen in queen_locations:
        index = queen_locations.index(queen)
        for others in queen_locations[index:]:
            if others[0] == queen[0]: 
                if(others[1]-queen[1] < 0):
                    current= [x+1 for x in queen]
                    target= others
                    while(current != target):
                        coordinates[current[0]][current[1]] = 2
            elif others[1] == queen[1]:
                #on top of each other
                pass
            elif diagonal(others, queen):
                print("hi")
                slope_value= slope(others, queen)
                if(slope_value < 0):
                    current=[x-1 for x in others]
                    target= queen
                    while(current != target):
                        coordinates[current[0]][current[1]] = 3
                        current = [x-1 for x in current]
                elif (slope_value > 0):
                    current=[x+1 for x in queen]
                    target= others
                    while(current != target):
                        coordinates[current[0]][current[1]] = 4
                        current = [x+1 for x in current]
    for coords in coordinates:
        print(coords)

def diagonal(coord, coord2):
    val1= coord[0] - coord2[0]
    val2= coord[1] - coord2[1]
    print(f"{val1} and {val2}")
    return coord[0] - coord2[0] == coord[1] - coord2[1]

def slope(coord, coord2):
    return(coord2[1]-coord[1])/(coord2[0]-coord[0])


print_board([
        ".x...x..",
        "........",
        ".x.x....",
        "........",
        "...x....",
        "........",
        "........",
        "........"])