input_ex = open("day_10/exday10.txt", "r").read().split("\n")[:-1]
# print(input_ex)

def initialize(input_ex):
    grid = []
    visual_grid = str()
    coordinates = {}
    for i,elem in enumerate(input_ex):
        tmp = []
        for j,c in enumerate(elem):
            tmp.append(c)
            coordinates[(j,i)] = c
        grid.append(tmp)
        visual_grid += "\n" + str(tmp)

    # print((grid))
    print(visual_grid.replace(",","").replace("[","").replace("]","").replace("'",""))
    # print()
    # print(coordinates)
    print()
    return coordinates

def get_asteroid_coords(coordinates):
    # find only coordinates of asteroids
    asteroid_coords = []
    for key,value in coordinates.items():
        if value == "#":
            asteroid_coords.append(key)

    print("asteroid_coords:",sorted(asteroid_coords), end='\n\n')
    return asteroid_coords


def max_size_grid(coordinates):
    max_x_grid = 0
    max_y_grid = 0

    min_x_grid = 0
    min_y_grid = 0

    for v in list(coordinates.keys()):
        if (v[0]) > max_x_grid:
            max_x_grid = v[0]
        if (v[1]) > max_y_grid:
                max_y_grid = v[1]
        if (v[0]) < min_x_grid:
                min_x_grid = v[0]
        if (v[1]) < min_y_grid:
                min_y_grid = v[1]
    print("(max_y_grid, max_y_grid) are:",(max_y_grid, max_y_grid))
    print("(min_y_grid, min_y_grid) are:",(min_y_grid, min_y_grid))

    print()
    return (max_x_grid, max_y_grid), (min_x_grid, min_y_grid)

# def test_for_1_set_of_asteroid_coords(coords_tested, asteroid_coords):
#     x_basis, y_basis = coords_tested
#     asteroid_coords.remove((x_basis,y_basis))
#     # return asteroid_coords
#     line_of_sight_tmp = []
#     for elem in asteroid_coords:
#         x,y = elem
#         line_of_sight_tmp.append(((x- x_basis), (y- y_basis)))
#         # print("total change needed:", ((x - x_basis), (y - y_basis)), end="\n")

#     line_of_sight_tmp = list(set(line_of_sight_tmp))
#     print("Potential line_of_sight_tmp:", sorted(line_of_sight_tmp))
#     print("length of line_of_sight_tmp:", len(line_of_sight_tmp))

#     # éliminer ceux qui ne sont en faut pas visibles
#     # print("\nThose that cannot be seen are : \n - (4,4), bc in same line as from O to (2,2); \n - (4,3), bc in same line as from O to (3,2)\n")
#     return asteroid_coords, line_of_sight_tmp

def create_ligne_droite(new_coord_test, coords_tested,
                        max_x_grid, max_y_grid,
                        min_x_grid, min_y_grid,
                        asteroid_coords,
                        print_=False):

    x_basis, y_basis = coords_tested
    diff = ((new_coord_test[0]-x_basis), (new_coord_test[1]-y_basis))
    if print_:
        print("je pars de (coords_tested):", coords_tested)
        print("pour arriver à (new_coord_test):",new_coord_test)
    # print("diff:",diff)

    # faire une liste correspondant à une ligne droite avec tous les points entre 2 coordinates
    ligne_droite = []

    def which_slope(diff):
                # slope : si les deux ont le même signe -> slope positive
                if diff[0] > 0 and diff[1] > 0 :
                    slope = 1
                elif diff[0] < 0 and diff[1] < 0 :
                    slope = 1
                else:
                    slope = -1
                return slope

    slope = which_slope(diff)
    # print("slope:", slope)
    ligne_droite.append(coords_tested)
    ligne_droite.append(new_coord_test)
    tmp_x, tmp_y = new_coord_test
    # print("(tmp_x, tmp_y):", (tmp_x, tmp_y))

    # cas particulier diff[0] == diff[1]
    if abs(diff[0]) == abs(diff[1]):

        if slope > 0:
            if tmp_x != min_x_grid:
                # until x reaches min_x_grid:
                while tmp_x != min_x_grid: # or tmp_y != min_y_grid:
                    # x -= 1
                    tmp_x -= 1
                    # y -= 1
                    tmp_y -= 1
                    ligne_droite.append((tmp_x, tmp_y))

            if tmp_x != max_x_grid:
                # until x reaches max_x_grid:
                while tmp_x != max_x_grid:
                    # x += 1
                    tmp_x += 1
                    # y += 1
                    tmp_y += 1
                    ligne_droite.append((tmp_x, tmp_y))

        elif slope < 0:
            if tmp_x != min_x_grid :
                # until x reaches min_x_grid:
                while tmp_x != min_x_grid: # or tmp_y != min_y_grid:
                    # x = x - 1
                    tmp_x -= 1
                    # y = y + 1
                    tmp_y += 1
                    ligne_droite.append((tmp_x, tmp_y))

            if tmp_x != max_x_grid :
                # until x reaches max_x_grid:
                while tmp_x != max_x_grid: # or tmp_y != max_y_grid:
                    # x += 1
                    tmp_x += 1
                    # y -= 1
                    tmp_y -= 1
                    ligne_droite.append((tmp_x, tmp_y))

    else:
        if slope > 0 :
            if tmp_y != max_y_grid:
                # until y reaches max_y_grid:
                if abs(diff[1]) != 0:
                    while tmp_y != max_y_grid:
                        # x += abs(diff[0])
                        tmp_x += abs(diff[0])
                        # y += abs(diff[1])
                        tmp_y += abs(diff[1])
                        ligne_droite.append((tmp_x, tmp_y))
            else:
                next

            if tmp_y != min_y_grid:
                # until y reaches min_y_grid
                if abs(diff[1]) != 0:
                    while tmp_y != min_y_grid:
                        # x -= abs(diff[0])
                        tmp_x -= abs(diff[0])
                        # y -= abs(diff[1])
                        tmp_y -= abs(diff[1])
                        ligne_droite.append((tmp_x, tmp_y))
            else:
                next

        elif slope < 0 :
            if tmp_y != min_y_grid:
                # until y reaches max_y_grid:
                if abs(diff[1]) != 0:
                    while tmp_y != min_y_grid:
                        # x += abs(diff[0])
                        tmp_x += abs(diff[0])
                        # y -= abs(diff[1])
                        tmp_y -= abs(diff[1])
                        ligne_droite.append((tmp_x, tmp_y))
            else:
                next

            if tmp_y != max_y_grid:
                if abs(diff[1]) != 0:
                    # until y reaches min_y_grid
                    while tmp_y != max_y_grid:
                        # x -= abs(diff[0])
                        tmp_x -= abs(diff[0])
                        # y += abs(diff[1])
                        tmp_y += abs(diff[1])
                        ligne_droite.append((tmp_x, tmp_y))
                else:
                    next


    ligne_droite = sorted(list(set(ligne_droite)))

    # Keeping in ligne_droite only those coordinates relevant to us that represent an asteroid
    # print("Avant:", sorted(ligne_droite))
    not_possible = []
    for elem in (ligne_droite):
        if elem not in asteroid_coords:
            ligne_droite.remove(elem)
    # print("Après:", (ligne_droite))

    if starting_point in ligne_droite:
        ligne_droite.remove(starting_point)

    if len(ligne_droite)>1:
        not_possible = ligne_droite[1:]

    # print(ligne_droite)

    possible = sorted(ligne_droite)[0]

    # for elem in (ligne_droite):
    #         if elem not in asteroid_coords:
    #             ligne_droite.remove(elem)


    return possible, not_possible









