def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    my_dict = {}
    if len(keys) <= len(values):
        return {keys[x]: values[x] for x in range(len(keys))}
    else:
        for x in range(0,len(values)):
            my_dict[keys[x]] = values[x]
        for x in range(len(values),len(keys)):
            my_dict[keys[x]] = None
        return my_dict


