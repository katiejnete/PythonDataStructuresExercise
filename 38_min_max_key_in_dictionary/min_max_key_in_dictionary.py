def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    d = list(d.keys())
    max = 0
    if type(d[0]) is int:
        for i in range(len(d)):
            if len(range(d[i])) > max:
                max = d[i]
        min = max
        for i in range(len(d)):
            if len(range(d[i])) < min:
                min = d[i]
        return (min,max)
    else:
        for i in range(len(d)):
            if len(d[i]) > max:
                max_str = d[i]
                max = len(d[i])
        min = max
        for i in range(len(d)):
            if len(d[i]) < min:
                min_str = d[i]
                min = len(d[i])
        return (min_str,max_str)


