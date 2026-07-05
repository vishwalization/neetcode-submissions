class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check row 
        for row in board:
            st = set()
            for i in row:
                if i != '.' and i in st:
                    return False
                st.add(i)

        # check col
        for i in range(9):
            st = set()
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in st:
                    return False

                st.add(board[j][i])
        

        # check 3x3
        for square in range(9):
            st = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j

                    if board[row][col] != '.' and board[row][col] in st:
                        return False
                
                    st.add(board[row][col])

        return True
                
