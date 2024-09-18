
def reverse(number):
    start_index =0
    end_index = len(number)-1
    while end_index> start_index:
        number[start_index], number[end_index] = number[end_index],number[start_index]
        start_index = start_index+1
        end_index = end_index-1
if __name__ == '__main__':
    n =[1,2,3,4,5,6,7,8,9]
    reverse(n)
    print(n)