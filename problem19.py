""""""
"""
This problem was asked by Amazon.

Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 
3 -> 4 -> -7, then -6 -> 6, leaving only 5.
"""


class LinkedList:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def print_node(linkedlist):
    start = end = linkedlist

    while start:
        end = start
        total = 0
        skip = False

        while end:
            total += end.data
            if total == 0:
                start = end
                skip = True
                break
            end = end.next

        if not skip:
            print(start.data)

        start = start.next

