#! /usr/bin/python

"""
This function will return the maximum sum starting from i, j to the bottom 
right. So call this with 0,0 to compute the max sum of the whole matrix.
This is a very simple dynamic programming algorithm.
"""
def max_sum(arr, i, j):
    # we have reached the bottom, stop
    if i == len(arr) - 1 and j == len(arr[0]) - 1:
        return arr[i][j]
    # check bounds
    if i == len(arr) - 1: # we can only move right
        return arr[i][j] + max_sum(arr, i, j + 1)
    if j == len(arr[0]) - 1: # we can only move down
        return arr[i][j] + max_sum(arr, i + 1, j)
    # choose the best path
    s1 = max_sum(arr, i + 1, j)
    s2 = max_sum(arr, i, j + 1)
    return arr[i][j] + (s1 if s1 > s2 else s2)

# sample inputs
a = [0] * 3
a[0] = [[10, 20], 
        [2,  40]]
a[1] = [[56, 45, 12, 24], 
        [75, 95, 35, 5 ], 
        [12, 75, 35, 50]]
a[2] = [[65,  75, 100, 12], 
        [14,  95, 5,   15], 
        [105, 15, 35,  30], 
        [5,   12, 100, 50]]

for i in range(3):
    print "input matrix: ", a[i]
    print "max sum: ", max_sum(a[i], 0, 0)
    print ""
