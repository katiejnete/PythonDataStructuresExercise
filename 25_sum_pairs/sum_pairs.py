def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    length = len(nums)
    space = 0
    while space < length - 2:
        for i in range(length-1):
            j = i + 1 + space
            if j < length - 1:
                if nums[i] + nums[j] == goal:
                    return (nums[i],nums[j])
                else:
                    j += 1
        space += 1
    return ()
        
    # for i in range(length):
    #     for j in range(length):
    #         if j+1 < length and i != j+1:
    #             print(nums[i],nums[j+1])
    #             if nums[i] + nums[j+1] == goal:
    #                 return (nums[i],nums[j+1])
    # return ()