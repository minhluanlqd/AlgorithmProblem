""""""
"""
This problem was asked by Netflix. #282

Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythogorean triplet 
(a, b, c) is defined by the equation a^2+ b^2= c^2.
"""


def checkPythagorean(arr):
    arr = [x ** 2 for x in arr]
    for a in arr:
        for b in arr:
            for c in arr:
                if a + b == c or a + c == b or b + c == a:
                    return True
    return False


""" Time: O(N^3)"""


def checkPythagorean_2(array):
    array = sorted([x ** 2 for x in array])
    for c in range(len(arr) - 1, 1, -1):
        a, b = 0, c - 1

        while a < b:
            if array[a] + array[b] == array[c]:
                return True
            elif array[a] + array[b] < array[c]:
                a += 1
            elif array[a] + array[b] > array[c]:
                b -= 1
    return False
"""Time : O(N^2)"""

arr = [110, 20, 3, 40, 99, 5, 6]
print(checkPythagorean(arr))
print(checkPythagorean_2(arr))
