def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    trutheys = []

    for ele in lst:
        if ele:
            trutheys.append(ele)

    return trutheys

# could also use list comprehensions