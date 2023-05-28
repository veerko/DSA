def binary_search(list,target):
    first = 0
    last =  len(list) - 1

    while first <= last:
        mid = (first + last) // 2

        if list[mid] == target:
            return mid
        if list[mid] > target:
            last = mid - 1
        else:
            first = mid + 1
    return None
    

print(binary_search([1,2,4,5,6,7], 4))
