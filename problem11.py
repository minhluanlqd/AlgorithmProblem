''''''
"""This problem was asked by Morgan Stanley. (# 258)

In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to 
left, and continuing to go back and forth. This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7
You should return [1, 3, 2, 4, 5, 6, 7]."""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def print_level(node, level, forward):
    if level == 0:
        print(node.data)
    else:
        if forward:
            print_level(node.left, level - 1, forward)
            print_level(node.right, level - 1, forward)
        else:
            print_level(node.right, level - 1, forward)
            print_level(node.left, level - 1, forward)


def get_height(tree, height=0):
    if not tree:
        return height
    return max(get_height(tree.left, height + 1), get_height(tree.right, height + 1))


"""If the binary tree is very skewed, the height would be O(N). Since printing each level is also O(N), 
this algorithm runs in O(N2) time. """


def boustrophedon_1(tree):
    n = get_height(tree)
    forward = True

    for level in range(n):
        print_level(tree, level, forward)
        forward = not forward


"""Since we pop each element exactly once, this indeed runs in O(N) time, with O(N) additional space for the stacks."""


def boustrophedon_2(root):
    forward = [root]
    backward = []
    while backward or forward:

        while forward:
            tmp = forward.pop()
            print(tmp.data)

            if tmp.left:
                backward.append(tmp.left)
            if tmp.right:
                backward.append(tmp.right)

        while backward:
            tmp = backward.pop()
            print(tmp.data)

            if tmp.left:
                forward.append(tmp.left)
            if tmp.right:
                forward.append(tmp.right)



