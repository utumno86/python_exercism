def to_rna(text):
    DNA = 'GCTA'
    RNA = 'CGAU'
    if any(char not in DNA for char in text):
        return ''
    else:
        transcription = str.maketrans(DNA, RNA)
        return text.translate(transcription)
