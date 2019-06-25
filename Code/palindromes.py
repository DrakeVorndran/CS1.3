#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

chars = list(string.ascii_lowercase)

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_recursive(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    if len(text) < 1:
        return True
    pal = text.lower()
    left = 0
    right = len(text) - 1
    is_pal = True
    while is_pal: # worst case O(n) when the string is a palindrome or if the string has no aplha chars
        while pal[left] not in chars: # O(n) in case where the string has no alpha chars
            left += 1
            if left >= right:
                return True 
        while pal[right] not in chars: # O(n) in case where the string has no alpha chars
            right -= 1
            if right <= left: 
                return True
        if left >= right:
            return True
        if pal[left] != pal[right]:
            return False
        left += 1
        right -= 1
        
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests


def is_palindrome_recursive(text, left=None, right=None):# worst case O(n) when the string is a palindrome or if the string has no aplha chars
    # TODO: implement the is_palindrome function recursively here
    if len(text) < 1:
        return True
    if left is None:
        left = 0
        right = len(text) - 1
    if left >= right:
        return True
    pal = text.lower()
    if pal[left] not in chars:# O(n) in case where the string has no alpha chars
        return is_palindrome_recursive(text, left+1, right)
    while pal[right] not in chars:# O(n) in case where the string has no alpha chars
        return is_palindrome_recursive(text, left, right-1)
    if pal[left] != pal[right]:
        return False
    return is_palindrome_recursive(text, left+1, right-1)
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
    # print(is_palindrome_recursive("it was a cat I saw?"))
