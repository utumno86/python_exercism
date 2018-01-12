def is_isogram(test_string):
    char_list = set()

    for char in test_string.lower():
        if char in char_list and char.isalpha():
            return False
        char_list.add(char)
    return True
