def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    nums_dict = {}
    count = 0
    index = 0
    while index < len(nums):
        nums_dict['lower'] = nums[index]
        for num in range(index+1,len(nums)):
            if nums[num] > nums_dict['lower']:
                count += 1
        index += 1
    return count


        