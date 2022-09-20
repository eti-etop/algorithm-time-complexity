import random, time

def main():
    
    matrixA = generateMatrix(800)
    matrixB = generateMatrix(800)

    print("Matrix A")
    # printMatrix(matrixA)
    
    print("Matrix B")
    # printMatrix(matrixB)

    print("Output")

    start = time.time()
    productMatrix = multiplyMatrix(matrixA, matrixB)
    stop = time.time()
    runningTime = stop - start

    # printMatrix(productMatrix)
    print(f"Runtime: {runningTime}")

    return


def multiplyMatrix(A, B):
    n = len(A)
    m = len(B)
    columnsInB = len(B[0])

    result = generateEmptyMatrix(n, m)

    for i in range(n):
        for j in range(columnsInB):
            for k in range(m):
                result[i][j] += A[i][k] * B[k][j]
    return result

def multiply2(A, B):

    result = generateEmptyMatrix(len(A), len(B))

    for i in range(len(A)):
 
        # iterating by column by B
        for j in range(len(B[0])):
 
            # iterating by rows of B
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result


def generateEmptyMatrix(n, m):
    
    matrix = []

    for i in range(n):
        rows = []
        for j in range(m):
            rows.append(0)
        matrix.append(rows)
    return matrix


def generateMatrix(n):
    matrix = []

    randomNumber = 0
    
    for i in range(n):
        rows = []
        for j in range(n):
            randomNumber = random.randint(1, 10)
            rows.append(randomNumber)
        
        matrix.append(rows)
    
    return matrix

def printMatrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()


main()