def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowel_map = {}
    phrase = phrase.lower()
    for char in phrase:
        if char in 'aeiou':
            if not not vowel_map.get(char):
                vowel_map[char] += 1
            else:
                vowel_map[char] = 1
    return vowel_map
# 