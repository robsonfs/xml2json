from unittest import TestCase, main

def quicksort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[0]

    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    if len(left) > 1:
        left = (quicksort(left))

    if len(right) > 1:
        right = (quicksort(right))

    m = [pivot] * arr.count(pivot)
    ordered_arr = left + m + right
    return ordered_arr

def get_smaller(l):
    if l:
        return quicksort(l)[0]
    return []



if __name__ == '__main__':
    main()
