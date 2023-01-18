class Sudoku_Solver:
    def __init__(self, board):
        self.board = board
        self.rows = [set(range(1, 10)) for _ in range(9)]
        self.cols = [set(range(1, 10)) for _ in range(9)]
        self.squares = [set(range(1, 10)) for _ in range(9)]

        for row in range(9):
            for col in range(9):
                if self.board[row][col] != 0:
                    num = self.board[row][col]
                    self.rows[row].remove(num)
                    self.cols[col].remove(num)
                    squareIndex = (row // 3) * 3 + (col // 3)
                    self.squares[squareIndex].remove(num)

    def solve(self):
        # Find the next empty cell
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    squareIndex = (row // 3) * 3 + (col // 3)
                    for num in self.rows[row].intersection(self.cols[col], self.squares[squareIndex]):
                        self.board[row][col] = num
                        self.rows[row].remove(num)
                        self.cols[col].remove(num)
                        self.squares[squareIndex].remove(num)
                        if self.solve():
                            return True
                        self.board[row][col] = 0
                        self.rows[row].add(num)
                        self.cols[col].add(num)
                        self.squares[squareIndex].add(num)
                    return False
        return True

    def display(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - ")

            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(str(self.board[i][j]) + " ", end="")