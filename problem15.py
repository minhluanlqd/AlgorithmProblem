""""""
"""
This problem was asked by Amazon. #278

Given an integer N, construct all possible binary search trees with N nodes.
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def make_trees(low, high):
    trees = []

    if low > high:
        trees.append(None)
        return trees

    for i in range(low, high + 1):
        left = make_trees(low, i - 1)
        right = make_trees(i + 1, high)

        for l in left:
            for r in right:
                node = Node(i, left=l, right=r)
                trees.append(node)
    return trees


def preOrder(root):
    result = []

    if root:
        result.append(root.data)
        result += preOrder(root.left)
        result += preOrder(root.right)

    return result


def construct_trees(N):
    trees = make_trees(1, N)
    for tree in trees:
        print(preOrder(tree))


construct_trees(3)
