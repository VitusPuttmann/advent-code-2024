""" This module contains functions that solve the challenges of day 2
    of the advent of code 2024 (https://adventofcode.com/).
"""

import os


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_02_input.txt")


def prep_report(filepath):
    """ Read a text file with numeric values creating a list
        for each row and combine them into a list. """
    report_list = []
    fin = open(filepath, 'r')
    for line in fin:
        num_list = []
        str_list = str.split(line, ' ')
        for str_list_entry in str_list:
            num_list.append(int(str_list_entry))
        report_list.append(num_list)
    fin.close()
    return report_list


def check_order(num_list):
    """ Check whether the numeric values in a list are ordered. """
    check_res = False
    if sorted(num_list, reverse = False) == num_list: check_res = True
    if sorted(num_list, reverse = True) == num_list: check_res = True
    return check_res


def check_distance(num_list):
    """ Check whether adjacent values in a list are within a specific
    distance. """
    check_res = False
    acc_diff = 0
    for num_list_val in range(len(num_list)-1):
        abs_diff = abs(num_list[num_list_val] - num_list[num_list_val+1])
        if abs_diff > 0 and abs_diff < 4: acc_diff += 1
    if acc_diff == len(num_list)-1: check_res = True
    return check_res


def solve_puzzle_02(filepath, dampened=False):
    """ Solve the puzzles of day 2 by checking the order and distance
        of the rows of numbers. """
    report_list = prep_report(filepath)
    acc_safe_tot = 0
    for report in report_list:
        acc_safe_rep = 0
        order = check_order(report)
        distance = check_distance(report)
        if order == True and distance == True: acc_safe_rep += 1
        if dampened == True:
            for rep_val in range(len(report)):
                report_red = report.copy()
                report_red.pop(rep_val)
                order_red = check_order(report_red)
                distance_red = check_distance(report_red)
                if order_red == True and distance_red == True: acc_safe_rep += 1
        if acc_safe_rep > 0: acc_safe_tot += 1
    return acc_safe_tot


def main():
    """ Execute the main function with the main input in two versions. """
    result_1 = solve_puzzle_02(filepath, dampened=False)
    print(f"Solution of the first puzzle of day 2: {result_1}.")

    result_2 = solve_puzzle_02(filepath, dampened=True)
    print(f"Solution of the second puzzle of day 2: {result_2}.")


if __name__ == '__main__':
    main()
