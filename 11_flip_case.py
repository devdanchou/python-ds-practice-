def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flippedPhrase = ""
    for char in phrase:
        if char.upper() == to_swap.upper():
            if char.upper() == char:
                flippedPhrase += char.lower()
            else:
                flippedPhrase += char.upper()
        else:
            flippedPhrase += char

    return flippedPhrase
