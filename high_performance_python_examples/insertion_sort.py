import random
import sys

# # for line_profiler
try:
    profile
except NameError:
    def profile(func):
        return func


# Function to do insertion sort
@profile
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# sorting the array [12, 11, 13, 5, 6] using insertionSort
if __name__ == '__main__':
    try:
        list_size = int(sys.argv[1])
    except Exception as err:
        list_size = 100
    randomlist = list(range(list_size, 1, -1))
    # print(randomlist)
    sorted_list = insertion_sort(randomlist)
    # print(randomlist)


"""
time python3 -u insertion_sort.py  10000

real	0m5.237s
user	0m5.220s
sys	0m0.016s
"""