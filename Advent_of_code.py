import numpy as np
from math import sqrt
from math import ceil


def day_1_1(): # The filename of my puzzle input is called "puzzle_input", and is used for every function.
    f = open("puzzle_input", "r")
    sum = 0
    for line in f:
        chars = []
        for char in line:
            if char.isdigit():
                chars.append(int(char))
        sum += chars[0]*10 + chars[-1]
    f.close()
    return sum


def day_1_2():
    f = open("puzzle_input", "r")
    sum = 0
    numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    for line_number, line in enumerate(f):
        first_number = [10000000, None]
        last_number = [10000000, None]
        for splitter in numbers.keys():
            if splitter in line:
                splitted = line.split(splitter)
                if len(splitted[0]) < first_number[0]:
                    first_number = [len(splitted[0]), splitter]
                if len(splitted[-1]) < last_number[0]:
                    last_number = [len(splitted[-1]), splitter]
        sum += 10*numbers[first_number[1]] + numbers[last_number[1]]
    return sum


def day_2_1():
    f = open("puzzle_input", "r")
    colors = {"red": 12, "green": 13, "blue": 14}
    sum = 0
    for line in f:
        possible = True
        id = int(line[5:line.index(":")])
        sets = line[line.index(":") + 1:].split(";")
        for set in sets:
            cubes = set.split(",")
            for cube in cubes:
                for color, value in colors.items():
                    if color in cube:
                        if int(cube.split()[0]) > value:
                            possible = False
        if possible:
            sum += id
    return sum


def day_2_2():
    f = open("puzzle_input", "r")
    sum = 0
    for line in f:
        sets = line[line.index(":") + 1:].split(";")
        min_number_cubes = {"blue": 0, "red": 0, "green": 0}
        for set in sets:
            cubes = set.split(",")
            for cube in cubes:
                if min_number_cubes[cube.split()[1]] < int(cube.split()[0]):
                    min_number_cubes[cube.split()[1]] = int(cube.split()[0])
        product = 1
        for color, value in min_number_cubes.items():
            product *= value
        sum += product
    return sum


def day_3_1():
    f = open("puzzle_input", "r")
    matrix = []
    sum = 0
    for index, line in enumerate(f):
        matrix.append([])
        for char in line:
            if char != "\n":
                matrix[index].append(char)
    f.close()
    matrix = np.asarray(matrix)
    for i in range(matrix.shape[0]):
        inputting = ["", False]
        for j in range(matrix.shape[1]):
            if matrix[i, j].isdigit():
                inputting[0] += matrix[i, j]
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        try:
                            if matrix[i + k, j + l] != "." and not matrix[i + k, j + l].isdigit():
                                inputting[1] = True
                        except:
                            pass
            else:
                if inputting[1]:
                    sum += int(inputting[0])
                inputting = ["", False]
        if inputting[1]:
            sum += int(inputting[0])
        inputting = ["", False]
    return sum


def day_3_2():
    f = open("puzzle_input", "r")
    matrix = []
    gears = {}
    sum = 0
    for index, line in enumerate(f):
        matrix.append([])
        for char in line:
            if char != "\n":
                matrix[index].append(char)
    f.close()
    matrix = np.asarray(matrix)
    for i in range(matrix.shape[0]):
        inputting = ["", False]  # NUMBER, SYMBOL
        for j in range(matrix.shape[1]):
            if matrix[i, j].isdigit():
                inputting[0] += matrix[i, j]
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        try:
                            if matrix[i + k, j + l] == "*":
                                inputting[1] = (i + k, j + l)
                        except:
                            pass
            else:
                if inputting[1] != False:
                    if inputting[1] not in gears.keys():
                        gears[inputting[1]] = []
                    gears[inputting[1]].append(int(inputting[0]))
                inputting = ["", False]
        if inputting[1] != False:
            if inputting[1] not in gears.keys():
                gears[inputting[1]] = []
            gears[inputting[1]].append(int(inputting[0]))
        inputting = ["", False]
    for index, gear in gears.items():
        product = 0
        if len(gear) == 2:
            product = 1
            for number in gear:
                product *= number
        sum += product
    return sum


def day_4_1():
    f = open("puzzle_input", "r")
    points = 0
    for line in f:
        card = line[line.index(":") + 1:].split("|")
        winning_numbers = []
        round_points = 0
        for number in card[0].split():
            winning_numbers.append(number)
        for number in card[1].split():
            if number in winning_numbers:
                if round_points == 0:
                    round_points = 1
                else:
                    round_points *= 2
        points += round_points
    f.close()
    return points


