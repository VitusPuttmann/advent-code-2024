"""
This module contains functions that solve the challenges of day 4
    of the Advent of Code 2024 (https://adventofcode.com/).
"""


import time
import itertools
import os


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_04_input.txt")


""" Define all possible direction shifts. """
DIRECTIONS = {
    'tl': (-1, -1), 't': (-1, 0), 'tr': (-1, 1), 'r': (0, 1),
    'br': (1, 1), 'b': (1, 0), 'bl': (1, -1), 'l': (0, -1)
}


def calc_runtime(func):
    """ Measure runtime of function. """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = round(end_time - start_time, 5)
        return result, runtime
    return wrapper


def create_array(filepath: str) -> list[list[str]]:
    """ Read in text file and create array as nested lists 
        with letters as cells. """
    
    with open(filepath, 'r') as file_input:
        letter_array = []
        for line in file_input:
            row_text = line.strip()
            row_list = list(row_text)
            letter_array.append(row_list)
    
    return letter_array


def shift_position(start: tuple, direction: str) -> tuple:
    """ Return outcome of cell shift in specified direction. """

    shift_y, shift_x = DIRECTIONS[direction]
    end = (start[0]+shift_y, start[1]+shift_x)
    return end


def search_letter(
        array: list[list[str]], letter: str, center: tuple, position: str
    ) -> bool:
    """ Search for a specific letter in a target cell relative to a center
        cell. """
    
    target = shift_position(center, position)

    if (
        target[0] < 0 or
        target[0] > (len(array)-1) or
        target[1] < 0 or
        target[1] > (len(array[0])-1)
    ):
        return False

    return array[target[0]][target[1]] == letter


@calc_runtime
def solve_puzzle_04_01(filepath: str) -> int:
    """ Create an array from a text file, take each cell of the array in turn,
        search for the presence of XMAS in all directions and return the total
        number of matches. """

    array = create_array(filepath)
    
    row_numbers = range(len(array))
    col_numbers = range(len(array[0]))
    
    directions = ['tl', 't', 'tr', 'r', 'br', 'b', 'bl', 'l']
    
    num_xmas = 0
    for row, col, direc in itertools.product(
        row_numbers, col_numbers, directions
    ):
        center_shift = (row, col)

        search_res = False
        
        if array[center_shift[0]][center_shift[1]] == 'X':
            search_res = search_letter(array, 'M', center_shift, direc)
            center_shift = shift_position(center_shift, direc)
        
        if search_res:
            search_res = search_letter(array, 'A', center_shift, direc)
            center_shift = shift_position(center_shift, direc)
        
        if search_res:
            search_res = search_letter(array, 'S', center_shift, direc)
        
        if search_res:
            num_xmas += 1
    
    return num_xmas


@calc_runtime
def solve_puzzle_04_02(filepath: str) -> int:
    """ Create an array from a text file, take each cell of the array in turn,
        search for the presence of x-MAS in all directions and return the total
        number of matches. """

    array = create_array(filepath)

    row_numbers = range(len(array))
    col_numbers = range(len(array[0]))

    directions = {
        'tl': ('br', 'bl', 'tr'),
        #'t': ('b', 'l', 'r'),
        'tr': ('bl', 'br', 'tl'),
        #'r': ('l', 't', 'b'),
        'br': ('tl', 'tr', 'bl'),
        #'b': ('t', 'r', 'l'),
        'bl': ('tr', 'br', 'tl')#,
        #'l': ('r', 't', 'b')
    }

    num_mas_2 = 0
    for row, col in itertools.product(
        row_numbers, col_numbers
    ):
        center = (row, col)

        if array[center[0]][center[1]] != 'A':
            continue
        
        for direc in directions.keys():
            count_cross = 0
            if search_letter(
                array, 'M', center, direc
            ) == False:
                continue
            if search_letter(
                array, 'S', center, directions[direc][0]
            ) == False:
                continue
            if search_letter(
                array, "M", center, directions[direc][1]
            ) == True and search_letter(
                array, "S", center, directions[direc][2]
            ) == True:
                count_cross += 1
            if search_letter(
                array, "S", center, directions[direc][1]
            ) == True and search_letter(
                array, "M", center, directions[direc][2]
            ) == True:
                count_cross += 1
            if count_cross > 0:
                num_mas_2 += 1
    
    num_mas = int(num_mas_2 / 2)
    
    return num_mas


def main():
    """ Execute the main functions with the main input. """
    
    result_1, runtime_1 = solve_puzzle_04_01(filepath)
    print(f"Solution to the first puzzle of day 4: {result_1}\n"
          f"Runtime: {runtime_1} seconds\n")

    result_2, runtime_2 = solve_puzzle_04_02(filepath)
    print(f"Solution to the second puzzle of day 4: {result_2}\n"
          f"Runtime: {runtime_2} seconds\n")


if __name__ == '__main__':
    main()
