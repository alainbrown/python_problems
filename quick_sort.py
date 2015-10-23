import random,math
# Complexity: O(n log n)
# Space: O(log n) -> stack size
def quicksort(array):
    random.shuffle(array)
    stac = [(0, len(array)-1)]
    while stac:
        start,stop = stac.pop()
        if stop - start > 0:
            pivot, left, right = array[start], start, stop
            while left <= right:
                while array[left] < pivot: left += 1
                while array[right] > pivot: right -= 1
                if left <= right:
                    array[left], array[right] = array[right], array[left]
                    left += 1
                    right -= 1
            stac.append((start, right))
            stac.append((left, stop))

alist = [54,26,93,17,77,31,44,55,20]
quicksort(alist)
print alist == [17, 20, 26, 31, 44, 54, 55, 77, 93]
