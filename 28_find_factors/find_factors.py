def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    import math
    all_divis = []
    s_r = math.sqrt(num)
    for i in range(round(s_r)):
        if i != 0 and num % i == 0:
            divis = num / i
            all_divis.append(int(i))
            all_divis.append(int(divis))
            all_divis.sort()
    return all_divis
            

