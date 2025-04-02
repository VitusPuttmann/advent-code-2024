"""
This module contains functions that solve the challenges of day 7 of the
Advent of Code 2024 (https://adventofcode.com/).
"""


import os
import time


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_07_input.txt")


def calc_runtime(func):
    """ Measure runtime of function. """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = round(end_time - start_time, 5)
        return result, runtime
    return wrapper


def list_equations(filepath: str) -> list[list[int]]:
    """ Read a text file and create a list consisting of its equations. """

    equations_list = []
    with open(filepath, 'r') as file_input:
        for line in file_input:
            str_line = line.strip()
            str_line = str_line.replace(':', '')
            int_line = [int(x) for x in str_line.split()]
            equations_list.append(int_line)

    return equations_list


def calculate_outcomes(int_list: list[int], concat: bool = False):
    """ Calculate all potential outcomes of sequentially combining the values
        of a list via addition or multiplication or via the addition of
        concatenation. """

    if concat == False:
        outcomes_list = [int_list.pop(0)]
        for val in int_list:
            addition_list = [x + val for x in outcomes_list]
            multiplication_list = [x * val for x in outcomes_list]
            outcomes_list = addition_list + multiplication_list
    
    if concat == True:
        outcomes_list = [int_list.pop(0)]
        for val in int_list:
            addition_list = [x + val for x in outcomes_list]
            multiplication_list = [x * val for x in outcomes_list]
            concatenation_list = [
                int(str(x)+str(val)) for x in outcomes_list
            ]
            outcomes_list = (
                addition_list + multiplication_list + concatenation_list
            )

    return outcomes_list


@calc_runtime
def solve_puzzle_07(filepath: str, second: bool = False) -> int:
    """ Create a list of lists from a text file, separate the outcome from the
        list, calculate all possible results for the remaining numbers, check
        whether the outcome is among the results, and calculate sum of results
        for which this is the case. """
    
    equations_list = list_equations(filepath)

    outcomes_sum = 0

    for equation in equations_list:
        outcome = equation.pop(0)
        potential_outcomes = calculate_outcomes(equation, concat=second)
        if outcome in potential_outcomes:
            outcomes_sum += outcome
    
    return outcomes_sum


def main():
    """ Execute the main functions with the main input. """

    result_1, runtime_1 = solve_puzzle_07(filepath)
    print(f"Solution to the first puzzle of day 7: {result_1}\n"
          f"Runtime: {runtime_1} seconds\n")

    result_1, runtime_1 = solve_puzzle_07(filepath, second=True)
    print(f"Solution to the first puzzle of day 7: {result_1}\n"
          f"Runtime: {runtime_1} seconds\n")


if __name__ == '__main__':
    main()
