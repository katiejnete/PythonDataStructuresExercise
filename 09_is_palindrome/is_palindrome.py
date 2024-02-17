def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    og = list(phrase.replace(' ','').lower()).copy()
    og = ''.join(og)
    new = list(phrase.replace(' ','').lower())
    new.reverse()
    new = ''.join(new)
    result = ''
    result = True if og == new else False
    return result
