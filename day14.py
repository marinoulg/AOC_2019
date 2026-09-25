from pprint import pprint
from fractions import Fraction

# GOAL : Produce a list of the reactions the factory can perform that are relevant
# to turn raw materials (your puzzle input) into fuel.

# Every reaction turns some quantities of specific input chemicals into some
# quantity of an output chemical.

# Almost every chemical is produced by exactly one reaction;
# the only exception, ORE, is the raw material input to the entire process and
# is not produced by a reaction.
# You just need to know how much ORE you'll need to collect before you can
# produce one unit of FUEL.

# Each reaction gives specific quantities for its inputs and output;
# reactions cannot be partially run, so only whole integer multiples of
# these quantities can be used.
# It's okay to have leftover chemicals when you're done, though.

# You just need to know how much ORE you'll need to collect before you can
# produce one unit of FUEL.

def create_my_dict(input_ex):
    my_dict = {}
    for elem in input_ex:
        a,b = (elem.split(" => "))
        my_dict[a.replace(",", " +")] = b

    return(my_dict)

def recursion(end, my_dict):
    for k,v in my_dict.items():
        if v == end:
            if "+" in k:
                # a,b = (k.split(" + "))
                # print((a,b))
                return(k.split(" + "))
                # # (end)
                # for k,v in my_dict.items():
                #     if a and b in my_dict.values():
                #         return (a,b)
                #     elif a in my_dict.values():
                #         return (a)
                #     elif b in my_dict.values():
                #         return (b)

def do_recursion(end, my_dict):
    my_need = []
    # end = "1 FUEL"
    # print(recursion("1 FUEL"))
    for elem in (recursion(end, my_dict)):
        my_need.append(elem)
    for elem in my_need:
        print(elem)
        if recursion(elem, my_dict) != None:
            my_need.remove(elem)
            for el in recursion(elem, my_dict):
                my_need.append(el)
    return(my_need)

def know_how_much_per_quantity(my_need):
    unit_quantity = {}
    for elem in my_need:
        quant, unit = elem.split(" ")
        if unit not in unit_quantity:
            unit_quantity[unit] = []
        unit_quantity[unit].append(int(quant))

    # pprint(unit_quantity)
    for elem in unit_quantity:
        unit_quantity[elem] = sum(unit_quantity[elem])

    return(unit_quantity)

def find_total_ORE(my_dict, unit_quantity):
    total_needed = []
    for k,v in my_dict.items():
        for key in unit_quantity.keys():
            if key in v:
                print((k,v))
                u,q = (v.split(" "))
                u = int(u)
                k,_ = (k.split(" ORE"))
                total_needed.append((round(unit_quantity[key] / u )*int(k)))

    return(sum(total_needed))

input_ex = open("day_14/ex1day14.txt", "r").read().split("\n")[:-1]

print(input_ex)
my_dict = create_my_dict(input_ex)
pprint(my_dict)
my_need = do_recursion(end="1 FUEL", my_dict=my_dict)
unit_quantity = know_how_much_per_quantity(my_need)
print(find_total_ORE(my_dict, unit_quantity))
