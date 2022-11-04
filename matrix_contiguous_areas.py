
MATRIX_1 = [
    [1, 3, 3],
    [1, 2, 3],
    [4, 2, 2]
]


MATRIX_2 = [
    [1, 1, 1, 1, 3, 3],
    [1, 1, 3, 2, 2, 3],
    [4, 5, 5, 5, 2, 2]
]


def explore_region(curr_value, i, j, n, m, mat, explored_squares, region):
    if mat[i][j] != curr_value or (i, j) in explored_squares:
        return

    region.append((i, j))
    explored_squares.append((i, j))

    if i + 1 < n:
        explore_region(curr_value, i + 1, j, n, m, mat, explored_squares, region)

    if i - 1 >= 0:
        explore_region(curr_value, i - 1, j, n, m, mat, explored_squares, region)

    if j - 1 >= 0:
        explore_region(curr_value, i, j - 1, n, m, mat, explored_squares, region)

    if j + 1 < m:
        explore_region(curr_value, i, j + 1, n, m, mat, explored_squares, region)


def count_regions(mat: list[list[int]]):
    n, m = len(mat), len(mat[0])
    explored_squares = []
    regions = []

    for i in range(n):
        for j in range(m):
            curr_value = mat[i][j]
            region = (curr_value, [])
            explore_region(curr_value, i, j, n, m, mat, explored_squares, region[1])
            if region[1]:
                regions.append(region)

    from pprint import pprint
    pprint(regions)


if __name__ == "__main__":
    count_regions(MATRIX_2)

