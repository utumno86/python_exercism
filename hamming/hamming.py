def distance(string1, string2):
    count = 0
    if len(string1) != len(string2):
        raise ValueError('The lengths of the hamming test strings are not equal')
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            count += 1
<<<<<<< HEAD
    return count
=======
    return count
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd
