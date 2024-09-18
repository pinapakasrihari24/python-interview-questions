def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        print(i)
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    # Sample list to be sorted
    arr = [39, 12, 18, 85, 72, 10, 2, 18]
    print("Unsorted list is:")
    print(len(arr))

    bubble_sort(arr)

    print("Sorted list is:")
    print(arr)
