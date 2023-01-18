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

from Sudoku import *

Generator = Sudoku_Generator()
Generator.generate()
print("\n")
Sudoku = Sudoku_Solver(Generator.board)
Sudoku.solve()
Sudoku.display()

