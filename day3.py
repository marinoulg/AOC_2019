input = open("exday3.txt", "r").read().split("\n")
instr1 = input[0].split(",")
instr2 = input[1].split(",")



O = (1,1)

def end_location(instr, where_am_i):
    for elem in instr:
        if elem.startswith("R"):
            where_am_i = (where_am_i[0]+int(elem[1:]), where_am_i[1])
        elif elem.startswith("L"):
            where_am_i = (where_am_i[0]-int(elem[1:]), where_am_i[1])

        elif elem.startswith("U"):
            where_am_i = (where_am_i[0], where_am_i[1]+int(elem[1:]))
        elif elem.startswith("D"):
            where_am_i = (where_am_i[0], where_am_i[1]-int(elem[1:]))
    return (where_am_i)

# print("end instr1", end_location(instr1, O))
# print("end instr2", end_location(instr2, O))

where_am_i = (1,1)

def stocking_instructions(instr, where_am_i):
    stock = []
    for elem in instr:
        if elem.startswith("R"):
            for _ in range(int(elem[1:])):
                where_am_i = (where_am_i[0]+1, where_am_i[1])
                stock.append(where_am_i)
            # print(where_am_i)

        elif elem.startswith("L"):
            for _ in range(int(elem[1:])):
                where_am_i = (where_am_i[0]-1, where_am_i[1])
                stock.append(where_am_i)
            # print(where_am_i)


        elif elem.startswith("U"):
            for _ in range(int(elem[1:])):
                where_am_i = (where_am_i[0], where_am_i[1]+1)
                stock.append(where_am_i)
            # print(where_am_i)

        elif elem.startswith("D"):
            for _ in range(int(elem[1:])):
                where_am_i = (where_am_i[0], where_am_i[1]-1)
                stock.append(where_am_i)
            # print(where_am_i)

    return ((sorted(list(set(stock))))),where_am_i
    # return (stock),where_am_i

stock1,where_am_i1 = stocking_instructions(instr1, O)
stock2,where_am_i2 = stocking_instructions(instr2,O)

# # s1 = stock1.sort(key=lambda tup: tup[1], reverse=True)

print(instr1)
print(stock1)
print()
print(instr2)
print(stock2)

# similar_coordinates = []

# if stock1[0][0] < stock2[0][0]:
#     stock_small = (stock1.copy())
#     stock_big = (stock2.copy())
# else:
#     stock_small = (stock2.copy())
#     stock_big = (stock1.copy())


# while stock_small[0][0]!=stock_big[0][0]:
#     stock_small.pop(0)
#     stock_small = sorted(stock_small)

print("------")
# print(stock_small)
# print()
# print(stock_big)


# for elem1 in sorted(stock_small):
#     elem2 = sorted(stock_big)[0]
#     # it_1+=1
#     while elem1[0] == elem2[0]:
#         for elem2 in sorted(stock_big):
#             print(elem1, elem2)
#             if elem2 == elem1:
#                 similar_coordinates.append(elem1)
#             elif elem2[0]>elem1[0]:
#                 break
#             else:
#                 # it_2 +=1
#                 next



# print("------")
# # print(it_1, it_2)
# print(stock_small)
# print()
# print(stock_big)


# by batches
batch1 = []
old_a = 1

def create_dict_for_stocks(stock):
    mydict = {}
    for elem in sorted(stock):
        a,b = elem
        # print((a,b))
        if a not in mydict:
            mydict[a] = []
            mydict[a].append((a,b))
        else:
            mydict[a].append((a,b))

    return (mydict)

mydict1 = create_dict_for_stocks(stock1)
mydict2 = create_dict_for_stocks(stock2)

# comparing dict keys both ways
tmp1 = []
for elem in (list(mydict1.keys())):
    if elem not in (list(mydict2.keys())):
        tmp1.append(elem)
tmp2 = []
for elem in (list(mydict2.keys())):
    if elem not in (list(mydict1.keys())):
        tmp2.append(elem)

for elem in tmp1:
    mydict1.pop(elem)

for elem in tmp2:
    mydict2.pop(elem)

print(mydict1)
print()
print(mydict2)
