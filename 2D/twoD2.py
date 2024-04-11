### 2D2 Connect the dots (30 points) ###
import re

def solve(board):
    pass



### helper function to visualize the board ###
def print_board(board):
    for line in board:
        xcounter=0
        for el in line:
            if(el == 'x'):
                xcounter= xcounter+1
            #print(el, end=' ')
        if(xcounter == 2):
            line = re.sub("^x.*x$", '-', line)
            print(line)

print_board(["x......x"])