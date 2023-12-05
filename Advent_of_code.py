import numpy as np


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


print(day_5_2())
