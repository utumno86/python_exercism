import string


def is_pangram(test_string):
    pangram = True
    for char in string.ascii_lowercase:
        if char not in test_string.lower():
            pangram = False
<<<<<<< HEAD
    return pangram
=======
    return pangram
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd
