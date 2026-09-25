from pprint import pprint
from fractions import Fraction
import math

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
                a,b = (k.split(" + "))
                return((a,b))
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

# print(input_ex)
# my_dict = create_my_dict(input_ex)
# my_need = do_recursion(end="1 FUEL", my_dict=my_dict)
# unit_quantity = know_how_much_per_quantity(my_need)
# print(find_total_ORE(my_dict, unit_quantity))

# ------- nouveau test - tout réduire à 1 unité --------

def initialize_dict(input_ex):
    my_dict = {}
    for elem in input_ex:
        a,b = (elem.split(" => "))
        if b not in my_dict: my_dict[b] = []
        my_dict[b].append(a.replace(",", " +"))
    return my_dict

def reduce_fractions(num1, num2):
    ent,virg = (str(num1/num2)).split(".")
    if len(virg) > 4:
        return False
        # return(Fraction(num1,num2))
    else:
        return True
        # return(num1/num2)

def all_1units_in_dict(my_dict):
    # insert keys of f"1 {u_maj}" if they do not exist
    keys_to_append = []
    for key in my_dict:
        q_maj, u_maj = key.split(" ")
        if f"1 {u_maj}" not in my_dict:
            keys_to_append.append((f"1 {u_maj}"))

    for key in keys_to_append:
        if key not in my_dict:
            my_dict[key] = []

    # have all major keys be in f"1 {u_maj}" with their corresponding float equivalent as value
    for key,value in my_dict.items():
        q_maj, u_maj = key.split(" ")
        q_maj = float(q_maj)
        # print(q_maj, u_maj)
        if " + " in value[0]: # only 1 values in list for now, bc just created the list
            tmp_list = (value[0].split(" + "))
            for i in range(len(tmp_list)):
                (pair_q_u) = tmp_list[i]
                q,u = pair_q_u.split(" ")
                tmp_list.pop(i)
                q = float(q)
                if reduce_fractions(q, q_maj) == True:
                    tmp_list.insert(i,{f"1 {u}":(q/q_maj)})
                else:
                    tmp_list.insert(i,{f"1 {u}":Fraction(q/q_maj)})
                # my_dict[f"1 {u_maj}"] = (tmp_list) mais : RuntimeError: dictionary changed size during iteration
                if key != f"1 {u_maj}":
                    my_dict[f"1 {u_maj}"] = (tmp_list)
                    my_dict[key] = []
                else: my_dict[key] = (tmp_list)

        else:
            if " " in value[0]:
                # tmp_list = ()
                q,u = value[0].split(" ")
                value.pop(0)
                q = float(q)
                if reduce_fractions(q, q_maj) == True:
                    value.insert(0,{f"1 {u}":(q/q_maj)})
                else:
                    value.insert(0,{f"1 {u}":Fraction(q/q_maj)})
                # my_dict[f"1 {u_maj}"] = (value) mais : RuntimeError: dictionary changed size during iteration
                if key != f"1 {u_maj}":
                    my_dict[f"1 {u_maj}"] = (value)
                    my_dict[key] = []
                else: my_dict[key] = (value)

    # Drop the keys that are no longer in format f"1 {u_maj}"
    to_pop = []
    for key in my_dict:
        if my_dict[key] == list():
            to_pop.append(key)

    for elem in to_pop:
        my_dict.pop(elem)

    return(my_dict)

input_ex = open("day_14/exday14.txt", "r").read().split("\n")[:-1]

original_dict = initialize_dict(input_ex)
my_dict = original_dict.copy()
pprint(my_dict)
print()
my_dict = all_1units_in_dict(my_dict)
pprint(my_dict)
print()

def recursion(key_to_find, my_dict):
    # key_to_find = "1 FUEL"
    for key,value in my_dict.items():
        if key == key_to_find:
            return (key, value)

def do_recursion(my_dict, keys,
                 list_to_apply_recursion_on=my_dict):
    # print("list_to_apply_recursion_on:", list_to_apply_recursion_on)
    for elem in list_to_apply_recursion_on:
        key = list(elem.keys())[0]
        # print("key:", key)
        key, v = recursion(key, my_dict)
        # print(my_dict[key])
        if len(my_dict[key]) == 1:
            keys.append((key, elem[key]))
        else:
            # print(key, end=": ")
            key, v = recursion(key, my_dict)
            # print(my_dict[key])
        # print()
    return keys, my_dict[key]

key_to_find = "1 FUEL"
key, list_to_apply_recursion_on = recursion(key_to_find, my_dict)
# print(key, end=": ")
# print(list_to_apply_recursion_on)

keys = []
try:
    for _ in range(1000):
        key, list_to_apply_recursion_on = do_recursion(my_dict, keys, list_to_apply_recursion_on)
except TypeError:
    pass

print("keys:", keys)
tmp_dict = {}
for pair in keys:
    u,q = pair
    if u not in tmp_dict: tmp_dict[u] = []
    tmp_dict[u].append(q)
print(tmp_dict)

for elem in tmp_dict:
    tmp_dict[elem] = sum(tmp_dict[elem])
print(tmp_dict)

print()

original_dict = initialize_dict(input_ex)
pprint(original_dict)
