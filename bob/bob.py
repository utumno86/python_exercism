#
# Skeleton file for the Python "Bob" exercise.
#


def hey(text):
    punctuation = text[-1:]
    if text.upper() == text and text.lower() != text:
        return 'Whoa, chill out!'
    elif punctuation == '?' or punctuation == ' ':
        return 'Sure.'
    elif len(text) < 1 or punctuation == '\t':
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'