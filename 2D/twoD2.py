### 2D2 Connect the dots (30 points) ###

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
    for line in board:
        for el in line:
            print(el, end=' ')
        print()
