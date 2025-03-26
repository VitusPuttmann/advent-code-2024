"""
This module contains functions that solve the challenges of day 2 of the
Advent of Code 2024 (https://adventofcode.com/).
"""


import os
import time


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_02_input.txt")

def calc_runtime(func):
    """ Measure runtime of function. """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = round(end_time - start_time, 5)
        return result, runtime
    return wrapper


def prep_report(filepath: str) -> list:
    """ Read a text file with numeric values and create a list for each row
    and combine them into a list. """

    report_list = []

    with open(filepath, 'r') as file_input:
        for line in file_input:
            num_list = list(map(int, line.split()))
            report_list.append(num_list)
    
    return report_list


def check_order(num_list: list) -> bool:
    """ Check whether the numeric values in a list are ordered. """

    if sorted(num_list, reverse=False) == num_list:
        return True
    if sorted(num_list, reverse=True) == num_list:
        return True
    
    return False


def check_distance(num_list: list) -> bool:
    """ Check whether adjacent values in a list have a distance between one
    and three. """

    for num_list_val in range(len(num_list)-1):
        abs_diff = abs(num_list[num_list_val] - num_list[num_list_val+1])
        if abs_diff == 0 or abs_diff > 3:
            return False
    
    return True


@calc_runtime
def solve_puzzle_02(filepath: str, dampened: bool = False) -> int:
    """ Check order and distance of lists and return number of safe lists. """
    
    report_list = prep_report(filepath)

    safe_total = 0

    for report in report_list:
        order = check_order(report)
        distance = check_distance(report)
        if order and distance:
            safe_total += 1
            continue

        if dampened:
            for i in range(len(report)):
                report_red = report[:i] + report[i+1:]
                order_red = check_order(report_red)
                distance_red = check_distance(report_red)
                if order_red and distance_red:
                    safe_total += 1
                    break

    return safe_total


def main():
    """ Execute the main function with the main input in two versions. """
    
    result_1, runtime_1 = solve_puzzle_02(filepath, dampened=False)
    print(f"Solution to the first puzzle of day 2: {result_1}\n"
          f"Runtime: {runtime_1} seconds\n")

    result_2, runtime_2 = solve_puzzle_02(filepath, dampened=True)
    print(f"Solution to the second puzzle of day 2: {result_2}\n"
          f"Runtime: {runtime_2} seconds\n")


if __name__ == '__main__':
    main()
