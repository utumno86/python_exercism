import string


def is_pangram(test_string):
    pangram = True
    for char in string.ascii_lowercase:
        if char not in test_string.lower():
            pangram = False
    return pangram
