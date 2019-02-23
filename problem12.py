""""""

"""
This problem was asked by Spotify.

Write a function, throw_dice(N, faces, total), that determines how many ways it is possible to throw N dice with some 
number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15.
"""


def throw_dice(N, faces, total):
    table = [[0] * (total + 1) for i in range(N + 1)]  # create table and initialize it 0

    for j in range(1, min(faces + 1, total + 1)):
        table[1][j] = 1
    for i in range(2, N + 1):
        for j in range(1, total + 1):
            for k in range(1, min(faces + 1, j)):
                table[i][j] += table[i - 1][j - k]

    return table[-1][-1]
"Time Complexity: O(N*faces*total)"

print(throw_dice(3, 6, 7))
