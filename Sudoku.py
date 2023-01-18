import random
import time


class Sudoku_Generator:
    def __init__(self):
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.difficulty = None

    def generate(self):
        self.fill_board(0, 0)
        self.remove_digits()
        self.difficulty = self.calculate_difficulty()
        self.display()

    def fill_board(self, row, col):
        if row == 9:
            return True
        if col == 9:
            return self.fill_board(row + 1, 0)
        if self.board[row][col] != 0:
            return self.fill_board(row, col + 1)
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(nums)
        for num in nums:
            if all(num != self.board[row][i] and num != self.board[i][col] and num != self.board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] for i in range(9)):
                self.board[row][col] = num
                if self.fill_board(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def is_valid(self, row, col, num):
        return not (num in [self.board[row][i] for i in range(9)] or num in [self.board[i][col] for i in range(9)] or num in [self.board[row // 3 * 3 + i // 3][col // 3 * 3 + i % 3] for i in range(9)])

    def remove_digits(self):
        gaps = [(i, j) for i in range(9) for j in range(9) if self.board[i][j] != 0]
        for i in random.sample(gaps, random.randint(40, 50)):
            self.board[i[0]][i[1]] = 0

    def calculate_difficulty(self):
        empty_cells = sum(row.count(0) for row in self.board)
        return "Expert" if empty_cells > 40 else "Hard" if empty_cells > 30 else "Intermediate" if empty_cells > 20 else "Easy"

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
        print("\nDifficulty: {}".format(self.difficulty))


class Sudoku_Solver:
    def __init__(self, board):
        self.board = board
        self.rows = [set(range(1, 10)) for _ in range(9)]
        self.cols = [set(range(1, 10)) for _ in range(9)]
        self.squares = [set(range(1, 10)) for _ in range(9)]
        self.empty_cells = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
        self.elapsed_time = None
        self.calls = 0
        self.solved = False

        for row in range(9):
            for col in range(9):
                if self.board[row][col] != 0:
                    num = self.board[row][col]
                    self.rows[row].remove(num)
                    self.cols[col].remove(num)
                    square_index = (row // 3) * 3 + (col // 3)
                    self.squares[square_index].remove(num)

    def solve(self):
        start_time = time.time()
        if self._solve():
            self.solved = True
        end_time = time.time()
        self.elapsed_time = end_time - start_time

    def _solve(self):
        if not self.empty_cells:
            return True
        self.calls += 1
        row, col = self.empty_cells.pop()
        for num in self.rows[row].intersection(self.cols[col]).intersection(self.squares[(row // 3) * 3 + col // 3]):
            self.board[row][col] = num
            self.rows[row].remove(num)
            self.cols[col].remove(num)
            self.squares[(row // 3) * 3 + col // 3].remove(num)
            if self._solve():
                return True
            self.rows[row].add(num)
            self.cols[col].add(num)
            self.squares[(row // 3) * 3 + col // 3].add(num)
            self.board[row][col] = 0
        self.empty_cells.append((row, col))
        return False

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
        if self.solved:
            print("\nSolved in {:.2f} seconds with {} calls.".format(self.elapsed_time, self.calls))
        else:
            print("\nUnable to find a solution.")
