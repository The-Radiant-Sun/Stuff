def requestPRN(question):
    return abs(round(int(input(question))))

"""from Farey_Algorithm import Farey_Algorithm

FA = Farey_Algorithm(requestPRN("Input cycle limit: "))
values = FA.convert(input("Input value for fractional approximation: "))
print(f"The approximated fraction is {values[0]}/{values[1]}, with a decimal conversion of {values[2]}")"""

from Hailstone_Algorithm import Hailstone_Algorithm

HA = Hailstone_Algorithm(requestPRN("Input cycle limit: "))
HA.reduce(requestPRN("Input values: "))
