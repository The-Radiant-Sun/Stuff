class Sudoku_Solver:
    def __init__(self):
        self.board = [[5, 3, 0,  0, 7, 0,  0, 0, 0],
                      [0, 0, 0,  1, 9, 5,  0, 0, 0],
                      [0, 9, 8,  0, 0, 0,  0, 6, 0],

                      [8, 0, 0,  0, 6, 0,  0, 0, 3],
                      [4, 0, 0,  8, 0, 0,  0, 0, 1],
                      [0, 0, 0,  0, 2, 0,  0, 0, 0],

                      [0, 6, 0,  0, 0, 0,  2, 8, 0],
                      [0, 0, 0,  4, 0, 9,  0, 0, 5],
                      [0, 0, 0,  0, 8, 0,  0, 7, 0]]

    def solve(self):
        # Find the next empty cell
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            self.display()
                            print("")
                            if self.solve():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

    def is_valid(self, row, col, num):
        # Check if the number is valid in the current cell
        for x in range(9):
            if self.board[row][x] == num or self.board[x][col] == num:
                return False
        start_row, start_col = row - row % 3, col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
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