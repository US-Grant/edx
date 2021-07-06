def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    if x == b:
        return 1
    elif x < b:
        return 0
    else:
        return myLog(x / b, b) + 1


def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    # Your code here
    L.reverse()
    for sublist in L:
        sublist.reverse()


def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here
    result = []
    for key in aDict.keys():
        if aDict[key] == target:
            result.append(key)
    return sorted(result)


def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    # Your code here
    m = None
    for item in t:
        tmp = item if isinstance(item, int) else max_val(item)
        if m and m < tmp or not m:
            m = tmp
    return m


def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer
    g takes in an integer, applies a Boolean function,
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    m = None
    for i in L[:]:
        if g(f(i)):
            if not m or m < i:
                m = i
        else:
            L.remove(i)
    if len(L) == 0:
        return -1
    return m
