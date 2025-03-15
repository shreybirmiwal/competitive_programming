class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = []
        cols = []
        squares = []
        for i in range(3):
            squares.append([])
            for g in range(3):
                squares[i].append(set())

        for i in range(len(board)):
            for g in range(len(board[0])):
                
                if g == 0:
                    rows.append(set())

                if i == 0:
                    cols.append(set())

                if (board[i][g] in rows[i]):
                    print("ERROR", board[i][g], "in rows", rows[i])
                    return False

                if (board[i][g] in cols[g]):
                    print("ERROR", board[i][g], "in cols", cols[g])
                    return False
                    print()
            

                if(board[i][g] in squares[int(i/3)][int(g/3)]):
                    print("ERROR", board[i][g], "in square", squares[int(i/3)][int(g/3)])
                    return False


                if not board[i][g] == '.':
                    rows[i].add(board[i][g])
                    cols[g].add(board[i][g])
                    squares[int(i/3)][int(g/3)].add(board[i][g])  

        return True

                    
        