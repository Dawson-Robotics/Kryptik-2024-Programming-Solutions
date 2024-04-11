
def isPunctuation(char):
    if char == '!'or char == '.' or char == '?' :
        return True
    return False

def solve(s1, s2):
    newText = ''
    if len(s1) > len(s2) :
        longer = s1
        shorter = s2
    elif len(s1) == len(s2) :
        if (isPunctuation(s1[len(s1)-1])) :
            longer = s2
            shorter = s1
        else :
            longer = s1
            shorter = s2
    else :
        longer = s2
        shorter = s1
    for i in range(len(longer)):
        if len(shorter) > i :
            char1 = longer[i]
            char2 = shorter[i]
            newText += char1+char2
        else :
            newText += longer[i]                                 

    return newText
