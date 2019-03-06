''''''
"""
This problem was asked by Facebook. #274

Given a string consisting of parentheses, single digits, and positive and negative signs, convert the string into a 
mathematical expression to obtain the answer.

Don't use eval or a similar built-in parser.

For example, given '-1 + (2 + 3)', you should return 4.
"""


def apply_ops(ops, values):
    op = ops.pop()
    right, left = values.pop(), values.pop()
    if op == '+':
        values.append(right + left)
    else:
        values.append(left - right)


def parse(equation):
    values = []
    ops = []

    for char in equation:
        if char.isdigit():
            values.append(int(char))
        elif char == '(':
            ops.append(char)
        elif char == ')':
            while ops and ops[-1] != '(':
                apply_ops(ops, values)
            ops.pop()
        elif char == ' ':
            continue
        else:
            while ops and ops[-1] not in "()":
                apply_ops(ops, values)
            ops.append(char)
    while ops:
        apply_ops(ops, values)

    return values[0]


# def fix_negative(equation):
#     if equation[0] == '-':
#         equation = '0' + equation
#
#     equation = equation.replace('(-', '(0-')
#     return equation


equ = '1 + (2 + 3) - 8 + 8 - 4'
print(parse(equ))
"""Time: O(N) Space: O(N)"""
"""Still need case '-' at first"""
