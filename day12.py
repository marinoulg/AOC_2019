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

def initialize_first_step(my_dict):
    for elem in my_dict:
        my_dict[elem].append({"position":(0,0,0), "velocity":(0,0,0)})
    return my_dict

def initialize_new_step(my_dict, current_step):
    for elem in my_dict:
        my_dict[elem].append(my_dict[elem][current_step].copy())
    return my_dict

def tmp_velocities_2_moons_v2(my_dict,
                              moon1_str:str,
                           moon2_str:str,
                           current_step:int):

    # update temporary velocities between 2 moons

    # smallest one + 1
    # biggest one - 1

    tmp_moon1, tmp_moon2 = [],[]
    # print("tmp_moon1 is for", moon2_str)
    moon1 = (my_dict[moon1_str])
    moon2 = (my_dict[moon2_str])

    if moon1_str != moon2_str:
        x,y,z = (moon1[current_step]["position"])
        x_comparing, y_comparing, z_comparing = (moon2[current_step]["position"])
        # print()
        if x < x_comparing:
            # print(f"{x} - {moon1_str} < {x_comparing} - {moon2_str} donc tmp_moon2.append(-1)")
            tmp_moon1.append(1)
            tmp_moon2.append(-1)
        elif x > x_comparing:
            # print(f"{x} > {x_comparing} donc tmp_moon2.append(1)")
            tmp_moon1.append(-1)
            tmp_moon2.append(1)
        else:
            tmp_moon1.append(0)
            tmp_moon2.append(0)

        if y < y_comparing:
            # print(f"{y} < {y_comparing} donc tmp_moon2.append(-1)")
            tmp_moon1.append(1)
            tmp_moon2.append(-1)
        elif y > y_comparing:
            # print(f"{y} < {y_comparing} donc tmp_moon2.append(1)")
            tmp_moon1.append(-1)
            tmp_moon2.append(1)
        else:
            tmp_moon1.append(0)
            tmp_moon2.append(0)

        if z < z_comparing:
            # print(f"{z} < {z_comparing} donc tmp_moon2.append(-1)")
            tmp_moon1.append(1)
            tmp_moon2.append(-1)
        elif z > z_comparing:
            # print(f"{z} < {z_comparing} donc tmp_moon2.append(1)")
            tmp_moon1.append(-1)
            tmp_moon2.append(1)
        else:
            tmp_moon1.append(0)
            tmp_moon2.append(0)
    # print()

    return tmp_moon1, tmp_moon2

def comparing_1_moon_to_others_for_future_velocity(my_dict,
                                                   moon_comparing,
                                                   moon_compared,
                                                   current_step,
                                                   temporary_velocities):

    for elem in my_dict:
        if elem not in temporary_velocities:
            temporary_velocities[elem] = []
        if elem != moon_comparing and elem not in moon_compared:
            # print(f"{elem} being compared to {moon_comparing}")
            tmp_velocity_moon1, tmp_velocity_moon2 = tmp_velocities_2_moons_v2(my_dict, moon_comparing, elem, current_step)
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

    if current_step == 0:
        my_dict = initialize_first_step(my_dict)
    else:
        # TO COMPLETE
        my_dict = initialize_new_step(my_dict, current_step)
    # my_dict = initialize_first_step(my_dict)

    print(f"\n---------- Current step is {current_step} ----------")

    temporary_velocities = {}
    moon_compared = []

    for moon in my_dict:
        moon_compared.append(moon)
        temporary_velocities, moon_compared = comparing_1_moon_to_others_for_future_velocity(my_dict,
                                                                                             moon,
                                                                                             moon_compared,
                                                                                             current_step,
                                                                                             temporary_velocities)
    # pprint(temporary_velocities)
    # print()
    # for elem in temporary_velocities:
    #     # print(elem)
    #     first_comp = temporary_velocities[elem][0]
    #     secd_comp = temporary_velocities[elem][1]
    #     third_comp = temporary_velocities[elem][2]
    #     actual_velocities = ((first_comp[0]+secd_comp[0]+third_comp[0], first_comp[1]+secd_comp[1]+third_comp[1], first_comp[2]+secd_comp[2]+third_comp[2]))
    #     my_dict[elem][current_step+1]["velocity"] = actual_velocities


    return temporary_velocities

def apply_velocity_aka_change_positions_nextstep(my_dict, current_step):
    # STEP 2: once all moons' velocities have been updated,
    # update the position of every moon by applying velocity.

    # simply add the velocity of each moon to its own position.

    # For example, if Europa has a position of x=1, y=2, z=3 and a velocity of x=-2, y=0,z=3,
    # then its new position would be x=-1, y=2, z=6.
    # This process does not modify the velocity of any moon.

    # my_dict = apply_gravity(my_dict, current_step)

    for elem in my_dict:
        # print(elem)
        first_comp = (my_dict[elem][current_step]["position"])
        secd_comp = (my_dict[elem][current_step+1]["velocity"])

        new_pos = ((first_comp[0]+secd_comp[0],first_comp[1]+secd_comp[1],
                    first_comp[2]+secd_comp[2]))
        my_dict[elem][current_step+1]["position"] = new_pos

    return(my_dict)

