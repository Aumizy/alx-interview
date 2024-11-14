#!/usr/bin/python3
"
    Create a function that returns a list of lists of integers representing
    the Pascal’s triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer
"


def pascal_triangle(n):
    "
    Pascal's triangle
    "
    if n <= 0:
        return []
    triangle = [[1]]
    for a in range(1, n):
        row = [1]
        for b in range(1, a):
            row.append(triangle[a - 1][b - 1] + triangle[a - 1][b])
        row.append(1)
        triangle.append(row)
    return triangle
