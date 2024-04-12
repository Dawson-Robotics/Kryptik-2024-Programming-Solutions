from twoD1 import solve

def test_document1():
    assert(solve(4) == 
['┌───────┐',
 '│┌─────┐│',
 '││┌───┐││',
 '│││┌─┐│││',
 '││││ ││││',
 '│││└─┘│││',
 '││└───┘││',
 '│└─────┘│',
 '└───────┘'])
    

def test_document2():
     assert(solve(2) == 
['┌───┐',
 '│┌─┐│',
 '││ ││',
 '│└─┘│',
 '└───┘'])
     
def test_document3():
    assert(solve(8) == 
['┌───────────────┐',
 '│┌─────────────┐│',
 '││┌───────────┐││',
 '│││┌─────────┐│││',
 '││││┌───────┐││││',
 '│││││┌─────┐│││││',
 '││││││┌───┐││││││',
 '│││││││┌─┐│││││││',
 '││││││││ ││││││││',
 '│││││││└─┘│││││││',
 '││││││└───┘││││││',
 '│││││└─────┘│││││',
 '││││└───────┘││││',
 '│││└─────────┘│││',
 '││└───────────┘││',
 '│└─────────────┘│',
 '└───────────────┘'])
