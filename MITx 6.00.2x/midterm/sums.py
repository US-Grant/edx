def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    max_sum = 0
    k = 1
    for i in L:
        tmp = i
        for j in L[k:]:
            tmp += j
            if max_sum < tmp:
                max_sum = tmp
        k += 1
        if i > max_sum:
            max_sum = i
    return max_sum

lists = [
    [3, 4, -1, 5, -4], # 11
    [3, 4, -8, 15, -1, 2], # 16
    [1, -1], # 1
    [5, -7, 1], # 5
    [0, -2, -5, -1, 5], # 5
    [-3, -2, 1, -1, -5] # 1
]

for list in lists:
    print(max_contig_sum(list))