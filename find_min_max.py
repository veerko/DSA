def min(arr):
    smallest_num = arr[0]

    for i in arr:
        if i < smallest_num :
            smallest_num = i

    return smallest_num


print(min([4,32,5,1,6,1,5]))

def max(arr):
    largest_num = arr[0]

    for i in arr:
        if i > largest_num:
            largest_num = i

    return largest_num

print(max([4,32,5,1,6,1,5]))
            