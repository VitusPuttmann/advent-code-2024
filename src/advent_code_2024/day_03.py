"""
This module contains functions that solve the challenges of day 3 of the
Advent of Code 2024 (https://adventofcode.com/).
"""


import os
import re
import time


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_03_input.txt")


def calc_runtime(func):
    """ Measure runtime of function. """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = round(end_time - start_time, 5)
        return result, runtime
    return wrapper


def extract_strings(filepath: str) -> list[tuple]:
    """ Read a text file, extract elements of 'mul()'-strings, and store them
        as a list of tuples. """
    
    with open(filepath, 'r') as file_input:
        str_list = []
        for line in file_input:
            line_strings = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
            for string_expr in line_strings:
                str_list.append(string_expr)
    
    return str_list


def extract_strings_do(filepath: str) -> list[tuple]:
    """ Read a text file, extract elements of 'mul()'-strings, including
        dependence on do() / don't(), and store them as list of tuples. """
    
    with open(filepath, 'r') as file_input:
        string_long = ""
        for line in file_input:
            add_line = re.sub(r"[\n\r]", "", line)
            string_long += " " + add_line
    
    string_list = re.split(r"don't\(\)", string_long)
    string_clean = ""
    init_part = string_list[0]
    init_part = re.sub(r"do\(\)(.*)", "", init_part)
    string_clean += init_part
    
    for split_string in string_list:
        if re.search(r"do\(\)", split_string):
            add_string = re.sub(r"^(.*?)do\(\)", "", split_string)
            string_clean += add_string
    
    str_list = []
    strings_rel = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', string_clean)
    for string_expr in strings_rel:
            str_list.append(string_expr)

    return str_list


@calc_runtime
def solve_puzzle_03(filepath: str, do: bool = False) -> int:
    """ Multiply the extracted elements. """
    
    if not do:
        mul_list = extract_strings(filepath)
    if do:
        mul_list = extract_strings_do(filepath)
    
    sum_mult = sum(int(x) * int(y) for x, y in mul_list)
    
    return sum_mult


def main():
    """ Execute the main function with the main input in two versions. """
    
    result_1, runtime_1 = solve_puzzle_03(filepath, do=False)
    print(f"Solution to the first puzzle of day 3: {result_1}\n"
          f"Runtime: {runtime_1} seconds\n")
    
    result_2, runtime_2 = solve_puzzle_03(filepath, do=True)
    print(f"Solution to the second puzzle of day 3: {result_2}\n"
          f"Runtime: {runtime_2} seconds\n")


if __name__ == '__main__':
    main()
