def word_count(text):
    words = []
    temp = []
    count = dict()
    words = text.split(" ")
    for word in words:
        new_word1 = word.replace(",", "\n")
        new_word1 = new_word1.replace("_", "\n")
        new_word1 = new_word1.replace("\t", "\n")
        temp = new_word1.split('\n')
        if len(temp) > 1:
            words.remove(word)
            for new_word2 in temp:
                words.append(new_word2)
    for word in words:
        for char in word:
            if char.isalnum() is False:
                word = word.replace(char, "")
        word = word.lower()
        if word != '':
            count[word] = count.get(word, 0) + 1
<<<<<<< HEAD
    return count
=======
    return count
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd
