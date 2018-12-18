"""
Given a real number n, find the square root of n. For example, given n = 9, return 3.

"""


# # given number upto given precision
# def square_root(number, precision):
#     start = 0
#     end = number / 2
#
#     # For computing integral part
#     # of square root of number
#     while start <= end:
#         mid = int((start + end) / 2)
#
#         if mid * mid == number:
#             ans = mid
#             break
#
#         # incrementing start if integral
#         # part lies on right side of the mid
#         if mid * mid < number:
#             start = mid + 1
#             ans = mid
#
#             # decrementing end if integral part
#         # lies on the left side of the mid
#         else:
#             end = mid - 1
#
#     # For computing the fractional part
#     # of square root upto given precision
#     increment = 0.1
#     for i in range(0, precision):
#         while ans * ans <= number:
#             ans += increment
#
#             # loop terminates when ans * ans > number
#         ans = ans - increment
#         increment = increment / 10
#
#     return ans
#
#
# n = int(input("Enter your number: "))
# print(square_root(n, 3))
# # Driver code
# print(round(square_root(50, 3), 4))
# print(round(square_root(10, 4), 4))

def square_root_1(n, error=0.00001):
    guess = 1

    while abs(guess ** 2 - n) >= error:
        guess = (guess + n / guess) / 2.0
    return guess


def square_root_2(n, error=0.00001):
    low = 0
    high = n
    guess = (low + high) / 2.0

    while abs(guess ** 2 - n) >= error:
        if guess ** 2 > n:
            high = guess
        else:
            low = guess
        guess = (low + high) / 2.0
    return guess


n = int(input("Enter your number: "))
print(square_root_1(n))
print(square_root_2(n))
