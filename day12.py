from pprint import pprint
input_ex = open("day_12/exday12.txt", "r").read().split("\n")[:-1]
# print(input_ex)

def create_dict_of_moons(input_ex):
    # 4 moons: Io, Europa, Ganymede, Callisto
    # Each moon has a 3-dimensional position (x, y, and z) and a 3-dimensional velocity.
    # the x, y, and z velocity of each moon starts at 0.

    my_dict = {}
    moons = ["Io", "Europa", "Ganymede", "Callisto"]
    for moon in moons:
        if moon not in my_dict:
            my_dict[moon] = [] # list composed of dicts {"position":(x,y,z), "velocity"=(x,y,z)}
            # so that my_dict[moon][0] is the first step, and my_dict[moon][1] is the 2nd step in current_step etc.

    # # Apply 1syt velocity -> is 0
    for i,k in enumerate(my_dict.keys()):
        # print(i, k)
        moon = input_ex[i].replace("<",'').replace(">","").split(', ')
        tmp = []
        for elem in moon:
            a,b = (elem.split("="))
            b = int(b)
            tmp.append(b)
        my_dict[k].append({"position":tuple(tmp), "velocity":(0,0,0)})

    return (my_dict)

def initialize_new_step(my_dict):
        for elem in my_dict:
            my_dict[elem].append({"position":(0,0,0), "velocity":(0,0,0)})
        return my_dict

def tmp_velocities_2_moons(moon1_str:str,
                           moon2_str:str,
                           current_step:int):

    # update temporary velocities between 2 moons

    # smallest one + 1
    # biggest one - 1

    moon1 = (my_dict[moon1_str])
    moon2 = (my_dict[moon2_str])

    iteration = 0
    l_moon1 = list(moon1[current_step]["velocity"])
    l_moon2 = list(moon2[current_step]["velocity"])

    # problem is here
    # bc it compares everything together
    for coord_moon1, coord_moon2 in zip(moon1[current_step]["position"], moon2[current_step]["position"]):
        print("iteration:",iteration)
        print("comparing:", coord_moon1, coord_moon2)
        if coord_moon1 > coord_moon2:
            tmp_moon1 = l_moon1[iteration]
            # print(l_moon1)
            l_moon1.insert(iteration, tmp_moon1-1)
            l_moon1.pop(iteration+1)

            tmp_moon2 = l_moon2[iteration]
            l_moon2.insert(iteration, tmp_moon2+1)
            l_moon2.pop(iteration+1)
            # print(l_moon1)
            # break

        elif coord_moon1 < coord_moon2:
            tmp_moon1 = l_moon1[iteration]
            # print(l_moon1)
            l_moon1.insert(iteration, tmp_moon1+1)
            l_moon1.pop(iteration+1)

            tmp_moon2 = l_moon2[iteration]
            l_moon2.insert(iteration, tmp_moon2-1)
            l_moon2.pop(iteration+1)
            # print(l_moon1)
            # break
        print()


        iteration+=1
        if iteration>1:
            continue
    # print(f"--- Temporary velocities for step {current_step+1} between {moon1_str} and {moon2_str} are ---")
    tmp_velocity_moon1 = tuple(l_moon1)
    tmp_velocity_moon2 = tuple(l_moon2)

    print(moon1_str,":", tmp_velocity_moon1)
    print(moon2_str,":", tmp_velocity_moon2)
    print()


    return tmp_velocity_moon1, tmp_velocity_moon2

def comparing_1_moon_to_others_for_future_velocity(moon_comparing,
                                                   moon_compared,
                                                   current_step,
                                                   temporary_velocities):

    for elem in my_dict:
        if elem not in temporary_velocities:
            temporary_velocities[elem] = []
        if elem != moon_comparing and elem not in moon_compared:
            # print(f"{elem} being compared to {moon_comparing}")
            tmp_velocity_moon1, tmp_velocity_moon2 = tmp_velocities_2_moons(moon_comparing, elem, current_step)
            # print(f"tmp_velocities_2_moons of Io is: {tmp_velocity_moon1}")
            temporary_velocities[moon_comparing].append(tmp_velocity_moon1)
            temporary_velocities[elem].append(tmp_velocity_moon2)

    return temporary_velocities, moon_compared

def apply_gravity(my_dict,
                   current_step):

    # STEP 1: update the velocity of every moon by applying gravity.
    # GOAL: change velocities for next step
    # smallest one + 1
    # biggest one - 1

    # To apply gravity, consider every pair of moons.
    # On each axis (x, y, and z), the velocity of each moon changes by exactly +1 or -1 to pull the moons together.

    # For example, if Ganymede has an x position of 3, and Callisto has a x position of 5,
    # then Ganymede's x velocity changes by +1 (because 5 > 3) and
    # Callisto's x velocity changes by -1 (because 3 < 5).

    # However, if the positions on a given axis are the same,
    # the velocity on that axis does not change for that pair of moons.

    my_dict = initialize_new_step(my_dict)
    print(f"---------- Current step is {current_step} ----------")

    temporary_velocities = {}
    moon_compared = []

    for moon in my_dict:
        moon_compared.append(moon)
        temporary_velocities, moon_compared = comparing_1_moon_to_others_for_future_velocity(moon,
                                                                                             moon_compared,
                                                                                             current_step,
                                                                                             temporary_velocities)
    for elem in temporary_velocities:
        # print(elem)
        first_comp = temporary_velocities[elem][0]
        secd_comp = temporary_velocities[elem][1]
        third_comp = temporary_velocities[elem][2]
        actual_velocities = ((first_comp[0]+secd_comp[0]+third_comp[0], first_comp[1]+secd_comp[1]+third_comp[1], first_comp[2]+secd_comp[2]+third_comp[2]))
        my_dict[elem][current_step+1]["velocity"] = actual_velocities

    return my_dict

def apply_velocity_aka_change_positions_nextstep(my_dict, current_step):
    # STEP 2: once all moons' velocities have been updated,
    # update the position of every moon by applying velocity.

    # simply add the velocity of each moon to its own position.

    # For example, if Europa has a position of x=1, y=2, z=3 and a velocity of x=-2, y=0,z=3,
    # then its new position would be x=-1, y=2, z=6.
    # This process does not modify the velocity of any moon.

    my_dict = apply_gravity(my_dict, current_step)

    for elem in my_dict:
        # print(elem)
        first_comp = (my_dict[elem][current_step]["position"])
        secd_comp = (my_dict[elem][current_step+1]["velocity"])

        new_pos = ((first_comp[0]+secd_comp[0],first_comp[1]+secd_comp[1],
                    first_comp[2]+secd_comp[2]))
        my_dict[elem][current_step+1]["position"] = new_pos

    return(my_dict)

my_dict = create_dict_of_moons(input_ex)
pprint(my_dict)

current_step=0
my_dict = apply_velocity_aka_change_positions_nextstep(my_dict, current_step)
pprint(my_dict)

# Time progresses by one step once all of the positions are updated.
current_step += 1

my_dict = apply_velocity_aka_change_positions_nextstep(my_dict, current_step)
pprint(my_dict)
