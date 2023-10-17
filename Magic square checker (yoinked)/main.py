def isMagicSquare(mat):
    n = len(mat)
    sumd1 = 0
    sumd2 = 0
    for i in range(n):
        sumd1 += mat[i][i]
        sumd2 += mat[i][n-i-1]
    if not(sumd1 == sumd2):
        return False
    for i in range(n):
        sumr = 0
        sumc = 0
        for j in range(n):
            sumr += mat[i][j]
            sumc += mat[j][i]
        if not(sumr == sumc == sumd1):
            return False
    return True

mat = [ [30, 39, 48, 1, 10, 19, 28],
        [38, 47, 7, 9, 18, 27, 29],
        [46, 6, 8, 17, 26, 35, 37],
        [5, 14, 16, 25, 34, 36, 45],
        [13, 15, 24, 33, 42, 44, 4],
        [21, 23, 32, 41, 43, 3, 12],
        [22, 31, 40, 49, 2, 11, 20] ]

if (isMagicSquare(mat)):
    print("YES!!!!!!1")
else:
    print("No.. :(")