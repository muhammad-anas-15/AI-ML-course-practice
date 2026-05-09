import random
import math

class MiniNumPy:

    def __init__(self, data):
        self.data = [list(row) for row in data]

    # Create matrix filled with zeros
    @staticmethod
    def zeros(rows, cols):
        matrix = []

        for i in range(rows):
            row = []

            for j in range(cols):
                row.append(0)

            matrix.append(row)

        return MiniNumPy(matrix)

    # Create matrix filled with ones
    @staticmethod
    def ones(rows, cols):
        matrix = []

        for i in range(rows):
            row = []

            for j in range(cols):
                row.append(1)

            matrix.append(row)

        return MiniNumPy(matrix)

    # Create matrix with random values
    @staticmethod
    def random(rows, cols, a=0, b=1):
        matrix = []

        for i in range(rows):
            row = []

            for j in range(cols):
                value = random.uniform(a, b)
                row.append(value)

            matrix.append(row)

        return MiniNumPy(matrix)

    # Shape of matrix
    def shape(self):
        return (len(self.data), len(self.data[0]))

    # Reshape of matrix
    def reshape(self, r, c):

        flat = []

    # Convert matrix into a 1D list
        for row in self.data:
            for x in row:
                flat.append(x)

    # Check if reshape is possible
        if len(flat) != r * c:
            raise ValueError("Invalid reshape dimensions")

        new_data = []
        index = 0

    # Create new matrix 
        for i in range(r):
            row = []
            for j in range(c):
                row.append(flat[index])
                index = index + 1

            new_data.append(row)

        return MiniNumPy(new_data)

    # Transpose Matrix
    def transpose(self):
        new_data = []

        rows = len(self.data)
        cols = len(self.data[0])

        # Swap rows and columns
        for j in range(cols):
            new_row = []

            for i in range(rows):
                new_row.append(self.data[i][j])

            new_data.append(new_row)

        return MiniNumPy(new_data)

    #  Pretty Print 
    def __str__(self):
        rows = []

        for row in self.data:
            new_row = ""

            for val in row:
                new_row = new_row + str(round(val,3)) + " "

            rows.append(new_row)

        result = ""

        for r in rows:
            result = result + r + "\n"

        return result

    # Indexing 
    def __getitem__(self, idx):
        return self.data[idx]

    # Matrix Addition 
    def __add__(self, other):
        result = []

        rows = len(self.data)
        cols = len(self.data[0])

         # Element-wise matrix addition
        for i in range(rows):
            row = []

            for j in range(cols):
                value = self.data[i][j] + other.data[i][j]
                row.append(value)

            result.append(row)

        return MiniNumPy(result)

    # Matrix Subtraction 
    def __sub__(self, other):
        result = []

        rows = len(self.data)
        cols = len(self.data[0])

        for i in range(rows):
            row = []
            for j in range(cols):
                value = self.data[i][j] - other.data[i][j]
                row.append(value)

            result.append(row)

        return MiniNumPy(result)

    #  Element-wise Multiplication 
    def __mul__(self, other):
        result = []

        rows = len(self.data)
        cols = len(self.data[0])

        for i in range(rows):
            row = []
            for j in range(cols):
                value = self.data[i][j] * other.data[i][j]
                row.append(value)

            result.append(row)

        return MiniNumPy(result)

    #  Matrix Multiplication (@ operator) 
    def __matmul__(self, other):

        r1, c1 = self.shape()
        r2, c2 = other.shape()

        if c1 != r2:
            raise ValueError("Matrix multiplication not possible")

        result = []

    # Multiply matrices
        for i in range(r1):
            row = []
            for j in range(c2):

                val = 0
                for k in range(c1):
                    val += self.data[i][k] * other.data[k][j]

                row.append(val)

            result.append(row)

        return MiniNumPy(result)

    #  Sum --------
    def sum(self, axis=None):

    # Sum of all elements
        if axis is None:

            total = 0

            for row in self.data:
                for val in row:
                    total += val

            return total

    # Column-wise sum (axis = 0)
        elif axis == 0:
            result = []

            rows = len(self.data)
            cols = len(self.data[0])

            for j in range(cols):
                col_sum = 0

                for i in range(rows):
                    col_sum += self.data[i][j]

                result.append(col_sum)

            return result

    # Row-wise sum (axis = 1)
        elif axis == 1:
            result = []

            for row in self.data:
                result.append(sum(row))

            return result

    #  Mean 
    def mean(self):
        total_elements = len(self.data)*len(self.data[0])
        return self.sum()/total_elements

    #  Standard Deviation 
    def std(self):
        mean_val = self.mean()

        total = 0
        rows = len(self.data)
        cols = len(self.data[0])

    # calculate sum of squared differences = variance
        for row in self.data:
            for x in row:
                total += (x - mean_val) ** 2

        variance = total / (rows * cols)

        return math.sqrt(variance)

    #  Boolean Indexing 
    def greater_than(self, threshold):
        new_data = []

        for row in self.data:
            new_row = []

            for val in row:

            # If value is greater than threshold → 1 else 0 
                if val > threshold:
                    new_row.append(1)
                else:
                    new_row.append(0)

            new_data.append(new_row)

        return MiniNumPy(new_data)


A = MiniNumPy.random(2,2,0,5)
B = MiniNumPy.random(2,2,0,5)

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nA + B:")
print(A + B)

print("\nA @ B:")
print(A @ B)

print("\nTranspose of A:")
print(A.transpose())

print("\nMatrix Mean:", A.mean())
print("Matrix Std:", A.std())

print("\nBoolean Indexing (A > 2):")
print(A.greater_than(2))