def reverse_integer(n):

    reversed = 0
    while n > 0:
        remainder = n %10
        reversed = reversed *10 + remainder
        n = n // 10
    return  reversed

if __name__ == '__main__':
    n = 12345
    print(reverse_integer(n))


