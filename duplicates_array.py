# Python program to print duplicates from a list of integers
uniqueList = []
duplicateList = []


def duplicates(lis):
    for i in lis:
        if i not in uniqueList:
            uniqueList.append(i)
        elif i not in duplicateList:
            (
                duplicateList.append(i))
    return len(duplicateList)


if __name__ == '__main__':
    lis = [1, 2, 1, 2, 3, 4, 6, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

    count = duplicates(lis)
    print(f"Found {count} duplicate element(s) in the given list, below is are duplicated elements \n {duplicateList}")
