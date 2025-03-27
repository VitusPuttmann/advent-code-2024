"""
This module contains functions that solve the challenges of day 5
    of the Advent of Code 2024 (https://adventofcode.com/).
"""


import os
import time


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_05_input.txt")


def calc_runtime(func):
    """ Measure runtime of function. """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = round(end_time - start_time, 5)
        return result, runtime
    return wrapper


def compile_rules(filepath: str) -> dict:
    """ Read in a text file, extract the section with rules and create a
        dictionary comprising the rules. """
    
    rules_dict = {}

    with open(filepath, 'r') as input_file:
        for line in input_file:
            if '|' in line:
                line_text = line.strip()
                str_list = str.split(line_text, '|')
                int_list = list(map(int, str_list))
                before = int_list[0]
                after = int_list[1]

                if before not in rules_dict:
                    rules_dict[before] = [after]
                else:
                    rules_dict[before].append(after)
    
    return rules_dict


def compile_updates(filepath: str) -> list[list[int]]:
    """ Read in a text file, extract the section with 'update'-cases, create a
        list for each case and combine the lists into a list. """

    updates_list = []

    with open(filepath, 'r') as input_file:
        for line in input_file:
            if ',' in line:
                line_text = line.strip()
                str_list = str.split(line_text, ',')
                int_list = list(map(int, str_list))
                updates_list.append(int_list)

    return updates_list


def verify_rule(num_list: list[int], num_left: int, num_right: int) -> bool:
    """ Check whether a rule is followed by two numbers. """

    position_1 = num_list.index(num_left)
    position_2 = num_list.index(num_right)

    return position_1 < position_2


def check_list(num_list: list[int], rule_dict: dict) -> bool:
    """ Check whether all rules are followed for an entire list. """

    for num_val in num_list:
        if num_val not in rule_dict:
            continue

        nums_right = rule_dict[num_val]

        for num_comp in nums_right:
            if num_comp not in num_list:
                continue
            check_res = verify_rule(num_list, num_val, num_comp)

            if not check_res:
                return False

    return True


def correct_list(num_list: list[int], rule_dict: dict) -> list[int]:
    """ Correct a list by reordering its elements based on the rules. """

    num_list_correct = num_list.copy()
    for num_val in num_list:
        if num_val not in rule_dict:
            continue

        nums_right = rule_dict[num_val]
        for num_comp in nums_right:
            if num_comp not in num_list:
                continue

            check_res = verify_rule(num_list_correct, num_val, num_comp)

            if not check_res:
                pop_index = num_list_correct.index(num_val)
                insert_val = num_list_correct.pop(pop_index)
                insert_index = num_list_correct.index(num_comp)
                num_list_correct.insert(insert_index, insert_val)

    return num_list_correct


@calc_runtime
def solve_puzzle_05_01(filepath: str) -> int:
    """ Compile the rulebook and the 'update'-cases from a textfile, identify
        the correct cases, extract the middle number of these cases and
        calculate the sum of these numbers. """
    
    rules_dict = compile_rules(filepath)
    updates_list = compile_updates(filepath)

    sum_correct = 0
    for update in updates_list:
        update_correct = check_list(update, rules_dict)

        if update_correct:
            middle_pos = int(len(update) / 2)
            sum_value = update[middle_pos]
            sum_correct += sum_value

    return sum_correct


@calc_runtime
def solve_puzzle_05_02(filepath: str) -> int:
    """ Compile the rulebook and the 'update'-cases from a textfile, identify
        the incorrect cases, correct these cases, extract the middle number of
        these cases and calculate the sum of these numbers. """
    
    rules_dict = compile_rules(filepath)
    updates_list = compile_updates(filepath)

    sum_corrected = 0
    for update in updates_list:
        update_correct = check_list(update, rules_dict)

        if not update_correct:
            corrected_list = correct_list(update, rules_dict)
            middle_pos = int(len(corrected_list) / 2)
            sum_value = corrected_list[middle_pos]
            sum_corrected += sum_value
    
    return sum_corrected


def main():
    """ Execute the main functions with the main input. """
    
    result_1, runtime_1 = solve_puzzle_05_01(filepath)
    print(f"Solution to the first puzzle of day 5: {result_1}\n"
          f"Runtime: {runtime_1} seconds\n")

    result_2, runtime_2 = solve_puzzle_05_02(filepath)
    print(f"Solution to the second puzzle of day 5: {result_2}\n"
          f"Runtime: {runtime_2} seconds\n")


if __name__ == '__main__':
    main()
