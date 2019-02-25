""""""
"""
This problem was asked by Apple. #273

A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, 
return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.
"""


def find_fixed_point(arr):
    for i in range(len(arr)):
        if i == arr[i]:
            return i

    return False


"""O(N) Time"""


def find_fixed_point_1(arr):
    low, high = 0, len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            low = mid + 1
        else:
            high = mid - 1
    return False


"""O(logN)"""
arr = [-6, 0, 2, 40]
arr_1 = [1, 5, 7, 8]
print(find_fixed_point(arr))
print(find_fixed_point(arr_1))

print(find_fixed_point_1(arr))
print(find_fixed_point_1(arr_1))
