def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_to_count = {}

    for char in phrase:
        if char in letter_to_count:
            letter_to_count[char] += 1
        else:
            letter_to_count[char] = 1
    #    letter_to_count[char] = (letter_to_count[char] or 0) + 1

    return letter_to_count
