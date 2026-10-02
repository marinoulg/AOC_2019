from day2 import *

input_d2 = open("day_2/exbasicday2.txt", "r").read().replace("\n","").split(",")
input_d4 = open("day_5/exday5.txt", "r").read().replace("\n","").split(",")
input_d4bis = open("day_5/ex2day5.txt", "r").read().replace("\n","").split(",")

print(input_d2)
integers = (getstarted(input_d2))
by_4_list = update_by4_list(integers)
print("by_4_list:",by_4_list)
print("integers:", integers)

def transform_str_to_readable_opcode(elem):
    # elem = "1002"
    opcode = elem[-2:]

    if len(elem) < 5:
        res = 5 - len(elem)
        elem = (elem+"0"*res)

    param_modes = []
    for c in elem[:-2]:
        param_modes.append(int(c))

    return (opcode, param_modes)

def which_opcode(opcode,
                 elem, integers,
                 parameter_modes = [0,0,0]):
    if opcode == 1:
        by_4_list = opcode1(elem, integers, parameter_modes)
        return by_4_list
    if opcode == 2:
        by_4_list = opcode2(elem, integers, parameter_modes)
        return by_4_list
    if opcode == 99:
        by_4_list = update_by4_list(integers)
        return by_4_list

def from_by4_to_integers(by_4_list):
    integers = []
    for elem in (str(by_4_list).replace(']',"").replace('[',"").split(", ")):
        integers.append(int(elem))
    return integers

for i in range(len(by_4_list)):
    elem = by_4_list[i]
    print("elem:", elem)

    opcode, param_modes = (transform_str_to_readable_opcode(str(elem[0])))
    print("opcode:", opcode)
    print("param_modes:", param_modes)
    by_4_list = (which_opcode(int(opcode),
                    elem,
                    integers,
                    # parameter_mode=param_modes
                    )
                 )
    integers = from_by4_to_integers(by_4_list)
    print(integers)

print()
(part1(only_ex1=True))

def opcode3(
            # input_integer,
            # parameter,
            elem,
            integers,
            parameter_modes=[0,0,0]):

    parameter_mode_pos1, parameter_mode_pos2, parameter_mode_pos3 = parameter_modes
    pos1, pos2, pos3 = elem[1], elem[2], elem[3]

    # Opcode 3 : takes a single integer as input and saves it to the position given
    # by its only parameter.
    # For example, the instruction ```3,50```` would take an input value and store
    # it at address 50.

    # What it looks like: ```3, 50```` (takes 1 parameter).
    # # What it does: It pauses the program and waits for the user (you)
    # to type in an integer.
    # Once you type it, it takes that number and stores it at the memory address
    # given by its parameter.
    # In ```3, 50````, it would wait for your input and save it into address 50.
    # It uses 2 values total (1 opcode + 1 parameter).


    by_4_list = update_by4_list(integers)
    return by_4_list

def opcode4(output_value,
            parameter,
            integers,
            parameter_modes=[0,0,0]):

    parameter_mode_pos1, parameter_mode_pos2, parameter_mode_pos3 = parameter_modes
    pos1, pos2, pos3 = elem[1], elem[2], elem[3]

    # Opcode 4: outputs the value of its only parameter.
    # For example, the instruction ```4,50```` would output the value at address 50.

    # What it looks like: ```4```, 50 (takes 1 parameter).
    # What it does: It reads a value from memory (depending on its parameter mode)
    # and prints/outputs it to the screen.
    # In ```4, 50````, if mode is position mode, it looks at whatever is
    # inside address 50 and outputs it.
    # It uses 2 values total (1 opcode + 1 parameter).

    by_4_list = update_by4_list(integers)
    return by_4_list





# Parameter modes are stored in the same value as the instruction's opcode.

# The opcode is a two-digit number based only on the ones and tens digit of the value,
# that is, the opcode is the rightmost two digits of the first value in an instruction.

# Example: consider the program 1002,4,3,4,33.
# // 1st number in program, aka 1002:
# Opcode is: ```02````

# Parameter modes are single digits, one per parameter, read right-to-left from the opcode:
# the first parameter's mode is in the hundreds digit,
# the second parameter's mode is in the thousands digit,
# the third parameter's mode is in the ten-thousands digit, and so on.
# Any missing modes are 0.

# Attention: always at least 3 parameters!

# Example:
# first parameter's mode is 0
# the second parameter's mode is 1
# the third parameter's mode is None, hence 0