coordinates = initialize(input_ex)
asteroid_coords= get_asteroid_coords(coordinates)

starting_point = (4,0)
nb_of_ast_possible_to_detect = 0
asteroid_coords.remove(starting_point)
(max_x_grid, max_y_grid), (min_x_grid, min_y_grid) = max_size_grid(coordinates)

def test_for_1_set_of_asteroid_coords(starting_point, new_coord_test,
                                  max_x_grid, max_y_grid,
                                  min_x_grid, min_y_grid,
                                  asteroid_coords):

    ligne_droite = create_ligne_droite(new_coord_test=new_coord_test, coords_tested=starting_point,
                                        max_x_grid=max_x_grid, min_x_grid=min_x_grid,
                                        max_y_grid=max_y_grid, min_y_grid=min_y_grid,
                                        asteroid_coords=asteroid_coords)
    return ligne_droite

    print("------------------------")

    nb_of_ast_possible_to_detect = 0
    if ligne_droite != []:
        nb_of_ast_possible_to_detect += 1
        print(f'Between the monitoring station at {starting_point} and the asteroid {new_coord_test}, the only asteroids that are visible are {ligne_droite[0]}.')

    print(f"At the monitoring station at {starting_point}, we detect {nb_of_ast_possible_to_detect} asteroid{"s" if nb_of_ast_possible_to_detect > 1 else ""} in direct line of sight.")
    print()
    return nb_of_ast_possible_to_detect

# possible, not_possible = test_for_1_set_of_asteroid_coords(starting_point,
#                                                                (2,2),
#                                                                 max_x_grid, max_y_grid,
#                                                                 min_x_grid, min_y_grid,
#                                                                 asteroid_coords)
# print("possible:", possible)
# print("not_possible:",not_possible)

print(f'Testing for monitoring station at {starting_point}:')
possibles_tmp = []
not_possibles_tmp = []
for elem in asteroid_coords:
    possible, not_possible = test_for_1_set_of_asteroid_coords(starting_point,
                                                               elem,
                                                                max_x_grid, max_y_grid,
                                                                min_x_grid, min_y_grid,
                                                                asteroid_coords)
    possibles_tmp.append(possible)
    not_possibles_tmp.append(not_possible)

# print("possibles_tmp:", possibles_tmp)
# print("not_possibles_tmp:",not_possibles_tmp)

not_possibles = []
for mini_not in not_possibles_tmp:
    for elem in mini_not:
        # print(elem)
        not_possibles.append(elem)

not_possibles = sorted(list(set(not_possibles)))
print("not_possibles:",not_possibles)

possibles = possibles_tmp.copy()
for elem in not_possibles:
    if elem in possibles_tmp:
        possibles.remove(elem)

possibles = sorted(list(set(possibles)))
print("possibles:", possibles)
print("Length possibles:",len(possibles))
