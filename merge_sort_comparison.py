#! /usr/bin/python

import time
import random
import sys
import math

def merge(arr):
    retval = []
    # iterate and perform the merge
    while True:
        heads = []
        for i in range(len(arr)):
            if len(arr[i]):
                heads.append((arr[i][0], i))
        if not len(heads):
            break
        minimum = sorted(heads, key = lambda x:x[0])[0]
        retval.append(minimum[0])
        del arr[minimum[1]][0]
    return retval

def merge_sortk(arr, low, high, k):
    # base case
    if high - low < k:
        retval = arr[low:high+1]
        retval.sort()
        return retval
    # divide the array into k parts
    cd = int(math.floor((high - low) / k))
    results = []
    r_low = low
    for i in range(1, k + 1):
        results.append(merge_sortk(arr, r_low, r_low + cd, k))
        r_low += cd + 1
    return merge(results)


def main():
    if len(sys.argv) < 2:
        ks = [2]
    else:
        ks = [int(x) for x in sys.argv[1:]]
    n = 100000
    # n = 1000000 # 1 million
    # n = 10000000 # 10 million
    # n = 100000000 # 100 million
    # n = 1000000000 # 1 billion
    arr = [random.randint(0,1000000000000) for i in range(n)]
    for k in ks:
        print 'running %(k)d way merge sort on input size %(n)d' % locals()
        start_time = time.time()
        merge_sortk(arr[:], 0, len(arr) - 1, k)
        print k, "way merge sort took", time.time() - start_time, "seconds"

if __name__ == "__main__":
    main()
