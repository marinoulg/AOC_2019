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
    # print(initial_letter, end="-- ")
    try:
        direct_orbit = mydict[initial_letter]
        # print("direct_orbit", direct_orbit[0])
        nb_of_orbits += 1
        indirect_orbit = direct_orbit[0]
        try:
            while mydict[indirect_orbit][0] != None:
                # print("indirect_orbit",mydict[indirect_orbit][0])
                indirect_orbit = mydict[indirect_orbit][0]
                nb_of_orbits += 1
        except KeyError:
            pass
    except KeyError:
        nb_of_orbits = 0

    # print("nb_of_orbits:", nb_of_orbits)
    return nb_of_orbits

def part1(input_d6):
    mydict = {}
    for elem in input_d6:
        value, key = elem.split(")")
        # print(key, value)
        if key not in mydict:
            mydict[key] = []
            mydict[key].append(value)
        else:
            mydict[key].append(value)

    # print()
    # print(mydict)

    total_orbits = []
    for key in mydict:
        total_orbits.append(nb_of_orbits_1_letter(key, mydict))

    # print(total_orbits)
    return(sum(total_orbits))

print(part1(input_d6))
