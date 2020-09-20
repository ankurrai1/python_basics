# TASK : is to impliment Selection sort


arr = [1, 7, 6, 4, 11, 0, -5]

def selectionSort(arr):
    i = 0
    while i<len(arr):
        smallest = min(arr[i:])
        index_of_smallest = arr.index(smallest)
        arr[i],arr[index_of_smallest] = arr[index_of_smallest],arr[i]
        i=i+1

print (arr)

selectionSort(arr)

print(arr)