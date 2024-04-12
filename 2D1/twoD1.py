### Squaresception (20 points) ###



def solve(n):
    square=[]
    add=3
    for i in range(n):
        if(i == 0):
            square.append(chr(9484) + chr(9472) + chr(9488))
            square.append(chr(9474) + " " + chr(9474))
            square.append(chr(9492) + chr(9472) + chr(9496))
        else:
            square = [chr(9474) + x + chr(9474) for x in square]
            square.insert(0, chr(9484) + (chr(9472)*add) + chr(9488))
            square.insert(len(square), chr(9492) + (chr(9472)*add) + chr(9496))
            add= add+2
    return square

val = solve(8)

for n in val:
    print(n)

