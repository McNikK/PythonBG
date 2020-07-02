class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __iter__(self):
        return iter(self.matrix)

    def __add__(self, other):
        return Matrix([[i+j for i,j in zip(a, b)] for a, b in zip(self.matrix, other)])

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, i)) for i in self.matrix])


m1 = Matrix([[1,2,3], [2,3,4],[3,5,6]])
m2 = Matrix([[1,2,3], [2,3,4],[3,5,6]])
m3 = m1+m2
print(m3)




