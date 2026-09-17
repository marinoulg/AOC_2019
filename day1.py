input = open("day1.txt", "r").read().split("\n")[:-1]
# print(input)

# --------- PART 1 ---------
def fuel_needed(elem:str):
    # transform into an integer
    elem = int(elem)
    # divide by three
    tmp = (round(elem/3,2))
    # round down
    tmp = int(tmp)
    # subtract 2
    final = (tmp - 2)
    return(final)

integers = []
for elem in input:
    final = fuel_needed(elem)
    integers.append(final)

# print("final sum is", sum(integers))

# --------- PART 2 ---------
integers = []
for elem in input:
    tmps = []
    tmp = fuel_needed(elem)
    tmps.append(tmp)
    while tmp > 0:
        tmp = fuel_needed(tmp)
        tmps.append(tmp)
    for elem in tmps:
        if elem <= 0:
            tmps.remove(elem)
    integers.append(sum(tmps))

print("final sum is", sum(integers))
