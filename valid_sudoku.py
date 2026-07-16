board=[["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]


def valid_sudoku(board):
    rows={}
    cols={}
    boxes={}
    for r in range(9):
        for c in range(9):
            vals=board[r][c]
            if vals==".":
                continue
           
            if r not in rows:
                rows[r]=set()
            if vals in rows[r]:
                False
            rows[r].add(vals)

            if c not in cols:
                cols[c]=set()
            if vals in cols[c]:
                False
            cols[c].add(vals)

            box_id=(r//3,c//3)
            if box_id not in boxes:
                boxes[box_id]=set()
            if vals in boxes[box_id]:
                False
            boxes[box_id].add(vals)
        return True                    



print(valid_sudoku(board))


#using default dict :the checking of r not in rows is removed
from collections import defaultdict

def valid_sudoku_defaultdict(board):
    rows=defaultdict(set)
    cols=defaultdict(set)
    boxes=defaultdict(set)

    for r in range(9):
        for c in range(9):
            vals=board[r][c]
            if vals==".":
                continue
            
            box_id=(r//3,c//3)
            if vals in rows[r] or vals not in cols[c] or vals not in boxes[box_id]:
                False
            rows[r].add(vals)
            cols[c].add(vals)
            boxes[box_id].add(vals)
        return True 
    
print(valid_sudoku_defaultdict(board))    