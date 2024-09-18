def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11, 11, 22, 25]
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)
