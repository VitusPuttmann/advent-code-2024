""" This module contains functions that solve the challenges of day 1
    of the advent of code 2024 (https://adventofcode.com/).
"""


import re
import os
import time
import inspect


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_01_input.txt")


def calc_runtime(func):
    """ Measure runtime of function. """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = round(end_time - start_time, 5)
        return result, runtime
    return wrapper


def prep_lists(filepath):
    """ Read a text file with two columns and create a list for each
        column. """
    
    fin = open(filepath, 'r')

    list_1 = []
    list_2 = []
    for line in fin:
        str_list = str.split(line, '   ')
        entry_1 = int(str_list[0])
        entry_2 = int(re.sub('\n', '', str_list[1]))
        list_1.append(entry_1)
        list_2.append(entry_2)
    
    fin.close()
    
    return list_1, list_2


def create_dict(val_list):
    """ Take a list and create a dictionary containing its unique elements
        and their frequencies. """
    
    val_dict = {}
    for num_val in val_list:
        if not num_val in val_dict:
            val_dict[num_val] = 1
        else:
            val_dict[num_val] += 1
    
    return val_dict


@calc_runtime
def solve_puzzle_01_01(filepath):
    """ Solve the first puzzle of day 1 by calculating the distance
        between two lists. """
    
    list_1, list_2 = prep_lists(filepath)
    
    list_1.sort()
    list_2.sort()
    
    res_acc = 0
    for val in range(len(list_1)):
        res_acc += abs(list_1[val] - list_2[val])
    
    return res_acc


@calc_runtime
def solve_puzzle_01_02(filepath):
    """ Solve the second puzzle of day 1 by calculating the
        similarity score of two lists. """
    
    list_1, list_2 = prep_lists(filepath)

    list_dict = create_dict(list_2)

    res_score = 0
    for list_val in list_1:
        if list_val in list_dict:
            res_score += (list_val * int(list_dict[list_val]))
    
    return res_score


def main():
    """ Execute the two main functions with the main input. """

    result_1, runtime_1 = solve_puzzle_01_01(filepath)
    print(f"Solution of the first puzzle of day 1: {result_1}\n"
          f"Runtime: {runtime_1} seconds\n")

    result_2, runtime_2 = solve_puzzle_01_02(filepath)
    print(f"Solution of the second puzzle of day 1: {result_2}\n"
          f"Runtime: {runtime_2} seconds\n")


if __name__ == '__main__':
    main()
