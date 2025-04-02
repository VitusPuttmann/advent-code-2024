"""
This module contains functions that solve the challenges of day 9 of the
Advent of Code 2024 (https://adventofcode.com/).
"""


import os
import time


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_09_input.txt")


def calc_runtime(func):
    """ Measure runtime of function. """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = round(end_time - start_time, 5)
        return result, runtime
    return wrapper


def dedense(diskmap: list[int]) -> list[str]:
    """ Transform a list of integers (i.e. diskmap) into an extended list of
        integers following the rules for extension. """

    filemap = []
    counter = 0
    for element in diskmap:
        # Identify equal indexes and calculate 'file number' based on index.
        if counter % 2 == 0:
            content = str(int(counter / 2))
        else:
            content = '.'
    
        for val in range(1, (element+1)):
            filemap.append(content)

        counter += 1

    return filemap


def identify_first_space(filemap: list[str]) -> int:
    """ Take a list of strings (i.e. filemap) and return the index of the
        first '.' (i.e. space). """

    index_space = filemap.index('.')
    return index_space


def identify_last_element(filemap: list[str]) -> tuple:
    """ Take a list of strings (i.e. filemap) and return the content and index
        of the last string that is not a '.' (i.e. file number). """

    reversed_filemap = list(reversed(filemap))

    file_content = next(item for item in reversed_filemap if item != '.')
    file_index = (
        len(reversed_filemap) - 1
    ) - reversed_filemap.index(file_content)

    file_information = (file_content, file_index)

    return file_information


def condense(filemap: list[str]) -> list[str]:
    """ Take a list of strings (i.e. filemap), successively replace the '.'
        (i.e. spaces)' at the beginning with strings from the end until no space
        is left between strings, and return the result as a list. """
    
    num_places = len(filemap) - 1
    num_spaces = filemap.count('.')
    test_index = num_places - num_spaces
    
    filemap_condensed = filemap.copy()
    first_space = identify_first_space(filemap_condensed)
    while first_space <= test_index:
        file_information = identify_last_element(filemap_condensed)
        file_content = file_information[0]
        file_index = file_information[1]

        filemap_condensed[first_space] = file_content
        filemap_condensed[file_index] = '.'

        first_space = identify_first_space(filemap_condensed)

    return filemap_condensed


def compile_spaces(filemap: list[str]) -> dict:
    """ Take a list of strings (i.e. filemap), calculate the starting index and
        length of spaces, and compile them into dictionary. """
    
    spaces_with_length = []
    index_counter = 0
    first = 0
    for slot in filemap:
        if slot != '.':
            first = 0
            index_counter += 1
        elif slot == '.' and first == 0:
            space_append = [index_counter, 1]
            spaces_with_length.append(space_append)
            first = 1
            index_counter += 1
        else:
            spaces_with_length[-1][1] += 1
            index_counter += 1
    
    spaces_with_length = dict(spaces_with_length)

    return spaces_with_length


def condense_unfragmented(filemap: list[str]) -> list[str]:
    """ Take a list of strings (i.e. filemap), identify strings (i.e. files)
        and their frequency, identify periods (i.e. spaces), attempt to shift
        strings to spaces starting from the end, and return the result as a
        list. """

    files_with_length = {}
    for slot in reversed(filemap):
        if slot == '.':
            continue
        if not slot in files_with_length:
            files_with_length[slot] = 1
        else:
            files_with_length[slot] +=1
    
    filemap_defragmented = filemap.copy()
    for name, length in files_with_length.items():
        file_name = name
        file_length = length
        border = filemap_defragmented.index(file_name)
        spaces = compile_spaces(filemap_defragmented)
        index_insert = -1
        index_loop = 0
        for index, space in spaces.items():
            if index_loop == 0 and space >= file_length and index < border:
                index_insert = int(index)
                index_loop = 1
        if index_insert >= 0:
            index_start = index_insert
            index_end = index_insert + file_length
            name_indices = []
            for slot, value in enumerate(filemap_defragmented):
                if value == file_name:
                    name_indices.append(slot)
            for index in name_indices:
                filemap_defragmented[index] = '.'
            for index in range(index_start, index_end):
                filemap_defragmented[index] = file_name

    return filemap_defragmented


def calculate_checksum(value_list: list[str]) -> int:
    """ Take a list of values, multiply the elements by their index, and
        calculate the sum of the multiplications. """
    
    checksum = 0
    for index, value in enumerate(value_list):
        if value == '.':
            continue
        outcome = index * int(value)
        checksum += outcome
    
    return checksum


@calc_runtime
def solve_puzzle_09(filepath: str, unfragmented: bool = False) -> int:
    """ Create a list of strings (i.e. diskmap) from a text file, extend the
        list, condense it, create a list including only integers, and calculate
        the checksum. """

    with open(filepath, 'r') as file_input:
        string_line = file_input.readline().strip()
        string_list = list(string_line)
        diskmap = [int(e) for e in string_list]

    filemap = dedense(diskmap)

    if unfragmented == False:
        filemap_condensed = condense(filemap)
    
    if unfragmented == True:
        filemap_condensed = condense_unfragmented(filemap)

    checksum = calculate_checksum(filemap_condensed)

    return checksum


def main():
    """ Execute the main functions with the main input. """

    result_1, runtime_1 = solve_puzzle_09(filepath, unfragmented=False)
    print(f"Solution to the first puzzle of day 9: {result_1}\n"
          f"Runtime: {runtime_1} seconds\n")

    result_2, runtime_2 = solve_puzzle_09(filepath, unfragmented=True)
    print(f"Solution to the second puzzle of day 9: {result_2}\n"
          f"Runtime: {runtime_2} seconds\n")


if __name__ == '__main__':
    main()
