""" This module contains functions that solve the challenges of day 3
    of the advent of code 2024 (https://adventofcode.com/).
"""

import operator
import os
import re


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_03_input.txt")


def extract_strings(filepath):
    """ Read a text file, extract specified 'mul()'-strings and
        prepare them for execution. """
    fin = open(filepath, 'r')
    str_list = []
    for line in fin:
        line_strings = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
        for string_expr in line_strings:
            string_expr_con = 'operator.' + string_expr
            str_list.append(string_expr_con)
    fin.close()
    return str_list


def extract_strings_do(filepath):
    """ Read a text file, extract specified 'mul()'-strings, including
        dependence on do() / don't() and prepare them for execution. """
    fin = open(filepath, 'r')
    string_long = ""
    for line in fin:
        add_line = re.sub(r"[\n\r]", "", line)
        string_long += " " + add_line
    fin.close()
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
    strings_rel = re.findall(r'mul\(\d{1,3},\d{1,3}\)', string_clean)
    for string_expr in strings_rel:
            string_expr_con = 'operator.' + string_expr
            str_list.append(string_expr_con)
    return str_list


def solve_puzzle_03(filepath, do=False):
    """ Solve the puzzles of day 3 by extracting and executing
        the 'mul()'-functions. """
    if do == False:
        exec_list = extract_strings(filepath)
    if do == True:
        exec_list = extract_strings_do(filepath)
    acc_res = 0
    for mul in exec_list:
        res = eval(mul)
        acc_res += res
    return acc_res


def main():
    """ Execute the main function with the main input in two versions. """
    result_1 = solve_puzzle_03(filepath, do=False)
    print(f"Solution of the first puzzle of day 3: {result_1}.")

    result_2 = solve_puzzle_03(filepath, do=True)
    print(f"Solution of the second puzzle of day 3: {result_2}.")


if __name__ == '__main__':
    main()