def day_4_2():
    f = open("puzzle_input", "r")
    scratchcards = 0
    puzzle_input = []
    copied_cards = []
    winners = {}
    opened_copies = {}

    for index, line in enumerate(puzzle_input):
        card = line[line.index(":") + 1:].split("|")
        winning_numbers = []
        round_points = 0
        scratchcards += 1
        opened_copies[index + 1] = 0
        for number in card[0].split():
            winning_numbers.append(number)
        for number in card[1].split():
            if number in winning_numbers:
                round_points += 1
        winners[index + 1] = round_points
        for i in range(index + 1, index + 1 + round_points):
            copied_cards.append(puzzle_input[i])
    while len(copied_cards) != 0:
        card_id = int(copied_cards[0][5:copied_cards[0].index(":")])
        scratchcards += 1
        round_points = winners[card_id]
        for i in range(card_id, card_id + round_points):
            print("{1} Won copy of card {0}".format(i + 1, card_id))
            copied_cards.append(puzzle_input[i])
        copied_cards.pop(0)
        print(scratchcards)
    f.close()
    return scratchcards


def day_4_2_eff():
    f = open("puzzle_input", "r")
    puzzle_input = []
    for line in f:
        try:
            line = line[:line.index("\n")]
        except:
            pass
        puzzle_input.append(line)
    wins = {}
    cards_per_card = []
    for i in range(len(puzzle_input)):
        wins[i] = []
        cards_per_card.append(0)
    for index, line in enumerate(puzzle_input):
        winning_numbers = [number for number in line[line.index(":") + 1:].split("|")[0].split()]
        for i in range(len([number for number in line[line.index(":") + 1:].split("|")[1].split() if number in winning_numbers])):
            wins[index].append(index + i + 1)
    for i in range(len(cards_per_card) - 1, -1, -1):
        for card in wins[i]:
            cards_per_card[i] += 1
            cards_per_card[i] += cards_per_card[card]
    return sum([win for win in cards_per_card]) + len(puzzle_input)


def day_5_1():
    f = open("puzzle_input", "r")
    puzzle_input = []
    for line in f:
        if "\n" in line:
            line = line[:-1]
        puzzle_input.append(line)
    seeds = puzzle_input[0].split()[1:]
    seeds = [int(seed) for seed in seeds]
    trans = []
    for line in puzzle_input[2:]:
        if line != "" and not line[0].isdigit():
            trans.append([])
        elif line != "":
            trans[len(trans) - 1].append(line.split())
    trans = [[[int(k) for k in trans[i][j]] for j in range(len(trans[i]))] for i in range(len(trans))]
    for seed_number, seed in enumerate(seeds):
        for to in trans:
            for line in to:
                if line[1] <= seed < line[1] + line[2]:
                    seeds[seed_number] = seed + line[0] - line[1]
                    seed = seeds[seed_number]
                    break
    return min(seeds)


def day_5_2():
    f = open("puzzle_input", "r")
    puzzle_input = []
    for line in f:
        if "\n" in line:
            line = line[:-1]
        puzzle_input.append(line)
    seeds = puzzle_input[0].split()[1:]
    seeds = [int(seed) for seed in seeds]
    seeds = [[seeds[i], seeds[i+1]] for i in range(0, len(seeds), 2)]
    trans = []
    for line in puzzle_input[2:]:
        if line != "" and not line[0].isdigit():
            trans.append([])
        elif line != "":
            trans[len(trans) - 1].append(line.split())
    trans = [[[int(k) for k in trans[i][j]] for j in range(len(trans[i]))] for i in range(len(trans))]
    for to in trans:
        terminated_indices = []
        for seed_number, seed in enumerate(seeds):
            for line in to:
                if seed[0] >= line[1] and seed[0] + seed[1] - 1 <= line[1] + line[2] - 1:
                    seeds[seed_number][0] = seed[0] + line[0] - line[1]
                    break
                elif line[1] <= seed[0] and seed[0] + seed[1] - 1 >= line[1] + line[2] - 1 and seed[0] <= line[1] + line[2] - 1:
                    seeds.append([seed[0], line[1] + line[2] - seed[0]])
                    seeds.append([line[1] + line[2], seed[0] + seed[1] - 1 - (line[1] + line[2] - 1)])
                    terminated_indices.append(seed_number)
                    break
                elif seed[0] <= line[1] and seed[0] + seed[1] - 1 >= line[1] and line[1] + line[2] - 1 >= seed[0] + seed[1] - 1:
                    seeds.append([seed[0], line[1] - seed[0]])
                    seeds.append([line[1], seed[0] + seed[1] - line[1] - 1])
                    terminated_indices.append(seed_number)
                    break
                elif seed[0] < line[1] and seed[0] + seed[1] -1 > line[1] + line[2] - 1:
                    seeds.append([seed[0], line[1] - seed[0]])
                    seeds.append([line[1], line[2]])
                    seeds.append([line[1] + line[2], seed[0] + seed[1] - 1 - (line[1] + line[2] - 1)])
                    terminated_indices.append(seed_number)
                    break
        for i in range(len(terminated_indices) - 1, -1, -1):
            seeds.pop(terminated_indices[i])
    lowest = [seed[0] for seed in seeds]
    return min(lowest)


