"""
This module contains functions that solve the challenges of day 8 of the
Advent of Code 2024 (https://adventofcode.com/).
"""


import os
import time
from itertools import combinations


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_08_input.txt")


def calc_runtime(func):
    """ Measure runtime of function. """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = round(end_time - start_time, 5)
        return result, runtime
    return wrapper


def create_grid(filepath: str) -> list[list[str]]:
    """ Read a text file and create a grid of the content as a list of lists.
        """
    
    grid_list = []
    
    with open(filepath, 'r') as file_input:
        for line in file_input:
            str_line = line.strip()
            str_list = list(str_line)
            grid_list.append(str_list)
    
    return grid_list


def identify_antinodes(
        grid: list[list[str]], coordinate_list: list[tuple],
        steps: int
    ) -> list[tuple]:
    """ Take a list of list (i.e. grid) and calculate all antinodes on the grip
        for a specific string (i.e. frequency) given its coordinates on the
        grid. """

    max_y = len(grid) - 1
    max_x = len(grid[0]) - 1

    combinations_list = list(combinations(coordinate_list, 2))

    antinode_list = []
    for pairs in combinations_list:
        distance_y = pairs[0][0] - pairs[1][0]
        distance_x = pairs[0][1] - pairs[1][1]

        for val in range(1, steps):
            if distance_x < 0 and distance_y < 0:
                antinode_1_y = pairs[0][0] - (val * abs(distance_y))
                antinode_1_x = pairs[0][1] - (val * abs(distance_x))
                antinode_2_y = pairs[1][0] + (val * abs(distance_y))
                antinode_2_x = pairs[1][1] + (val * abs(distance_x))
            elif distance_x < 0 and distance_y > 0:
                antinode_1_y = pairs[0][0] + (val * abs(distance_y))
                antinode_1_x = pairs[0][1] - (val * abs(distance_x))
                antinode_2_y = pairs[1][0] - (val * abs(distance_y))
                antinode_2_x = pairs[1][1] + (val * abs(distance_x))
            elif distance_x > 0 and distance_y < 0:
                antinode_1_y = pairs[0][0] - (val * abs(distance_y))
                antinode_1_x = pairs[0][1] + (val * abs(distance_x))
                antinode_2_y = pairs[1][0] + (val * abs(distance_y))
                antinode_2_x = pairs[1][1] - (val * abs(distance_x))
            elif distance_x > 0 and distance_y > 0:
                antinode_1_y = pairs[0][0] + (val * abs(distance_y))
                antinode_1_x = pairs[0][1] + (val * abs(distance_x))
                antinode_2_y = pairs[1][0] - (val * abs(distance_y))
                antinode_2_x = pairs[1][1] - (val * abs(distance_x))
            antinode_1 = (antinode_1_y, antinode_1_x)
            antinode_2 = (antinode_2_y, antinode_2_x)

            for antinode in [antinode_1, antinode_2]:
                if antinode[0] < 0 or antinode[0] > max_y:
                    continue
                if antinode[1] < 0 or antinode[1] > max_x:
                    continue
                if antinode not in antinode_list: antinode_list.append(antinode)

    return antinode_list


@calc_runtime
def solve_puzzle_08(filepath: str, extended: bool = False) -> int:
    """ Create a list of lists of strings from a text file representing a grid,
        identify all unique strings (i.e., frequencies), calculate all antinodes
        for each of them depending on the approach chosen, compile a list of the
        antinodes and count their number. """
    
    grid_list = create_grid(filepath)
    
    frequency_dict = {}

    for row_index, row_content in enumerate(grid_list):
        """ Loop over all elements in the list of lists (i.e., the grid),
            identify relevant strings (i.e., antennas), and store all
            coordinates of a string in a dictionary. """
        for element_index, element_content in enumerate(row_content):
            if element_content == '.':
                continue
            row_coordinate = row_index
            col_coordinate = element_index
            coordinate = (row_coordinate, col_coordinate)
            if not element_content in frequency_dict:
                frequency_dict[element_content] = [coordinate]
            else:
                frequency_dict[element_content].append(coordinate)

    all_antinodes = []
    for frequency_list in frequency_dict.values():
        if not extended:
            antinodes = identify_antinodes(grid_list, frequency_list, 2)
        if extended:
            antinodes = identify_antinodes(grid_list, frequency_list, 50)
        all_antinodes += antinodes

    if extended:
        for element in frequency_dict.values():
            if len(element) > 1:
                for subelement in element:
                    all_antinodes.append(subelement)
        
    unique_antinodes = list(set(all_antinodes))
    number_antinodes = len(unique_antinodes)

    return number_antinodes


def main():
    """ Execute the main functions with the main input. """

    result_1, runtime_1 = solve_puzzle_08(filepath)
    print(f"Solution to the first puzzle of day 8: {result_1}\n"
          f"Runtime: {runtime_1} seconds\n")

    result_2, runtime_2 = solve_puzzle_08(filepath, extended=True)
    print(f"Solution to the second puzzle of day 8: {result_2}\n"
          f"Runtime: {runtime_2} seconds\n")


if __name__ == '__main__':
    main()