def initialize_exercise(input_ex):
    my_dict = create_dict_of_moons(input_ex)
    pprint(my_dict)

    current_step=0
    temporary_velocities = apply_gravity(my_dict,
                                        current_step)

    for elem in temporary_velocities:
        # print(elem)
        first_comp = temporary_velocities[elem][0]
        secd_comp = temporary_velocities[elem][1]
        third_comp = temporary_velocities[elem][2]
        actual_velocities = ((first_comp[0]+secd_comp[0]+third_comp[0], first_comp[1]+secd_comp[1]+third_comp[1], first_comp[2]+secd_comp[2]+third_comp[2]))
        my_dict[elem][current_step+1]["velocity"] = actual_velocities

    my_dict = apply_velocity_aka_change_positions_nextstep(my_dict, current_step)
    return my_dict, current_step

def next_step(my_dict,
              current_step):
    current_step += 1
    temporary_velocities = apply_gravity(my_dict,
                                        current_step)
    # pprint(temporary_velocities)
    # print()
    # pprint(my_dict)
    # print()
    for elem in temporary_velocities:
        first_comp = temporary_velocities[elem][0]
        secd_comp = temporary_velocities[elem][1]
        third_comp = temporary_velocities[elem][2]

        actual_velocities = ((first_comp[0]+secd_comp[0]+third_comp[0], first_comp[1]+secd_comp[1]+third_comp[1], first_comp[2]+secd_comp[2]+third_comp[2]))
        x,y,z = actual_velocities

        # Change position at current_step+1
        x_pos, y_pos, z_pos = (my_dict[elem][current_step]["position"])
        x_change_velocity, y_change_velocity, z_change_velocity = (my_dict[elem][current_step]["velocity"])

        # print(my_dict[elem][current_step+1]["position"])
        # print(elem, (x+x_pos+x_change_velocity, y+y_pos+y_change_velocity, z+z_pos+z_change_velocity))
        my_dict[elem][current_step+1]["position"] = (x+x_pos+x_change_velocity, y+y_pos+y_change_velocity, z+z_pos+z_change_velocity)


        # Change velocity at current_step+1
        # print(elem, (x+x_change_velocity, y+y_change_velocity, z+z_change_velocity))
        my_dict[elem][current_step+1]["velocity"] = (x+x_change_velocity, y+y_change_velocity, z+z_change_velocity)
        # print()

    return(my_dict, current_step)

# Io : <x=-1, y=0, z=2>
# Europa : <x=2, y=-10, z=-7>
# Ganymede : <x=4, y=-8, z=8>
# Callisto : <x=3, y=5, z=-1>

# After 1 step:
# Io : pos=<x= 2, y=-1, z= 1>, vel=<x= 3, y=-1, z=-1>
# Europa : pos=<x= 3, y=-7, z=-4>, vel=<x= 1, y= 3, z= 3>
# Ganymede : pos=<x= 1, y=-7, z= 5>, vel=<x=-3, y= 1, z=-3>
# Callisto : pos=<x= 2, y= 2, z= 0>, vel=<x=-1, y=-3, z= 1>
my_dict, current_step = initialize_exercise(input_ex)
pprint(my_dict)

def solving_part1(nb_of_steps, my_dict, current_step):
    # nb_of_steps = 10
    for _ in range(nb_of_steps-1):
        my_dict, current_step = next_step(my_dict, current_step)

    # After 10 steps:
    # Io : pos=<x= 2, y= 1, z=-3>, vel=<x=-3, y=-2, z= 1>
    # Europa : pos=<x= 1, y=-8, z= 0>, vel=<x=-1, y= 1, z= 3>
    # Ganymede : pos=<x= 3, y=-6, z= 1>, vel=<x= 3, y= 2, z=-3>
    # Callisto : pos=<x= 2, y= 0, z= 4>, vel=<x= 1, y=-1, z=-1>

    # pprint(my_dict)
    # print("-----")

    total_sum_of_NRJ = []
    for elem in my_dict:
        # print(elem)

        a,b,c = (my_dict[elem][current_step+1]["position"])
        a, b, c = abs(a), abs(b), abs(c)
        # A moon's potential energy is the sum of the absolute values of its x, y, and z position coordinates.
        potential = sum([a,b,c])
        # print("moon's potential energy:", potential)

        d,e,f = (my_dict[elem][current_step+1]["velocity"])
        d,e,f = abs(d), abs(e), abs(f)
        # A moon's kinetic energy is the sum of the absolute values of its velocity coordinates.
        kinetic = sum([d,e,f])
        # print("moon's kinetic energy:", kinetic)

        # The total energy for a single moon is its potential energy multiplied by its kinetic energy.
        print(f"Total energy of moon {elem}:", potential*kinetic, end="\n")
        total_sum_of_NRJ.append(potential*kinetic)

    return (sum(total_sum_of_NRJ))

total_sum_of_NRJ = solving_part1(10, my_dict, current_step)
print(total_sum_of_NRJ)
