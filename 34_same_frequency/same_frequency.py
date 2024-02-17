def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    dict1 = {}
    dict2 = {}
    for dig in str(num1):
        if not not dict1.get(dig):
            dict1[dig] += 1
        else:
            dict1[dig] = 1
    for dig in str(num2):
        if not not dict2.get(dig):
            dict2[dig] += 1
        else:
            dict2[dig] = 1
    return True if dict1 == dict2 else False
    


