# How many different passwords within the range given in your puzzle input meet these criteria?
input = open("day4.txt", "r").read().split("\n")

def for_first_num(number):
    number = str(number)
    actual_number = []

    num_old = int(number[0])
    actual_number.append(str(num_old))

    for char in number[1:]:
        num = int(char)
        if num_old < num:
            num_old = num
            actual_number.append(str(num))
            continue
        else:
            # print(num_old,num)
            actual_number.append(str(num_old))
            break

    while len(actual_number) != 6:
        actual_number.append(str(num_old))
    return int("".join(actual_number))

def get_possible_number(number):
    # Going from left to right, the digits never decrease;
    number = str(number)
    actual_number = []

    num_old = int(number[0])
    actual_number.append(str(num_old))

    for char in number[1:]:
        num = int(char)
        if num_old < num:
            num_old = num
            actual_number.append(str(num))
            continue
        else:
            # print(num_old,num)
            actual_number.append(str(num_old))

    actual_number = int("".join(actual_number))
    return actual_number

def initialize(input):
    possibles = []
    mini, maxi = input[0].split("-")
    actual_mini = (for_first_num(int(mini)))
    actual_maxi = (get_possible_number(int(maxi)))

    possibles.append((actual_mini))
    possibles.append((actual_maxi))
    return possibles, mini, maxi

def rule_increase(possibles):
    # Going from left to right, the digits never decrease; ☑
    # they only ever increase or stay the same (like 111123 or 135679). ☑
    print("\n‼️ Rule : Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).")
    def get_next_one_rule_increase(pos, possibles):
        elem = get_possible_number(possibles[pos-1]+1)
        possibles.insert(pos, elem)
        return pos, possibles

    pos = 1
    get_next_one_rule_increase(pos, possibles)
    while possibles[pos] <= possibles[-1]:
        pos+=1
        get_next_one_rule_increase(pos, possibles)
    print("Implemented ✅✅✅")
    return (possibles)

def testing_1_num(digit_same_possibles, number):
    # Two adjacent digits are the same (like 22 in 122345).
    old_char = (str(number)[0])
    for char in (str(number)[1:]):
        if (old_char == char):
            # print(True)
            digit_same_possibles.append(number)
            break
        else:
            old_char = char
            continue
    else:
        print(f"{False} for num {(str(number))}")
    return digit_same_possibles

def rule_adjacent_numbers(possibles):
    # Two adjacent digits are the same (like 22 in 122345).
    print("\n‼️ Rule : Two adjacent digits are the same")
    digit_same_possibles = []
    for i in range(len(possibles)):
        number = possibles[i]
        digit_same_possibles = testing_1_num(digit_same_possibles, number)
    print("Corrected ✅✅✅")
    return digit_same_possibles

def within_range(digit_same_possibles,mini, maxi):
    # The value is within the range given in your puzzle input.

    print("\n‼️ Rule : The value is within the range given in your puzzle input")
    print(f"As it currently stands, is the smallest number in the range, aka {digit_same_possibles[0]} ≥ {int(mini)} ? {digit_same_possibles[0] >= int(mini)}")
    print(f"As it currently stands, is the biggest number in the range, aka {digit_same_possibles[-1]} ≤ {int(maxi)} ? {digit_same_possibles[-1] <= int(maxi)}")

    # print(digit_same_possibles[-1],maxi) # False for maxi
    for num in reversed(digit_same_possibles):
        if (num) >= int(maxi):
            digit_same_possibles.remove(num)
        else:
            break
    print("Corrected ✅✅✅")
    return digit_same_possibles

def run_part1(input):
    possibles, mini, maxi = initialize(input)

    # Going from left to right, the digits never decrease;
    # they only ever increase or stay the same (like 111123 or 135679).
    possibles = rule_increase(possibles)

    # Two adjacent digits are the same (like 22 in 122345).
    digit_same_possibles = rule_adjacent_numbers(possibles)

    # The value is within the range given in your puzzle input.
    digit_same_possibles = within_range(digit_same_possibles,mini, maxi)

    # It is a six-digit number.
    print("\n‼️ Rule: It is a six-digit number.")
    print(f"Number mini in range : {digit_same_possibles[0]}, {len(str(digit_same_possibles[0]))} digits")
    print(f"Number maxi in range : {digit_same_possibles[-1]}, {len(str(digit_same_possibles[-1]))} digits")
    print("Verified ✅✅✅")

    print('\n---- waiting for answer ----')
    return (len(digit_same_possibles))

print(run_part1(input))
