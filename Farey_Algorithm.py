class Farey_Algorithm:
    def __init__(self, limit):
        self.limit = limit

    def convert(self, integer):
        sNum = integer.split('.')
        wNum = int(sNum[0])
        dNum = float(integer) - wNum

        uNumer, uDenom = 1, 1
        lNumer, lDenom = 0, 1

        for i in range(self.limit):
            nNumer = uNumer + lNumer
            nDenom = uDenom + lDenom
            if nNumer / nDenom < dNum:
                lNumer, lDenom = nNumer, nDenom
            elif nNumer / nDenom > dNum:
                uNumer, uDenom = nNumer, nDenom
            else:
                return [nNumer, nDenom, nNumer / nDenom]

        uNumer = uNumer + uDenom * wNum
        lNumer = lNumer + lDenom * wNum

        return [uNumer, uDenom, uNumer / uDenom] if abs(uNumer / uDenom - dNum) < abs(lNumer / lDenom - dNum) else [lNumer, lDenom, lNumer / lDenom]
