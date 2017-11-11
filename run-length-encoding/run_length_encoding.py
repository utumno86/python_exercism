def decode():
    pass


def encode(input):
    code = {}
    output = ''
    for letter in input:
        if letter in code:
            code[letter] += 1
        else:
            code[letter] = 1
    for key, value in code.items():
        if (value > 1):
            output += "{}{}".format(value,key)
        else:
            output += "{}".format(key)
    return output
