# Valid Sudoku
import collections


# Solution 1: 3 loops
# Time Complexity: O(n^2)
# Space Complexity: O(n)
def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    
    for i in range(9):
        row = {}
        col = {}
        
        # loop through the rows and columns
        for j in range(9):
            if board[i][j] != '.':
                if board[i][j] in row:
                    return False
                row[board[i][j]] = 1
            if board[j][i] != '.':
                if board[j][i] in col:
                    return False
                col[board[j][i]] = 1
    for i in range(3):
        for j in range(3):
            box = {}
            for k in range(3):
                for l in range(3):
                    if board[i*3+k][j*3+l] != '.':
                        if board[i*3+k][j*3+l] in box:
                            return False
                        box[board[i*3+k][j*3+l]] = 1
    return True


# Solution 2: using set

def isValidSudoku2(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    
    for r in range(9):
        row = set()
        col = set()
        box = set()
        for c in range(9):
            if board[r][c] != '.':
                if board[r][c] in row:
                    return False
                row.add(board[r][c])
                
            if board[c][r] != '.':
                if board[c][r] in col:
                    return False
                col.add(board[c][r])
            
            # i//3*3+c//3: the row index of the box
            # i%3*3+c%3: the column index of the box
            if board[r//3*3+c//3][r%3*3+c%3] != '.':
                if board[r//3*3+c//3][r%3*3+c%3] in box:
                    return False
                box.add(board[r//3*3+c//3][r%3*3+c%3])
    return True


# Solution 3: using dictionary
def isValidSudoku3(board):
    # 
    row = collections.defaultdict(set)
    col = collections.defaultdict(set)
    box = collections.defaultdict(set)
    
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                if (board[i][j] in row[i] or
                    board[i][j] in col[j] or
                    board[i][j] in box[(i//3, j//3)]):
                    return False
                row[i].add([board[i][j]])
                col[j].add([board[i][j]]) 
                box[(i//3,j//3)].add([board[i][j]])
    return True

if __name__ == '__main__':
    board = [
        ['5','3','.','.','7','.','.','.','.'],
        ['6','.','.','1','9','5','.','.','.'],
        ['.','9','8','.','.','.','.','6','.'],
        ['8','.','.','.','6','.','.','.','3'],
        ['4','.','.','8','.','3','.','.','1'],
        ['7','.','.','.','2','.','.','.','6'],
        ['.','6','.','.','.','.','2','8','.'],
        ['.','.','.','4','1','9','.','.','5'],
        ['.','.','.','.','8','.','.','7','9']
    ]
    # print(isValidSudoku(board))
    print(isValidSudoku3(board))