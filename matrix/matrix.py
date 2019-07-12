class Matrix(object):

    def __init__(self, matrix_string):
        self.matrix = []
        rows = matrix_string.splitlines()
        self.matrix = ([[int(element) for element in row.split(' ')] for row in rows])

    def row(self, index):
        return self.matrix[index - 1][:]

    def column(self, index):
        return [row[index-1] for row in self.matrix]
