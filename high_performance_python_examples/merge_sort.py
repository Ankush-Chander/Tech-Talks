# Python3 implementation of QuickSort
import sys
from functools import wraps

sys.setrecursionlimit(20000)

# for line_profiler
try:
    profile
except NameError:
    def profile(func):
        return func

from random import randint


@profile
def merge_sort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # into 2 halves
        R = arr[mid:]

        # Sorting the first half
        merge_sort(L)

        # Sorting the second half
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


if __name__ == '__main__':
    try:
        list_size = int(sys.argv[1])
    except Exception as err:
        list_size = 100
    randomlist = list(range(list_size, 1, -1))
    # print(randomlist)
    sorted_list = merge_sort(randomlist)
    # print(randomlist)

"""
time python3 -u merge_sort.py  10000

real	0m0.096s
user	0m0.083s
sys	0m0.013s
"""