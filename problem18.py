""""""
"""
This problem was asked by Google. #298

A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes 
along, but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest 
portion of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of 
four.
"""


def pick_fruits(trees):
    a, b = trees[0], trees[1]

    last_picked = b
    last_picked_count = (a == b)
    max_length_path = curr = 1

    for tree in trees[1:]:
        if tree not in (a, b):
            a, b = last_picked, tree
            last_picked = tree
            curr = last_picked_count + 1
        else:
            curr += 1
            if last_picked == tree:
                last_picked_count += 1
            else:
                last_picked = tree
                last_picked_count = 1

        max_length_path = max(curr, max_length_path)
    return max_length_path


trees = [2, 1, 2, 3, 3, 1, 3, 5]
print(pick_fruits(trees))
