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


input = open("exday2.txt", "r").read().split("\n")
ex1 = input[0].split(",")
ex2 = input[1].split(",")
ex3 = input[2].split(",")
ex4 = input[3].split(",")
ex5 = input[4].split(",")

# print(ex1)
def getstarted(ex1):
    integers = []
    for elem in ex1:
        elem = int(elem)
        integers.append(elem)

    print("List to deal with", integers)
    print("------")
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
    return by_4_list



def opcode1(integers, by_4_list):
    # print("List by Opcode", by_4_list)
    # print("------")

    for elem in by_4_list:
        opcode = (elem[0])
        if opcode == 1:
            # addition
            pos1, pos2, pos3 = elem[1], elem[2], elem[3]
            res = integers[pos1] + integers[pos2]
            integers.pop(pos3)
            integers.insert(pos3,res)
    return integers

def opcode2(integers, by_4_list):
    for elem in by_4_list:
        opcode = (elem[0])
        # print("poc2", opcode)
        if opcode == 2:
            # multiplication
            pos1, pos2, pos3 = elem[1], elem[2], elem[3]
            res = integers[pos1] * integers[pos2]
            integers.pop(pos3)
            integers.insert(pos3,res)
    return integers

def opcode99(integers, by_4_list):
    for elem in by_4_list:
        opcode = (elem[0])
        if opcode == 99:
            # program is finished and should immediately halt
            break

        # else:
        #     # Encountering an unknown opcode means something went wrong.
        #     print("Error in opcode")
        # print(integers)

def part1(ex1):
    integers = getstarted(ex1)
    print(integers)
    by_4_list = update_by4_list(integers)

    ints = integers.copy()
    while ints != None :
        # print("opcode1")
        integers = opcode1(integers, by_4_list)
        by_4_list = update_by4_list(integers)
        # print(integers)

        # print("opcode2")
        integers = opcode2(integers, by_4_list)
        by_4_list = update_by4_list(integers)
        # print(integers)

        # print("opcode3")
        ints = opcode99(integers, by_4_list)
        # print(ints)

    return (integers[0])

print("...........")
print()
print("Ex1", part1(ex1))
print("...........")
print()
print("Ex2",part1(ex2))
print("...........")
print()
print("Ex3",part1(ex3))
print("...........")
print()
print("Ex4",part1(ex4))
print("...........")
print()
print("Ex5",part1(ex5))
