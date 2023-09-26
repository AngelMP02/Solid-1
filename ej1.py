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
         
# Definir una matriz de ejemplo
mi_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Crear un objeto de la clase Matrix
matriz_objeto = Matrix(mi_matriz)

# Imprimir la matriz original
print("Matriz original:")
matriz_objeto.print()

# Imprimir la matriz transpuesta
print("\nMatriz transpuesta:")
matriz_objeto.transpose()
