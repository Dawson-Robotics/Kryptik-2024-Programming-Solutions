### Shear force (35 points) ###

# Given a c (digit)
# given c + x = 10
# x = 10 - c
# return x
def inverse(digit: int):
    return 10 - abs(digit)

# given list
# x = amount
# dir = left side of x positive, right side if x negative
# add 0 to the dir side of list x times
# return list
def shift(lst: list[int], amount: int) -> list[int]:
    dir = amount > 0
    listlen = len(lst)-1
    for x in range(0, abs(amount)):
        if (dir):
            for x in range(0, listlen):
                lst.insert(0, 0)
        else:
            for x in range(0, listlen):
                lst.append(0)
    return lst
    
# given mode, shear modulus
# positive meaning mode is D
# negative meaning mode is G
def convertMode(mode):
    mod, direc = mode
    if mode[1] == "D":
        return -int(mod)
    if mode[1] == "G":
        return int(mod)
    return 0

# given an array of arrays
# add all the values stacked on top of eachother.
def flatten(array):
    num = []
    
    for x in range(0, len(array[0])):
        num.append(0)
    
    for x in range(0, len(array)):
        for y in range(0, len(array[x])):
            num[y] += array[x][y]
    
    num = [(inverse(x) if x < 0 else x) for x in  num]
    res = "".join([str(x) for x in num])
    print(res)
    return res
    
        
def solve(tableau, mode):
    mode = convertMode(mode)
    for indx in range(0, len(tableau)):
        if (mode > 0):
            tableau[indx] = shift(tableau[indx], mode - indx)
        else:
            tableau[indx] = shift(tableau[indx], mode + indx)
    print(tableau)  
    for x in tableau:
        for y in range():
            
    print(flatten(tableau))
    return flatten(tableau)
    
              
    
    
    
        