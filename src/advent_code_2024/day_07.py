""" This module contains functions that solve the challenges of day 7
    of the advent of code 2024 (https://adventofcode.com/).
"""

import os


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_07_input.txt")


def list_equations(filepath):
    """ Read a text file and create a list consisting of
        its equations. """
    
    fin = open(filepath, 'r')

    equations_list = []
    for line in fin:
        str_line = line.strip()
        str_list = str.split(str_line, ':')
        list_first = [int(str_list[0])]
        list_second = str_list[1].strip()
        list_second = list_second.strip()
        list_second = str.split(list_second, " ")
        list_second = [int(x) for x in list_second]
        list_combined =  list_first + list_second
        equations_list.append(list_combined)
    
    return equations_list


def calculate_outcomes(int_list, concat=False):
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


def solve_puzzle_07_01(filepath):
    """ Create a list from a text file, identify all possible outcomes, 
        and calculate their sum. """
    
    equations_list = list_equations(filepath)

    outcomes_sum = 0

    for equation in equations_list:
        outcome = equation.pop(0)
        potential_outcomes = calculate_outcomes(equation)
        if outcome in potential_outcomes:
            outcomes_sum += outcome
    
    return outcomes_sum


def solve_puzzle_07_02(filepath):
    """ Create a list from a text file, identify all possible outcomes
        including concatenation, and calculate their sum. """
    
    equations_list = list_equations(filepath)

    outcomes_sum = 0

    for equation in equations_list:
        outcome = equation.pop(0)
        potential_outcomes = calculate_outcomes(equation, concat=True)
        if outcome in potential_outcomes:
            outcomes_sum += outcome
    
    return outcomes_sum


def main():
    """ Execute the main functions with the main input. """

    result_1 = solve_puzzle_07_01(filepath)
    print(f"Solution of the first puzzle of day 7: {result_1}.")

    result_2 = solve_puzzle_07_02(filepath)
    print(f"Solution of the second puzzle of day 7: {result_2}.")


if __name__ == '__main__':
    main()
