input_d6 = open("day_6/day6.txt", "r").read().split("\n")[:-1]

def verifying_if_some_orbit_around_many(mydict):
    print("for loop")
    for elem in (list(mydict.values())):
        if len(elem) != 1:
            print(elem)
    else:
        return False
# print(verifying_if_some_orbit_around_many(mydict))

def nb_of_orbits_1_letter(initial_letter, mydict):
    # let's count the number of direct and indirect orbits

    nb_of_orbits = 0
    print(initial_letter, end="-- ")
    try:
        direct_orbit = mydict[initial_letter]
        print("direct_orbit", direct_orbit[0])
        nb_of_orbits += 1
        indirect_orbit = direct_orbit[0]
        try:
            while mydict[indirect_orbit][0] != None:
                print("indirect_orbit",mydict[indirect_orbit][0])
                indirect_orbit = mydict[indirect_orbit][0]
                nb_of_orbits += 1
        except KeyError:
            pass
    except KeyError:
        nb_of_orbits = 0

    print("nb_of_orbits:", nb_of_orbits)
    return nb_of_orbits

def part1(input_d6):
    mydict = {}
    for elem in input_d6:
        value, key = elem.split(")")
        if key not in mydict:
            mydict[key] = []
            mydict[key].append(value)
        else:
            mydict[key].append(value)

    total_orbits = []
    for key in mydict:
        total_orbits.append(nb_of_orbits_1_letter(key, mydict))

    return(sum(total_orbits))


# Part 2

def nb_of_orbits_1_letter_p2(initial_letter, mydict):
    # let's count the number of direct and indirect orbits

    nb_of_orbits = 0
    orbits = []
    # print(initial_letter, end="-- ")
    try:
        direct_orbit = mydict[initial_letter]
        # print("direct_orbit", direct_orbit[0])
        nb_of_orbits += 1
        indirect_orbit = direct_orbit[0]
        try:
            while mydict[indirect_orbit][0] != None:
                # print("indirect_orbit",mydict[indirect_orbit][0])
                orbits.append(indirect_orbit)
                indirect_orbit = mydict[indirect_orbit][0]
                nb_of_orbits += 1
        except KeyError:
            pass
    except KeyError:
        nb_of_orbits = 0

    # print("nb_of_orbits:", nb_of_orbits)
    return nb_of_orbits, orbits





def crossover(mydict):
    nb_of_orbitsY, orbitsY = (nb_of_orbits_1_letter_p2("YOU", mydict))
    nb_of_orbitsS, orbitsS = (nb_of_orbits_1_letter_p2("SAN", mydict))

    # print("orbitsY: ", orbitsY)
    # print("orbitsS:",orbitsS, end="\n\n")

    for elemY in orbitsY:
        for elemS in orbitsS:
            if elemY == elemS:
                return elemS, orbitsY, orbitsS

def part2(input_d6):
    mydict = {}
    for elem in input_d6:
        value, key = elem.split(")")
        # print(key, value)
        if key not in mydict:
            mydict[key] = []
            mydict[key].append(value)
        else:
            mydict[key].append(value)

    elemS, orbitsY, orbitsS = (crossover(mydict))
    print("crossover:", elemS)

    count = 0
    for elem in orbitsY:
        if elem != elemS:
            count += 1
        else:
            break
    for elem in orbitsS:
        if elem != elemS:
            count += 1
        else:
            break

    print("minimum number of orbital transfers required:", count)

part2(input_d6)
