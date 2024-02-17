def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    l_sum = 0
    r_sum = 0
    neg_y = -1
    for num in range(len(matrix)):
        x = num
        y = num
        l_sum += matrix[y][x]
        r_sum += matrix[neg_y][x]
        neg_y -= 1
    return l_sum + r_sum

