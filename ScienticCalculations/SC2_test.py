from SC2 import solve

def test_document1():
    assert(solve([1, 2, 5, 6, 3, 12, 24, 2, 2, 4, 9, 10], 22) == [[12, 10],[12, 9, 1],[12, 6, 4],[12, 6, 3, 1],[12, 6, 2, 2],[12, 5, 4, 1],[12, 5, 3, 2],[12, 5, 2, 2, 1],[12, 4, 3, 2, 1],[12, 4, 2, 2, 2],[12, 3, 2, 2, 2, 1],[10, 9, 3],[10, 9, 2, 1],[10, 6, 5, 1],[10, 6, 4, 2],[10, 6, 3, 2, 1],[10, 6, 2, 2, 2],[10, 5, 4, 3],[10, 5, 4, 2, 1],[10, 5, 3, 2, 2],[10, 5, 2, 2, 2, 1],[10, 4, 3, 2, 2, 1],[9, 6, 5, 2],[9, 6, 4, 3],[9, 6, 4, 2, 1],[9, 6, 3, 2, 2],[9, 6, 2, 2, 2, 1],[9, 5, 4, 3, 1],[9, 5, 4, 2, 2],[9, 5, 3, 2, 2, 1],[9, 4, 3, 2, 2, 2],[6, 5, 4, 3, 2, 2],[6, 5, 4, 2, 2, 2, 1]])


def test_document2():
    assert(solve([1, 3, 5, 7, 9], 25) == [[9, 7, 5, 3, 1]])

def test_document3():
    assert(solve([14, 31, 17, 50, 7, 9, 11], 40) == [[31, 9],[17, 14, 9]])

def test_document4():
    assert(solve([7, 8, 9, 12, 13, 13, 5, 6], 26) == [[13, 13],[13, 8, 5],[13, 7, 6],[12, 9, 5],[12, 8, 6],[8, 7, 6, 5]])
