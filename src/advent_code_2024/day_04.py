""" This module contains functions that solve the challenges of day 4
    of the advent of code 2024 (https://adventofcode.com/).
"""

import itertools
import os


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_04_input.txt")


def create_array(filepath):
    """ Read in text file and create array as nested lists 
        with letters as cells. """
    
    fin = open(filepath, 'r')
    
    letter_array = []
    for line in fin:
        row_text = line.strip()
        row_list = list(row_text)
        letter_array.append(row_list)
    
    fin.close()
    
    return letter_array


def shift_position(start, direction):
    """ Define shifts in cell for all directions. """

    if direction == 'tl':
        end = (start[0]-1, start[1]-1)
    elif direction == 't':
        end = (start[0]-1, start[1])
    elif direction == 'tr':
        end = (start[0]-1, start[1]+1)
    elif direction == 'r':
        end = (start[0], start[1]+1)
    elif direction == 'br':
        end = (start[0]+1, start[1]+1)
    elif direction == 'b':
        end = (start[0]+1, start[1])
    elif direction == 'bl':
        end = (start[0]+1, start[1]-1)
    elif direction == 'l':
        end = (start[0], start[1]-1)
    else:
        print("Invalid direction specification.")
    
    return end


def search_letter(array, letter, center, position):
    """ Search for a specific letter in a target cell relative to a
        center cell. """
    
    target = shift_position(center, position)

    if (
        target[0] < 0 or
        target[0] > (len(array)-1) or
        target[1] < 0 or
        target[1] > (len(array[0])-1)
    ):
        return False

    if array[target[0]][target[1]] == letter:
        return True
    else:
        return False


def solve_puzzle_04_01(filepath):
    """ Create an array from a text file, take each cell of
    the array in turn, search for the presence of XMAS in all
    directions and return the total number of matches. """

    array = create_array(filepath)
    
    row_numbers = range(len(array))
    col_numbers = range(len(array[0]))
    
    directions = ['tl', 't', 'tr', 'r', 'br', 'b', 'bl', 'l']
    
    num_xmas = 0
    for row, col, dir in itertools.product(
        row_numbers, col_numbers, directions
    ):
        center_shift = (row, col)

        search_res = False
        
        if array[center_shift[0]][center_shift[1]] == 'X':
            search_res = search_letter(array, 'M', center_shift, dir)
            center_shift = shift_position(center_shift, dir)
        
        if search_res == True:
            search_res = search_letter(array, 'A', center_shift, dir)
            center_shift = shift_position(center_shift, dir)
        
        if search_res == True:
            search_res = search_letter(array, 'S', center_shift, dir)
        
        if search_res == True:
            num_xmas += 1
    
    return num_xmas


def solve_puzzle_04_02(filepath):
    """ Create an array from a text file, take each cell of
    the array in turn, search for the presence of x-MAS in all
    directions and return the total number of matches. """

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
    
    result_1 = solve_puzzle_04_01(filepath)
    print(f"Solution of the first puzzle of day 4: {result_1}.")

    result_2 = solve_puzzle_04_02(filepath)
    print(f"Solution of the second puzzle of day 4: {result_2}.")


if __name__ == '__main__':
    main()
