""""""
"""
This problem was asked by Google. #283

A regular number in mathematics is defined as one which evenly divides some power of 60. Equivalently, we can say that 
a regular number is one whose only prime divisors are 2, 3, and 5.

These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to 
the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.
"""

import heapq


def regular_number_1(n):
    twos = [2 ** i for i in range(n)]
    threes = [3 ** i for i in range(n)]
    fives = [5 ** i for i in range(n)]

    solution = set()
    for two in twos:
        for three in threes:
            for five in fives:
                solution.add(two * three * five)
    return sorted(solution)[:n]  # Sort O(LogN)


"""Time: O(N^3LogN)"""


def regular_number_2(n):
    solution = [1]
    last = 0
    count = 0
    while count < n:
        x = heapq.heappop(solution)
        if x > last:
            yield x
            last = x;
            count += 1
            heapq.heappush(solution, 2 * x)
            heapq.heappush(solution, 3 * x)
            heapq.heappush(solution, 5 * x)


"""Time: O(NLogN)"""


def regular_number_3(n):
    solution = [1] * n
    i2, i3, i5 = 0, 0, 0

    for i in range(1, n):
        m = min(2 * solution[i2], 3 * solution[i3], 5 * solution[i5])
        solution[i] = m

        if m % 2 == 0:
            i2 += 1
        if m % 3 == 0:
            i3 += 1
        if m % 5 == 0:
            i5 += 1
    return solution


"""Time and space: O(N)"""

print(regular_number_1(10))
print(regular_number_2(10))
print(regular_number_3(10))
