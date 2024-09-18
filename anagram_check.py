def is_anagram(str1, str2):
    str_list1 = list(str1.lower())
    str_list2 = list(str2.lower())

    if len(str_list1) != len(str_list2):
        return False

    str_list1 = sorted(str_list1)
    str_list2 = sorted(str_list2)

    for i in range(len(str_list1)):
        if str_list1[i] != str_list2[i]:
            return False

    return True

if __name__ == '__main__':
    str1 = 'restful'
    str2 = 'FLUSTER'

    print(is_anagram(str1,str2))