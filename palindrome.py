'''def is_palindrom(s):
    if s[::-1] == s:
        return True
    return False
'''


def is_palindrome(s):
    standard_str = s
    reverse_string = reverse(s)
    if standard_str==reverse_string:
        return True
    return False

def reverse(data):
    data = list(data)
    start_index = 0
    end_index =len(data)-1

    while end_index>start_index:
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index =start_index + 1
        end_index = end_index - 1
        return  ''.join(data)


if __name__ =='__main__':
    print(is_palindrome("srihari"))