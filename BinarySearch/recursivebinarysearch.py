def RecursiveSearch(array, key, min , max):
    mid = (max + min )// 2
    if max<min:
        return -1
    if array[mid] > key:
       return  RecursiveSearch(array, key, min, mid-1)
    elif array[mid] < key:
        return RecursiveSearch(array, key, mid+1, max)
    else :
        return mid