def BubbleSort(array):
    """Does bubble sort algorithm"""
    swapped = 1
    for passnum in range(len(array)-1, 0, -1):
        if swapped == 0:
            return
        for i in range(passnum):
            if array[i] > array[i+1]:
                array[i], array[i+1] = arr[i+1], array[i]
                swapped = 1
    return array


if __name__ == "__main__":

    arr = [10, 4, 43, 5, 57, 91, 45, 9, 7]
    
    result = BubbleSort(arr)

    print(result)