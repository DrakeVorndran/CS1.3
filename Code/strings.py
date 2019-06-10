#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)

    # This works but I feel like its cheating
    # for i in range(len(text)):
    #     if text[i:i+len(pattern)] == pattern:
    #         return True
    # return False
    if(len(pattern) < 1):
        return True
    for i in range(len(text) - len(pattern) + 1):
        # if the first char
        if text[i] == pattern[0]:
            if(check_pos(text, pattern, 0, i)):
                return True
    return False
                
def check_pos(text, pattern, position, diff):
    # breaks the loop if we are at the end of the pattern
    if position == len(pattern):
        return True
    # checks if pattern matches, and calls itself if it does
    if text[diff + position] == pattern[position]:
        return check_pos(text, pattern, position + 1, diff)
    return False




def find_index(text, pattern):
    if(len(pattern) < 1):
        return 0
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    for i in range(len(text) - len(pattern) + 1):
        # if the first char
        if text[i] == pattern[0]:
            if(check_pos(text, pattern, 0, i)):
                return i


def find_all_indexes(text, pattern):
    if(len(pattern) < 1):
        return list(range(len(text)))
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    indexes = []
    for i in range(len(text) - len(pattern) + 1):
        # if the first char
        if text[i] == pattern[0]:
            if(check_pos(text, pattern, 0, i)):
                indexes.append(i)
    return indexes


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()