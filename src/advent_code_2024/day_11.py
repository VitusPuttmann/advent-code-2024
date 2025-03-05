""" This module contains functions that solve the challenges of day 11
    of the advent of code 2024 (https://adventofcode.com/).
"""


import os


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_11_input.txt")


def create_list(filepath: str) -> list[int]:
    """ Open file, read line and transfer content into list. """

    with open(filepath, 'r') as input_file:
        line_string = input_file.readline().strip()
        line_list = line_string.split()
        line_list = [int(x) for x in line_list]
    
    return line_list


def transform_value(value: int) -> list[int]:
    """ Apply one of three transformations to value."""
    
    if value == 0:
        return [1]
    elif len(str(value)) % 2 == 0:
        first_part = int(str(value)[:(len(str(value)))//2])
        second_part = int(str(value)[(len(str(value)))//2:])
        return [first_part, second_part]
    else:
        return [value*2024]


def add_dictionary(memory: dict, value: int, steps: int):
    """ Calculate dictionary entries for specific value and number
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
    """ Create dictionary with entries for values from 1 to 10 for
        a given number of steps. """

    memory = {}

    for number in range(1, total_steps+1):
        for value in range(1, 10):
            add_dictionary(memory, value, number)
    
    return memory


def solve_puzzle_11(filepath: str, steps: int = 25) -> int:
    """ Create list from input file, create dictionary for given number
        of steps, and calculate final number of values for transformation
        of initial list. """

    input = create_list(filepath)

    memory = create_dictionary(steps)
    
    output = 0

    for entry_input in input:
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

    result_1 = solve_puzzle_11(filepath)
    print(f"Solution of the first puzzle of day 11: {result_1}.")

    result_2 = solve_puzzle_11(filepath, 75)
    print(f"Solution of the second puzzle of day 11: {result_2}.")


if __name__ == '__main__':
    main()
