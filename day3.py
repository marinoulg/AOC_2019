input = open("day3.txt", "r").read().split("\n")


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

    # print(stock)
    return (stock),where_am_i
    # return (stock),where_am_i

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

def comparing_dict_keys(mydict1,mydict2):
    # comparing dict keys both ways
    tmp1 = []
    for elem in (list(mydict1.keys())):
        if elem not in (list(mydict2.keys())):
            tmp1.append(elem)
    tmp2 = []
    for elem in (list(mydict2.keys())):
        if elem not in (list(mydict1.keys())):
            tmp2.append(elem)
    return tmp1, tmp2

def deleting_useless_keys(mydict1,mydict2,
                          tmp1,tmp2):
    # deleting useless keys both ways
    for elem in tmp1:
        mydict1.pop(elem)

    for elem in tmp2:
        mydict2.pop(elem)
    return mydict1, mydict2

def manhattan_distance(coords1, coords2):
        x1, y1 = coords1
        x2, y2 = coords2
        return abs(x1-x2)+abs(y1-y2)

def part1(input):
    O = (1,1)
    where_am_i = (1,1)

    instr1 = input[0].split(",")
    instr2 = input[1].split(",")
    stock1,where_am_i1 = stocking_instructions(instr1, O)
    stock2,where_am_i2 = stocking_instructions(instr2,O)

    mydict1 = create_dict_for_stocks(stock1)
    mydict2 = create_dict_for_stocks(stock2)
    tmp1, tmp2 = comparing_dict_keys(mydict1,mydict2)
    mydict1,mydict2 = deleting_useless_keys(mydict1,mydict2,tmp1,tmp2)

    # print(instr1)
    # print(stock1)
    # print()
    # print(instr2)
    # print(stock2)

    similar_coordinates = []
    for key in mydict1.keys():
        for elem1 in (mydict1[key]):
            for elem2 in mydict2[key]:
                if elem1 == elem2:
                    similar_coordinates.append(elem1)

    distances = {}
    for coord in similar_coordinates:
        distances[(manhattan_distance(O,coord))] = coord

    return stock1, stock2,distances

print()
stock1, stock2,distances = (part1(input))
print("Answer part 1:", sorted(list(distances.keys()))[0])
print()

def counting_iterations_to_get_to_cross(stock, coordinate):
    it = 1
    for elem in (stock):
        if elem != coordinate:
            it +=1
        else: break
    return it

steps = []
for elem in (list(distances.values())):
    steps.append(counting_iterations_to_get_to_cross(stock1,elem)+counting_iterations_to_get_to_cross(stock2,elem))

print(sorted(steps)[0])
