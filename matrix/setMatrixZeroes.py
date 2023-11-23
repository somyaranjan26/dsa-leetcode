# Set Matrix Zeroes

# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Solution 1
from sys import stdin


def setMatrixZeroes(matrix):
    # create a set to store the row and column indices
    rows = set()
    cols = set()
    
    # loop through the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # if the current element is 0
            if matrix[i][j] == 0:
                # add the row and column indices to the sets
                rows.add(i)
                cols.add(j)
    
    # loop through the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # if the row or column index is in the sets
            if i in rows or j in cols:
                # set the current element to 0
                matrix[i][j] = 0
    
    return matrix

# Solution 2
def setMatrixZeroes2(matrix):
    # create a boolean variable to check if the first column has a 0
    col0 = False
    
    # loop through the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # if the current element is 0
            if matrix[i][j] == 0:
                # if the column index is 0
                if j == 0:
                    # set col0 to True
                    col0 = True
                # else
                else:
                    # set the first element of the row and column to 0
                    matrix[i][0] = 0
                    matrix[0][j] = 0
    
    # loop through the matrix
    for i in range(len(matrix)-1, -1, -1):
        for j in range(len(matrix[0])-1, 0, -1):
            # if the first element of the row or column is 0
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                # set the current element to 0
                matrix[i][j] = 0
        # if col0 is True
        if col0:
            # set the first element of the row to 0
            matrix[i][0] = 0
    
    return matrix

 
# Sample Input 2 :
# 2      #! number of test cases
# 2 3    #! row and column
# 7 19 3
# 4 21 0
# 3 3    #! row and column
# 1 2 3
# 4 0 6
# 7 8 9

# Sample Output 2 :
# 7 19 0
# 0 0 0
# 1 0 3
# 0 0 0
# 7 0 9

def takeInput():
    row = int(stdin.readline().rstrip())
    col = int(stdin.readline().rstrip())
    
    mat = [[int(j) for j in stdin.readline().rstrip().split()] for i in range(row)]
    return mat, row, col

