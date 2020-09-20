# TASK : is to impliment InsertionSort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            arr[j] = key
            j -= 1

    return arr


arr = [1, 7, 6, 4, 11, 0, -5]

print(arr)

insertion_sort(arr)

print(arr)