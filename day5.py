input_d4 = open("day_5/day5.txt", "r").read().split("\n")
input_d2 = open("day_2/day2.txt", "r").read().split("\n")
ex1_d2 = input_d2[0].split(",")

from day2 import *
print(getstarted(ex1))

# Opcode 3 : takes a single integer as input and saves it to the position given
# by its only parameter.
# For example, the instruction 3,50 would take an input value and store it at address 50.

# Opcode 4: outputs the value of its only parameter.
# For example, the instruction 4,50 would output the value at address 50.
