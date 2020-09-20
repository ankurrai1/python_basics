# TASK : is to impliment binary search


def binarySearch(arr, ele):
    if len(arr) == 0:
        return False
    midpoint = len(arr)//2
    if arr[midpoint]==ele:
        return True
    else:
        if ele<arr[midpoint]:
            return binarySearch(arr[:midpoint],ele)
        else:
            return binarySearch(arr[midpoint+1:],ele)

            

dataSet = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(dataSet, 3))
print(binarySearch(dataSet, 1))