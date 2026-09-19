input_d8 = open("day_8/day8.txt", "r").read()[:-1]

# example: given an image 3 pixels wide and 2 pixels tall
# image = (3,2)
image = (25,6)

# Images are sent as a series of digits that each represent the color of a
# single pixel.
# 0 is black, 1 is white, and 2 is transparent.

def get_layers_in_2D(input_, image):
    # The digits fill each row of the image left-to-right,
    # then move downward to the next row,
    # filling rows top-to-bottom until every pixel of the image is filled.

    # Each image actually consists of a series of identically-sized layers
    # that are filled in this way.
    # So, the first digit corresponds to the top-left pixel of the first layer,
    # the second digit corresponds to the pixel to the right of that on the same layer,
    # and so on until the last digit, which corresponds to the bottom-right pixel of the last layer.

    layers_horiz = []
    tmp = []
    for i in range(len(input_)):
        if i%image[0]==0:
            tmp = []
            for u in range(i, i+image[0]):
                tmp.append(input_[u])
            layers_horiz.append(tmp)

    # print(layers_horiz)

    layers = []
    for j in range(len(layers_horiz)):
        if j%image[1]==0:
            # print(layers_horiz[j])
            tmp = []
            for v in range(j, j+image[1]):
                tmp.append(layers_horiz[v])
            layers.append(tmp)

    return (layers)

def get_layer_in_1D(layer):
    return (("".join(str(layer)).replace("[","").replace("]","")).replace("'","")).split(", ")

def all_1D_and_count_0_per_layer(input_d8, image):
    # create all layers in 1D & create a dict to count the number of 0 in each layer
    layers = get_layers_in_2D(input_d8, image)
    layers_image_1D = []
    count_layer = 0
    how_many_zeros = {}

    for layer in layers:
        tmp_layer = get_layer_in_1D(layer)
        new_layer = []
        for elem in tmp_layer:
            new_layer.append(int(elem))
            if int(elem) == 0:
                if count_layer not in how_many_zeros:
                    how_many_zeros[count_layer] = 1
                else: how_many_zeros[count_layer] += 1
        count_layer += 1
        layers_image_1D.append(new_layer)

    return how_many_zeros, layers_image_1D

def layer_fewest_0(how_many_zeros, layers_image_1D):
    # find which layer contains the fewest 0 digits
    old_value = float('inf')
    # print(old_value>0)
    best_key = None
    for key, value in (how_many_zeros.items()):
        if value < old_value:
            old_value = value
            best_key = key

    print("layer that contains the fewest 0 digits: ", best_key)
    print(f"layer {best_key} contains {old_value} 0 digits")

    # print(how_many_zeros)
    return (layers_image_1D, best_key)

def get_final_count(layers_image_1D, key):
    # On that layer, what is the number of 1 digits multiplied by the number of 2 digits?
    final_count = {}
    for num in layers_image_1D[key]:
        if (num) == 1:
            if 1 not in final_count:
                final_count[1] = 1
            else:
                final_count[1] += 1
        elif (num) == 2:
            if 2 not in final_count:
                final_count[2] = 1
            else:
                final_count[2] += 1
    print(final_count)
    print("number of 1 digits:", final_count[1])
    print("number of 2 digits:", final_count[2])
    print("final answer:",final_count[1]*final_count[2])
    return (final_count)

def part1(input_d8, image):
    how_many_zeros, layers_image_1D = all_1D_and_count_0_per_layer(input_d8, image)
    layers_image_1D, key = layer_fewest_0(how_many_zeros, layers_image_1D)
    # print("this is the layer", layers_image_1D[key])
    final_count = get_final_count(layers_image_1D, key)
    return final_count
# (part1(input_d8, image))

# --------------- part 2 ---------------

# Example :
# input_ex = open("day_8/ex2day8.txt", "r").read().strip()
# image_ex = (2,2)
# layers_ex = get_layers_in_2D(input_ex, image_ex)

input_real = open("day_8/day8.txt", "r").read().strip()
image = (25,6)

def get_coords_colors(image, layers):
    final_layers_colors = {}
    for coordy in range(image[1]):
        for coordx in range(image[0]):
            # print((coordx,coordy), end=": ")
            for layer in (layers):
                if (layer[coordy][coordx]) == "1":
                    final_layers_colors[(coordx,coordy)] = 1
                    # print(1)
                    break
                elif (layer[coordy][coordx]) == "0":
                    final_layers_colors[(coordx,coordy)] = 0
                    # print(0)
                    break
                elif (layer[coordy][coordx]) == "2":
                    next
    return (final_layers_colors)

def final_image(all_axes, final_layers_colors, how_tall_pixel_img):
    axis_0 = []
    for x,y in final_layers_colors.keys():
        if y == how_tall_pixel_img:
            axis_0.append(final_layers_colors[(x,y)])
    all_axes+= "\n"+str(axis_0)
    return all_axes

def part2(input_real, image):
    layers = get_layers_in_2D(input_real, image)
    final_layers_colors = (get_coords_colors(image, layers))

    all_axes = str()
    for how_tall_pixel_img in range(image[1]):
        all_axes = final_image(all_axes, final_layers_colors, how_tall_pixel_img)

    print(all_axes.replace("[","").replace("]","").replace(",","").replace("1","X").replace("0"," "))

part2(input_real, image)
