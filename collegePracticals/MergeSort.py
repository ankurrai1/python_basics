def mergeSort(arr):
    if len(arr) > 1:

        r = len(arr)//2
        leftArr = arr[:r]
        rightArr = arr[r:]

        mergeSort(leftArr)
        mergeSort(rightArr)

        i = j = k = 0

       
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1

       
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1


arr = [1, 7, 6, 4, 11, 0, -5]
print(arr)
mergeSort(arr)
print(arr)
 