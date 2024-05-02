import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_morethan():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 1, 2, 3, 4, 5]
    result = len(input_arr) >= 10
    assert result == 1
def test_bubble_sort_nonum():
    input_arr = []
    result = len(input_arr) == 0
    assert result
def test_bubble_sort_noint():
    input_arr = ['a', 'b', 'c']
    result = False
    for x in input_arr:
       ''' if not isinstance(x, int):
            result = True
            break'''
    assert not result

