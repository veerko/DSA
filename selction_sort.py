def findMin(lst):
    min = lst[0]
    min_index = 0

    for i in range(len(lst)):
        if lst[i] < min:
            min = lst[i]
            min_index = i

    return min_index


def selction_sort(lst):
    sorted_lst = []
    for i in range(len(lst)):
        min_index = findMin(lst)
        sorted_lst.append(lst.pop(min_index))
    return sorted_lst


print(selction_sort([4,32,5,1,6,1,5]))
