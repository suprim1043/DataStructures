def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array = [8,7,3,4,56,2]


def insertionSort(array):

    n = len(array)
    for i in range(n):
        j = i - 1
        while j >= 0 and array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            j -= 1
    return array

print(insertionSort(array))






