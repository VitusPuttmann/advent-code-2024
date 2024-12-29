""" This module contains functions that solve the challenges of day 8
    of the advent of code 2024 (https://adventofcode.com/).
"""

import os
from itertools import combinations

""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_08_input.txt")


def create_map(filepath):
    """ Read a text file and create a map of the content as a list. """
    
    fin = open(filepath, 'r')

    map_list = []
    for line in fin:
        str_line = line.strip()
        str_list = list(str_line)
        map_list.append(str_list)
    
    return map_list


def identify_antinodes(map, coordinate_list, steps):
    """ Take a map and calculate all antinodes on the map for a 
        specific frequency given its coordinates on the map. """

    max_x = len(map[0]) - 1
    max_y = len(map) - 1

    combinations_list = list(combinations(coordinate_list, 2))

    antinode_list = []
    for pairs in combinations_list:
        distance_x = pairs[0][0] - pairs[1][0]
        distance_y = pairs[0][1] - pairs[1][1]

        for val in range(1, steps):
            if distance_x < 0 and distance_y < 0:
                antinode_1_x = pairs[0][0] - (val * abs(distance_x))
                antinode_1_y = pairs[0][1] - (val * abs(distance_y))
                antinode_2_x = pairs[1][0] + (val * abs(distance_x))
                antinode_2_y = pairs[1][1] + (val * abs(distance_y))
            if distance_x < 0 and distance_y > 0:
                antinode_1_x = pairs[0][0] - (val * abs(distance_x))
                antinode_1_y = pairs[0][1] + (val * abs(distance_y))
                antinode_2_x = pairs[1][0] + (val * abs(distance_x))
                antinode_2_y = pairs[1][1] - (val * abs(distance_y))
            if distance_x > 0 and distance_y < 0:
                antinode_1_x = pairs[0][0] + (val * abs(distance_x))
                antinode_1_y = pairs[0][1] - (val * abs(distance_y))
                antinode_2_x = pairs[1][0] - (val * abs(distance_x))
                antinode_2_y = pairs[1][1] + (val * abs(distance_y))
            if distance_x > 0 and distance_y > 0:
                antinode_1_x = pairs[0][0] + (val * abs(distance_x))
                antinode_1_y = pairs[0][1] + (val * abs(distance_y))
                antinode_2_x = pairs[1][0] - (val * abs(distance_x))
                antinode_2_y = pairs[1][1] - (val * abs(distance_y))
            antinode_1 = (antinode_1_x, antinode_1_y)
            antinode_2 = (antinode_2_x, antinode_2_y)

            for antinode in [antinode_1, antinode_2]:
                if antinode[0] < 0 or antinode[0] > max_x:
                    continue
                if antinode[1] < 0 or antinode[1] > max_y:
                    continue
                if not antinode in antinode_list: antinode_list.append(antinode)
    
    return antinode_list


def solve_puzzle_08(filepath, extended=False):
    """ Create a list from a text file containing a map, identify all
        unique frequencies, calculate antinodes for each of them - depending
        on the version chosen -, compile a list of all antinodes and
        count their number. """
    
    map_list = create_map(filepath)
    
    frequency_dict = {}
    for row_index, row_content in enumerate(map_list):
        for element_index, element_content in enumerate(row_content):
            if element_content == '.':
                continue
            x_coordinate = element_index
            y_coordinate = row_index
            coordinate = (x_coordinate, y_coordinate)
            if not element_content in frequency_dict:
                frequency_dict[element_content] = [coordinate]
            else:
                frequency_dict[element_content].append(coordinate)

    all_antinodes = []
    for frequency_list in frequency_dict.values():
        if extended == False:
            antinodes = identify_antinodes(map_list, frequency_list, 2)
        if extended == True:
            antinodes = identify_antinodes(map_list, frequency_list, 50)
        all_antinodes += antinodes

    if extended == True:
        for element in frequency_dict.values():
            if len(element) > 1:
                for subelement in element:
                    all_antinodes.append(subelement)
        
    unique_antinodes = list(set(all_antinodes))
    number_antinodes = len(unique_antinodes)

    return number_antinodes


def main():
    """ Execute the main functions with the main input. """

    result_1 = solve_puzzle_08(filepath)
    print(f"Solution of the first puzzle of day 8: {result_1}.")

    result_2 = solve_puzzle_08(filepath, extended=True)
    print(f"Solution of the second puzzle of day 8: {result_2}.")


if __name__ == '__main__':
    main()
