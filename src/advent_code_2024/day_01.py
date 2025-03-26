"""
This module contains functions that solve the challenges of day 1 of the
Advent of Code 2024 (https://adventofcode.com/).
"""


import os
import time

from collections import Counter


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


def prep_lists(filepath: str):
    """ Read a text file with two columns and create a list for each column. """
    
    list_1 = []
    list_2 = []
    
    with open(filepath, 'r') as file_input:
        for line in file_input:
            line = line.strip()
            str_list = line.split()
            list_1.append(int(str_list[0]))
            list_2.append(int(str_list[1]))
    
    return list_1, list_2


@calc_runtime
def solve_puzzle_01_01(filepath: str) -> int:
    """ Calculate the distance between two lists. """
    
    list_1, list_2 = prep_lists(filepath)
    
    list_1.sort()
    list_2.sort()
    
    distance = sum(abs(first - second) for first, second in zip(list_1, list_2))

    return distance


@calc_runtime
def solve_puzzle_01_02(filepath: str) -> int:
    """Calculate the similarity score of two lists. """
    
    list_1, list_2 = prep_lists(filepath)

    second_counts = Counter(list_2)

    similarity = sum(num * second_counts[num] for num in list_1)
    
    return similarity


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