def day_6_1():
    f = open("puzzle_input").read().split("\n")
    time = [int(number) for number in f[0].split()[1:]]
    distance = [int(number) for number in f[1].split()[1:]]
    product = 1
    for i in range(len(time)): # formula: 0 = x * (time - x) - distance -> 0 = -1x^2 + time * x - distance + 1
        distances = [(-1*time[i] + sqrt(time[i]**2 - 4 * -1 * -1 * (distance[i] + 1)))/-2, (-1*time[i] - sqrt(time[i]**2 - 4 * -1 * -1 * (distance[i] + 1)))/-2]
        product *= distances[1]//1 - ceil(distances[0]) + 1
    return int(product)


def day_6_2():
    f = open("puzzle_input").read().split("\n")
    time = int("".join([number for number in f[0].split()[1:]]))
    distance = int("".join([number for number in f[1].split()[1:]]))
    distances = [(-1 * time + sqrt(time ** 2 - 4 * -1 * -1 * (distance + 1))) / -2,
                 (-1 * time - sqrt(time ** 2 - 4 * -1 * -1 * (distance + 1))) / -2]
    product = distances[1] // 1 - ceil(distances[0]) + 1
    return int(product)


# print(day_6_2())


# Down below I've made functions for AoC 2022 (For my own practice)


def year_2022_day_3_1():
    f = open("puzzle_input", "r").read().split("\n")
    items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s = 0
    for line in f:
        double = list(set(line[:len(line)//2]) & set(line[len(line)//2:]))
        s += items.index(double[0]) + 1
    return s


def year_2022_day_3_2():
    f = open("puzzle_input", "r").read().split("\n")
    items = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return sum([items.index(list(set(f[i]) & set(f[i + 1]) & set(f[i + 2]))[0]) + 1 for i in range(0, len(f), 3)])


def year_2022_day_5_2():
    f = open("puzzle_input", "r").read().split("\n")
    matrix = np.array([[f[i][j] for j in range(1, len(f[i]), 4)] for i in range(0, f.index("") - 1)])
    matrix = [[matrix[j, i] for j in range(matrix.shape[0] - 1, -1, -1) if matrix[j, i] not in [" ", "0"]] for i in range(matrix.shape[1])]
    for line in f[f.index("") + 1:]:
        for i in range(int(line.split()[1]), 0, -1):
            matrix[int(line.split()[5]) - 1].append(matrix[int(line.split()[3]) - 1].pop(-1 * i))
    return "".join([matrix[i][-1] for i in range(len(matrix))])


def year_2022_day_6_1():
    f = open("puzzle_input", "r").read()
    return [i for i in range(3, len(f)) if len(set(f[i-4:i])) == 4][0]


def year_2022_day_6_2():
    f = open("puzzle_input", "r").read()
    return [i for i in range(13, len(f)) if len(set(f[i-14:i])) == 14][0]


def year_2022_day_7_1():
    f = open("puzzle_input", "r").read().split("\n")
    dir = []
    content = {}
    sizes = {}
    for line in f:
        args = line.split()
        if args[0] == "$":
            if args[1] == "cd":
                if args[2] != "..":
                    dir.append(args[2])
                    if dir[-1] not in content.keys():
                        content["|".join(dir)] = []
                else:
                    dir.pop(-1)
        else:
            if (args[0], "|".join(dir) + "|" + args[1]) not in content["|".join(dir)]:
                content["|".join(dir)].append((args[0], "|".join(dir) + "|" + args[1]))
    print(content)
    def det_size(files, dir):
        size = 0
        for file in files:
            if file[0].isdigit():
                size += int(file[0])
            else:
                if dir in sizes.keys():
                    size += sizes[dir]
                else:
                    size += det_size(content[file[1]], file[1])
        sizes[dir] = size
        return size
    s = 0
    for dir, files in content.items():
        size = det_size(files, dir)
        if size <= 100000:
            s += size
    return s

def year_2022_day_7_2():
    f = open("puzzle_input", "r").read().split("\n")
    dir = []
    content = {}
    sizes = {}
    for line in f:
        args = line.split()
        if args[0] == "$":
            if args[1] == "cd":
                if args[2] != "..":
                    dir.append(args[2])
                    if dir[-1] not in content.keys():
                        content["|".join(dir)] = []
                else:
                    dir.pop(-1)
        else:
            if (args[0], "|".join(dir) + "|" + args[1]) not in content["|".join(dir)]:
                content["|".join(dir)].append((args[0], "|".join(dir) + "|" + args[1]))
    def det_size(files, dir):
        size = 0
        for file in files:
            if file[0].isdigit():
                size += int(file[0])
            else:
                if dir in sizes.keys():
                    size += sizes[dir]
                else:
                    size += det_size(content[file[1]], file[1])
        sizes[dir] = size
        return size
    for dir, files in content.items():
        det_size(files, dir)
    potential_sizes = []
    for dir, size in sizes.items():
        if size >= 30000000 - (70000000 - sizes["/"]):
            potential_sizes.append(int(size))
    return min(potential_sizes)


print(year_2022_day_7_2())
