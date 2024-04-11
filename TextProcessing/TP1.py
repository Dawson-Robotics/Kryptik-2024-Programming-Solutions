### Fix the rules (15 points) ###

# You've read the rules for the CRC programming competition, but you don't understand
# them because there are too many errors to read any decently. You need to remove the capital
# letters that are not at the beginning of a word and add some at the beginning of each sentence.

def isPunctuation(char):
    if char == '!'or char == '.' or char == '?' :
        return True
    return False

def adjustPunctuation(char):
    return '!'

def isLowerCase(char):
    if char.lower() == char :
        return True
    return False

def checkCRC(text, pos):
    if text[pos].lower() == 'c' and pos < len(text)-1:
        if text[pos+1].lower() == 'r' and text[pos+2].lower() == 'c' :
            return True
    if text[pos].lower() == 'r' and pos > 0:
        if text[pos+1].lower() == 'c' and text[pos-1].lower() == 'c' :
            return True
    if text[pos].lower() == 'c' and pos > 1:
        if text[pos-1].lower() == 'r' and text[pos-2].lower() == 'c' :
            return True
    return False

def solve(text):
    newText = ''
    for i in range(len(text)):
        char = text[i]
        if isPunctuation(char) and char != '!' :
            char = adjustPunctuation(char)
        else :
            if i == 0 or isPunctuation(text[i-2]) and i != 1:
                char = char.upper()
            elif isLowerCase(char) == False and text[i-1] != ' ':
                char = char.lower()

        if checkCRC(text, i) :
            char = char.upper()

        newText += char

    return newText

