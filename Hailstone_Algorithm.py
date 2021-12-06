class Hailstone_Algorithm:
    def __init__(self, limit):
        self.limit = limit

    def reduce(self, integer):
        iteration = 0

        while iteration != self.limit and integer != 1:
            if integer % 2 == 1:
                integer = integer * 3 + 1
            else:
                integer = integer / 2

            iteration += 1
            print(str(integer).split('.')[0])
