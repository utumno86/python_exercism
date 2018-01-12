def to_rna(text):
    DNA = 'GCTA'
    RNA = 'CGAU'
    if any(char not in DNA for char in text):
        return ''
    else:
        transcription = str.maketrans(DNA, RNA)
<<<<<<< HEAD
        return text.translate(transcription)
=======
        return text.translate(transcription)
>>>>>>> 371894dab186cec701ce325dcc4d002c02d93cbd
