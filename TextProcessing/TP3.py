### Palindrole (30 points) ###

import math

# def symetryCheckEven(section):
#     for i in range(int(len(section))/2):
#         if section[i] != section[len(section)-i] :
#             return False
#     return True

def symetryCheckEven(section):
    for i in range(len(section)):
        if i < len(section)/2 :
            if section[i] != section[len(section)-i-1] :
                return False
    return True

def symetryCheckOdd(section):
    for i in range(len(section)):
        if i < math.trunc(len(section)/2+1) :
            if section[i] != section[len(section)-i-1] :
                return False
    return True

# def solve(L):
#     orderCount = 0
#     for i in range(len(L)):
#         for j in range(len(L)):
#             substr = L[i:-j]
#             if len(substr) > 2 :
#                 if len(substr)%2 == 1 : #odd
#                     if symetryCheckOdd(substr) :
#                         orderCount +=1
#                 else : #even
#                     if symetryCheckEven(substr) :
#                         orderCount +=1
    
#     return orderCount

# def solve(L):
#     orderCount = 0
#     i = 0
#     while i < len(L):
#         substr = L[:len(L)-i]
#         if len(substr) > 2 :
#             if len(substr)%2 == 1 : #odd
#                 if symetryCheckOdd(substr) :
#                     orderCount +=1
#                     i += int(len(substr)%2) + 1
#                 else :
#                     return orderCount
#             else : #even
#                 if symetryCheckEven(substr) :
#                     orderCount +=1
#                     i += int(len(substr)%2) + 1
#                 else :
#                     return orderCount
#         i+=1
    
#     return orderCount

def solve(L):
    orderCount = 0
    listwords = [L]
    while True :
        for word in listwords :
            if len(word) > 1 :
                if len(word)%2 == 1 : #odd
                    if not symetryCheckOdd(word) :
                        return orderCount
                else : #even
                    if not symetryCheckEven(word) :
                        return orderCount
            else:
                return orderCount
        orderCount += 1
        listwords = []
        if len(word)%2 == 1 :
            listwords.append(word[int(len(word)/2+1):])
            listwords.append(word[:int(len(word)/2)])
        else :
            listwords.append(word[int(len(word)/2):])
            listwords.append(word[:int(len(word)/2)])
    