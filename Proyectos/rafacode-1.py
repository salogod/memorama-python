import random

def create_matrix(row, col):
    """Function to create a matrix with shuffled values."""
    values = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
    random.shuffle(values)
    matrix = [values[i:i + col] for i in range(0, row * col, col)]
    return matrix

def show_matrix(matrix):
    """Function to display a matrix in the usual way."""
    for row in matrix:
        for value in row:
            print(f'{value:3}', end=' ')
        print()

def validate(r, c, matrix):
    if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
        print("Enter valid row and column values.")
        return False
    elif matrix[r][c] == 0:
        print("The cell has already been matched.")
        return False
    else:
        return True

def main():
    rows = 4
    columns = 5
    matrix = create_matrix(rows, columns)
    tokens = 20

    while tokens > 0:
        print(f"{tokens} tokens remaining")
        show_matrix(matrix)

        r1 = int(input("Cell 1 row: "))
        c1 = int(input("Cell 1 column: "))
        r2 = int(input("Cell 2 row: "))
        c2 = int(input("Cell 2 column: "))

        if validate(r1, c1, matrix) and validate(r2, c2, matrix):
            if matrix[r1][c1] == matrix[r2][c2]:
                matrix[r1][c1] = 0
                matrix[r2][c2] = 0
                tokens -= 2
                print(f"{tokens} tokens remaining")
                show_matrix(matrix)
            else:
                print("The cells do not match.")

        answer = input("Continue (y/n)? ")
        if answer.lower() != "y":
            break

    if tokens == 0:
        print("You win!")

if _name_ == "_main_":
    main()