class Matrix:
    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matrix = [[0 for i in range(n)] for j in range(m)]

    def insert(self, i, j, number):
        self.matrix[i - 1][j - 1] = number

    def number_at(self, i, j):
        return self.matrix[i - 1][j - 1]

    def add(self, other_matrix):
        if ((self.m != other_matrix.m) or (self.n != other_matrix.n)):
            raise ValueError

        result = Matrix(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                result.insert(i, j, self.number_at(i,j) + other_matrix.number_at(i, j))
        return result

    def multiply(self, other_matrix):
        if (self.n != other_matrix.m):
            raise ValueError
        result = Matrix(self.m, other_matrix.n)
        for i in range(result.m):
            for j in range(result.n):
                sum = 0
                for k in range(self.n):
                    sum = sum + self.number_at(i + 1, k + 1) * other_matrix.number_at(k + 1, j + 1)
                result.insert(i + 1, j + 1, sum)
        return result
