import re

def word_count(text):
    words = []
    temp = []
    count = dict()
    words = re.findall(r"\w+'\w+|[A-Za-z0-9]+", text)
    for word in words:
        word = word.lower()
        if word != '':
            count[word] = count.get(word, 0) + 1
    return count