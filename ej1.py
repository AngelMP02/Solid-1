class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def print(self):
        for row in self.matrix:
            for col in row:
                print(col, end=' ')
            print()

    def transpose(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print(self.matrix[j][i], end=' ')
            print()