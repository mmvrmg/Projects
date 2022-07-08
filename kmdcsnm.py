def bubbleSort(array):
    length = len(array)

    for i in range(length): 
        for j in range(length - i): 
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


array = [7, 4, 5, 9, 2, 1, 6, 3, 8]
print(bubbleSort(array))