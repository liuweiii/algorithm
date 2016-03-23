def partition(array, left, right):
    i = left - 1
    j = left
    temp = array[right]
    while j <= right - 1:
        if temp > array[j]:
            i += 1
            swap = array[i]
            array[i] = array[j]
            array[j] = swap
        j += 1
    swap = array[i+1]
    array[i+1] = array[right]
    array[right] = swap
    return i + 1


def fast_sort(array, left, right):
    if left < right:
        q = partition(array, left, right)
        fast_sort(array, left, q - 1)
        fast_sort(array, q + 1, right)


a = [5, 3, 8, 9, 9, 4, 7]
print a
fast_sort(a, 0, len(a) - 1)
print a
