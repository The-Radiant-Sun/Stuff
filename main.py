"""from Farey_Algorithm import Farey_Algorithm

FA = Farey_Algorithm(requestPRN("Input cycle limit: "))
values = FA.convert(input("Input value for fractional approximation: "))
print(f"The approximated fraction is {values[0]}/{values[1]}, with a decimal conversion of {values[2]}")"""

"""from Hailstone_Algorithm import Hailstone_Algorithm

HA = Hailstone_Algorithm(requestPRN("Input cycle limit: "))
HA.reduce(requestPRN("Input values: "))"""

"""from Multithreading import Multithreading
MT = Multithreading()


def p(n):
    print(f"Thread {n} active")


for i in range(5):
    MT.openActiveThread(str(i), p, (i,))"""

"""import File_Type_Converter

File_Type_Converter.convertFileTypesInFolders('/Users/finn/Documents/PycharmProjects/Jump-Recorder/Info', 'csv', 'txt')"""

from Sudoku_Solver import Sudoku_Solver

board = [[5, 3, 0,  0, 7, 0,  0, 0, 0],
         [0, 0, 0,  1, 9, 5,  0, 0, 0],
         [0, 9, 8,  0, 0, 0,  0, 6, 0],

         [8, 0, 0,  0, 6, 0,  0, 0, 3],
         [4, 0, 0,  8, 0, 0,  0, 0, 1],
         [0, 0, 0,  0, 2, 0,  0, 0, 0],

         [0, 6, 0,  0, 0, 0,  2, 8, 0],
         [0, 0, 0,  4, 0, 9,  0, 0, 5],
         [0, 0, 0,  0, 8, 0,  0, 7, 0]]

sudoku = Sudoku_Solver(board)
sudoku.solve()
sudoku.display()

