class Matrix(object):

    def __init__(self, matrix_string):
        self.matrix = []
        rows = matrix_string.split("\n")
        for row in rows:
            self.matrix.append(list(map(lambda element: int(element), row.split(' '))))

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        from_columns = []
        for row in self.matrix:
            from_columns.append(row[index -1])
        return from_columns
