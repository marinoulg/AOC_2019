# position 0 : you will find an opcode - either 1, 2, or 99.

# The opcode indicates what to do;
    # Opcode 1 : adds together numbers read from two positions and stores the result in a third position.
    # Opcode 2 : multiplies together numbers read from two positions and stores the result in position 0.
    # Opcode 99 : the program is finished and should immediately halt.
    # Encountering an unknown opcode means something went wrong.

# Attention : the three integers after the opcode indicate where the inputs and outputs are, not their values.


# Opcode 1 :
# The three integers immediately after the opcode tell you these three positions -
# the first two indicate the positions from which you should read the input values,
# and the third indicates the position at which the output should be stored.
# For example, if your Intcode computer encounters 1,10,20,30, it should read the
# values at positions 10 and 20, add those values, and then overwrite the value
# at position 30 with their sum.

# Opcode 2 :
# Opcode 2 works exactly like opcode 1, except it multiplies the two inputs
# instead of adding them.

# Once you're done processing an opcode, move to the next one by stepping forward 4 positions.


input = open("day_2/exday2.txt", "r").read().split("\n")
ex1 = input[0].split(",")
ex2 = input[1].split(",")
ex3 = input[2].split(",")
ex4 = input[3].split(",")
ex5 = input[4].split(",")
ex6 = input[5].split(",")

# print(ex1)
def getstarted(ex1):
    integers = []
    for elem in ex1:
        elem = int(elem)
        integers.append(elem)
    return integers

def update_by4_list(integers):
    by_4_list = []
    old_pos = 0
    for pos in range(len(integers)):
        tmp = []
        if pos%4 == 0:
            tmp.append(integers[old_pos:pos])
            old_pos = pos
        if tmp != []:
            by_4_list.append(tmp[0])
    by_4_list.append(integers[old_pos:])
    by_4_list.pop(0)
    # print(by_4_list)
    return by_4_list

def getpart1(ex1):
    integers = getstarted(ex1)
    # print(integers)
    by_4_list = update_by4_list(integers)
    # print(by_4_list)

    for l in range(len(by_4_list)):
        # print()
        for elem in by_4_list[l:]:
            print(by_4_list[l:])
            opcode = (elem[0])
            if opcode == 1:
                print("opcode", opcode, end = "; ")
                pos1, pos2, pos3 = elem[1], elem[2], elem[3]
                # print(pos1, pos2, pos3 )
                res = integers[pos1] + integers[pos2]
                integers.pop(pos3)
                integers.insert(pos3,res)
                # print(integers)
                print("first:", integers[0])
                by_4_list = update_by4_list(integers)
                break
            if opcode == 2:
                    # multiplication
                    print("opcode", opcode, end = "; ")
                    pos1, pos2, pos3 = elem[1], elem[2], elem[3]
                    res = integers[pos1] * integers[pos2]
                    integers.pop(pos3)
                    integers.insert(pos3,res)
                    # print(integers)
                    print("first:", integers[0])
                    by_4_list = update_by4_list(integers)
                    break
            if opcode == 99:
                # print(integers)
                print("first:", integers[0])
                by_4_list = update_by4_list(integers)
                break
            else:
                break
    return(integers)


# print("...........")
# print()
# print("Ex1", getpart1(ex1))
# print("...........")
# print()
# print("Ex2",getpart1(ex2))
# print("...........")
# print()
# print("Ex3",getpart1(ex3))
# print("...........")
# print()
# print("Ex4",getpart1(ex4))
# print("...........")
# print()
# print("Ex5",getpart1(ex5))
# print()
# print("Ex6",getpart1(ex6))

# print("----------------------------------------------------")
# --------------------------


# on real input
# input = open("day_2/day2.txt", "r").read().split(",")
# print()
# # To do this, before running the program,
# # replace position 1 with the value 12 and
# input.pop(1)
# input.insert(1,12)
# # replace position 2 with the value 2.
# input.pop(2)
# input.insert(2,2)
# # What value is left at position 0 after the program halts
# # print("List to deal with", integers)
# # print("------")

# print(getpart1(input)[0])

# -------------- Part 2 --------------
# When you run an Intcode program, make sure to start by initializing memory to
# the program's values.
# A position in memory is called an address
# (for example, the first value in memory is at "address 0").

# Opcodes (like 1, 2, or 99) mark the beginning of an instruction.
# The values used immediately after an opcode, if any, are called the instruction's parameters.
# For example, in the instruction ```1,2,3,4````, 1 is the opcode; 2, 3, and 4 are the parameters.
# The instruction 99 contains only an opcode and has no parameters.

# The address of the current instruction is called the instruction pointer;
# it starts at 0.
# After an instruction finishes, the instruction pointer increases by
# the number of values in the instruction;
# until you add more instructions to the computer, this is always 4
# (1 opcode + 3 parameters) for the add and multiply instructions.
# (The halt instruction would increase the instruction pointer by 1,
# but it halts the program instead.)

# In this program, the value placed in address 1 is called the noun,
# and the value placed in address 2 is called the verb.
# Each of the two input values will be between 0 and 99, inclusive.

# Once the program has halted, its output is available at address 0, also just like before.
# Each time you try a pair of inputs, make sure you first reset the computer's
# memory to the values in the program (your puzzle input) -
# in other words, don't reuse memory from a previous attempt.

# Find the input noun and verb that cause the program to produce the output 19690720.
# What is 100 * noun + verb?
# (For example, if noun=12 and verb=2, the answer would be 1202.)

# print(end="\n\n\n")

input = open("day_2/exbasicday2.txt", "r").read().split(",")

integers = getstarted(input)
print(integers)
print()
# To do this, before running the program,
# replace position 1 with the value 12 and
input.pop(1)
input.insert(1,12)
# replace position 2 with the value 2.
input.pop(2)
input.insert(2,2)
# What value is left at position 0 after the program halts
# print("List to deal with", integers)
# print("------")

print(getpart1(input))
