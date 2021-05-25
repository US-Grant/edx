import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """
    l = len(choices)
    result = np.array(list(format(2**l-1, "0"+str(l)+"b")), dtype=int)
    min_sum = sum(result)
    flag = False
    sums = []
    for i in range(2**l):
        tmp_array = np.array(list(format(i, "0"+str(l)+"b")), dtype=int)
        tmp = sum(tmp_array*choices)
        sums.append(tmp)
        if tmp == total:
            flag = True
            current_sum = sum(tmp_array)
            if current_sum < min_sum:
                min_sum = current_sum
                result = tmp_array
    if not flag:
        a = []
        m = max(sums)
        for s in sums:
            if total-s >=0:
                a.append(total-s)
            else:
                a.append(m)
        i = a.index(min(a))
        return np.array(list(format(i, "0"+str(l)+"b")), dtype=int)
    return result

        #print(np.array(list(bin(i)[2:]), dtype=int))

print(find_combination([1, 81, 3, 102, 450, 10], 9))
print(find_combination([4, 10, 3, 5, 8], 1))
print(find_combination([1,1,3,5,3], 5))
#print(format(2, f"05b"))
#print(np.array(list("1100"), dtype=int))
