### Squared circle (25 points) ###
import random

def solve(rayon, L, nbrPoints):
    circHits = 0
    print(L, " ", rayon)
    for pointNum in range(nbrPoints):
        #( random.random(), L)
        xPos = random.random()*L/2
        yPos = random.random()*L/2
        
        dist = (xPos ** 2 + yPos ** 2) ** 0.5
        print(xPos, yPos, dist)
        if (xPos ** 2 + yPos ** 2) ** 0.5 <= rayon:
            circHits += 1
    #print(circHits/nbrPoints)
    return(circHits/nbrPoints)
