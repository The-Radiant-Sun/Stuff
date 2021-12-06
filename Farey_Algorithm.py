class Farey_Algorithm:
    def __init__(self, limit):
        self.limit = limit

    def convert(self, rational):
        sNum = rational.split('.')
        wNum = int(sNum[0])
        dNum = float(rational) - wNum  # Converting the inputted value into a 0 - 1 decimal

        uNumer, uDenom = 1, 1  # Creating upper bound fraction
        lNumer, lDenom = 0, 1  # Creating lower bound fraction

        for i in range(self.limit):
            nNumer = uNumer + lNumer  # Creating median fraction numerator
            nDenom = uDenom + lDenom  # Creating median fraction denominator
            if nNumer / nDenom < dNum:
                lNumer, lDenom = nNumer, nDenom  # Replacing the lower bound if possible
            elif nNumer / nDenom > dNum:
                uNumer, uDenom = nNumer, nDenom  # Replacing the upper bound if possible
            else:
                return [nNumer, nDenom, nNumer / nDenom]

        uNumer = uNumer + uDenom * wNum  # Reformating into rational number
        lNumer = lNumer + lDenom * wNum

        return [uNumer, uDenom, uNumer / uDenom] if abs(uNumer / uDenom - dNum) < abs(lNumer / lDenom - dNum) else [lNumer, lDenom, lNumer / lDenom]
