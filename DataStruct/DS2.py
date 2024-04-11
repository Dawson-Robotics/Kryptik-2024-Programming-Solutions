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
def shift(list: list[int], amount: int) -> list[int]:
    dir = x > 0
    for x in range(0, abs(amount)):
        if (dir):
            x.insert(0, 0)
        else:
            x.append(0)
    
# given mode, shear modulus
# positive meaning mode is D
# negative meaning mode is G
def convertMode(mode):
    mod, direc = mode
    if mode == "D":
        return mod
    if mode == "G":
        return -mod
    return 0

def solve(tableau, mode):
    mode = convertMode(mode)
    
    for x in range(mode, -mode):
