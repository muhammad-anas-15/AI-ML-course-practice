# Matrix Operations Calculator

# Function to print matrix 
def print_matrix(m):
    for row in m:
        for val in row:
            print(f"{val:6}", end=" ")

        print()

    print()

# Matrix Addition 
def add_matrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Matrices must have same dimensions!")
        return None
    
    result = []

    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)

    return result

# Matrix Subtraction
def subtract_matrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("Matrices must have same dimensions!")
        return None
    
    result = []

    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])

        result.append(row)

    return result

# Matrix Multiplication 
def multiply_matrix(A, B):
    if len(A[0]) != len(B):
        print("Matrix multiplication not possible!")
        return None

    result = []

    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            val = 0
            for k in range(len(B)):
                val += A[i][k] * B[k][j]

            row.append(val)

        result.append(row)

    return result

#  Matrix Transpose 
def transpose_matrix(A):
    result = []

    for j in range(len(A[0])):
        row = []
        for i in range(len(A)):
            row.append(A[i][j])

        result.append(row)

    return result

# Scalar Multiplication 
def scalar_multiply(A, s):
    result = []

    for row in A:
        new_row = []
        for val in row:
            new_row.append(val * s)

        result.append(new_row)

    return result

#  Determinant 
def determinant(A):
    if len(A) == 2 and len(A[0]) == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]

    if len(A) == 3 and len(A[0]) == 3:
        return (
            A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
            - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
            + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0])
        )

    print("Determinant only for 2x2 or 3x3 matrices.")
    return None


# Input Matrix
def input_matrix():
    rows = int(input("Rows: "))
    cols = int(input("Columns: "))

  # create empty list  
    matrix_values = []

    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1}: ").split()))
        matrix_values.append(row)

    return matrix_values


#  Menu 
while True:

    print("\nMatrix Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Scalar Multiplication")
    print("7. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        print("Matrix A")
        A = input_matrix()

        print("Matrix B")
        B = input_matrix()

        res = add_matrix(A, B)

        if res:
            print("Result:")
            print_matrix(res)

    elif choice == "2":
        print("Matrix A")
        A = input_matrix()

        print("Matrix B")
        B = input_matrix()

        res = subtract_matrix(A, B)

        if res:
            print("Result:")
            print_matrix(res)

    elif choice == "3":
        print("Matrix A")
        A = input_matrix()

        print("Matrix B")
        B = input_matrix()

        res = multiply_matrix(A, B)

        if res:
            print("Result:")
            print_matrix(res)

    elif choice == "4":
        print("Matrix")
        A = input_matrix()

        res = transpose_matrix(A)

        print("Transpose:")
        print_matrix(res)

    elif choice == "5":
        print("Matrix")
        A = input_matrix()

        det = determinant(A)

        if det is not None:
            print("Determinant:", det)

    elif choice == "6":
        print("Matrix")
        A = input_matrix()

        s = int(input("Enter scalar: "))
        res = scalar_multiply(A, s)

        print("Result:")
        print_matrix(res)

    elif choice == "7":
        print("Program Ended")
        break

    else:
        print("Invalid choice!")