""" This module contains functions that solve the challenges of day 5
    of the advent of code 2024 (https://adventofcode.com/).
"""

import os
import re


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_05_input.txt")


def compile_rules(filepath):
    """ Read in text file, extract section with rules and create
        dictionary comprising the rules. """
    
    fin = open(filepath, 'r')
    
    rules_dict = {}
    for line in fin:
        if re.search(r'\|', line):
            line_text = line.strip()
            str_list = str.split(line_text, '|')
            int_list = list(map(int, str_list))
            before = int_list[0]
            after = int_list[1]

            if not before in rules_dict:
                rules_dict[before] = [after]
            else:
                rules_dict[before].append(after)
    
    fin.close()
    
    return rules_dict


def compile_updates(filepath):
    """ Read in text file, extract section with 'update'-cases, create
        list for each case and combine lists into list. """
        
    fin = open(filepath, 'r')

    updates_list = []
    for line in fin:
        if re.search(',', line):
            line_text = line.strip()
            str_list = str.split(line_text, ',')
            int_list = list(map(int, str_list))
            updates_list.append(int_list)

    return updates_list


def verify_rule(num_list, num_left, num_right):
    """ Check whether a rule is followed by two numbers. """

    position_1 = num_list.index(num_left)
    position_2 = num_list.index(num_right)

    return position_1 < position_2


def check_list(num_list, rule_dict):
    """ Check whether all rules are followed for an entire list. """

    list_check = True

    violations = 0
    for num_val in num_list:
        if not num_val in rule_dict:
            continue

        nums_right = rule_dict[num_val]

        for num_comp in nums_right:
            if not num_comp in num_list:
                continue
            check_res = verify_rule(num_list, num_val, num_comp)

            if check_res == False: violations += 1

    if violations > 0: list_check = False

    return list_check


def correct_list(num_list, rule_dict):
    """ Correct a list by reordering its elements based on the rules. """

    num_list_correct = num_list.copy()
    for num_val in num_list:
        if not num_val in rule_dict:
            continue

        nums_right = rule_dict[num_val]
        for num_comp in nums_right:
            if not num_comp in num_list:
                continue

            check_res = verify_rule(num_list_correct, num_val, num_comp)

            if check_res == False:
                pop_index = num_list_correct.index(num_val)
                insert_val = num_list_correct.pop(pop_index)
                insert_index = num_list_correct.index(num_comp)
                num_list_correct.insert(insert_index, insert_val)

    return num_list_correct


def solve_puzzle_05_01(filepath):
    """ Compile the rulebook and the 'update'-cases from a textfile,
        identify the correct cases, extract the middle number of these 
        cases and calculate the sum of these numbers. """
    
    rules_dict = compile_rules(filepath)
    updates_list = compile_updates(filepath)

    sum_correct = 0
    for update in updates_list:
        update_correct = check_list(update, rules_dict)

        if update_correct == True:
            middle_pos = int(len(update) / 2)
            sum_value = update[middle_pos]
            sum_correct += sum_value

    return sum_correct


def solve_puzzle_05_02(filepath):
    """ Compile the rulebook and the 'update'-cases from a textfile,
        identify the incorrect cases, correct these cases, extract the
        middle number of these cases and calculate the sum
        of these numbers. """
    
    rules_dict = compile_rules(filepath)
    updates_list = compile_updates(filepath)

    sum_corrected = 0
    for update in updates_list:
        update_correct = check_list(update, rules_dict)

        if update_correct == False:
            corrected_list = correct_list(update, rules_dict)
            middle_pos = int(len(corrected_list) / 2)
            sum_value = corrected_list[middle_pos]
            sum_corrected += sum_value
    
    return sum_corrected


def main():
    """ Execute the main functions with the main input. """
    
    result_1 = solve_puzzle_05_01(filepath)
    print(f"Solution of the first puzzle of day 5: {result_1}.")

    result_2 = solve_puzzle_05_02(filepath)
    print(f"Solution of the second puzzle of day 5: {result_2}.")


if __name__ == '__main__':
    main()
