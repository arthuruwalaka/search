def BinarySearch(array, key):
    min = 0
    max = len(array) -1
    while max >= min:
        mid = (min + max) // 2 
        if array[mid] > key:
            max = mid-1
        elif array[mid] < key:
            min = mid+1
        else:
            return mid

    return -1
