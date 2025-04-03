"""
This module contains functions that solve the challenges of day 11 of the
Advent of Code 2024 (https://adventofcode.com/).
"""


import os
import time


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_11_input.txt")


def calc_runtime(func):
    """ Measure runtime of function. """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = round(end_time - start_time, 5)
        return result, runtime
    return wrapper


def create_list(filepath: str) -> list[int]:
    """ Open a text file, read each line and store the content as a list. """

    with open(filepath, 'r') as input_file:
        line_string = input_file.readline().strip()
        line_list = line_string.split()
        line_list = [int(x) for x in line_list]
    
    return line_list


def transform_value(value: int) -> list[int]:
    """ Apply one of three transformations to an input value."""
    
    if value == 0:
        return [1]
    elif len(str(value)) % 2 == 0:
        first_part = int(str(value)[:(len(str(value)))//2])
        second_part = int(str(value)[(len(str(value)))//2:])
        return [first_part, second_part]
    else:
        return [value*2024]


def add_dictionary(memory: dict, value: int, steps: int):
    """ Calculate dictionary entries for a specific value and defined number
        of steps. """

    memory_entry = (value, steps) 

    process_value = 0
    process_list = []
    process_list.append([value])
    for step in range(1, steps+1):
        process_list.append([])
        remaining_steps = steps + 1 - step
        for entry in process_list[step-1]:
            lookup = (entry, remaining_steps)
            if lookup in memory:
                process_value += memory[lookup]
            else:
                process_outcome = transform_value(entry)
                process_list[step].extend(process_outcome)
    num_values = len(process_list[steps])
    process_value += num_values

    memory[memory_entry] = process_value


def create_dictionary(total_steps: int) -> dict:
    """ Create a dictionary with entries for values from 1 to 10 for
        a given number of steps. """

    memory = {}

    for number in range(1, total_steps+1):
        for value in range(1, 10):
            add_dictionary(memory, value, number)
    
    return memory


@calc_runtime
def solve_puzzle_11(filepath: str, steps: int = 25) -> int:
    """ Create a list from an input file, create a dictionary for the given
        number of steps, and calculate the final number of values for the
        transformation of the initial list. """

    initial = create_list(filepath)

    memory = create_dictionary(steps)
    
    output = 0

    for entry_input in initial:
        process_value = 0
        process_list = []
        process_list.append([entry_input])
        for step in range(1, steps+1):
            process_list.append([])
            remaining_steps = steps + 1 - step
            for entry in process_list[step-1]:
                lookup = (entry, remaining_steps)
                if lookup in memory:
                    process_value += memory[lookup]
                else:
                    process_outcome = transform_value(entry)
                    process_list[step].extend(process_outcome)
        num_values = len(process_list[steps])
        process_value += num_values
        output += process_value
    
    return output


def main():
    """ Execute the main function with the main input. """

    result_1, runtime_1 = solve_puzzle_11(filepath)
    print(f"Solution to the first puzzle of day 11: {result_1}\n"
          f"Runtime: {runtime_1} seconds\n")

    result_2, runtime_2 = solve_puzzle_11(filepath, 75)
    print(f"Solution to the second puzzle of day 11: {result_2}\n"
          f"Runtime: {runtime_2} seconds\n")


if __name__ == '__main__':
    main()
