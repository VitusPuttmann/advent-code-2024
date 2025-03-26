"""
AoC 2024: Provision of solutions

This script provides solutions to the challenges of the Advent of Code (AoC)
2024 (https://adventofcode.com/) in response to user input, including the
respective execution time and code.

Author: Vitus Püttmann
Date:   26.03.2025
"""


import os
import importlib


def prompt_day() -> int:
    """ Prompt user for day input and ensure it is a valid day (1-24). """

    print("For which day of the Advent of Code 2024 do you want the solution?")
    
    while True:
        try:
            choice_day = int(input("Day: "))
            if 1 <= choice_day <= 24:
                return choice_day
            else:
                print("Please enter a number between 1 and 24.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 24.")


def load_day_function(day: int):
    """ Dynamically load the function for the requested day from the
    'src.advent_code_2024' module. """

    try:
        module_name = f"src.advent_code_2024.day_{day:02d}"
        module = importlib.import_module(module_name)
        return getattr(module, "main")
    except (ModuleNotFoundError, AttributeError):
        print(f"The challenge of day {day} has not been solved yet.")
        return None


def print_script(day: int):
    """ Display the content of the script of the selected day. """

    script_path = os.path.join(os.getcwd(), f"src", "advent_code_2024",
                               f"day_{day:02d}.py")
    
    with open(script_path) as script:
        print(script.read())


if __name__ == '__main__':
    """ Import scripts with solutions for days, obtain user input, and
        provide solution, execution time and scripts as requested. """
    
    while True:
        choice_day = prompt_day()
        main_function = load_day_function(choice_day)

        if main_function:
            main_function()

            interest_script = input("If you want to see the code, "
                                    "enter 'yes'.\n")
            
            if interest_script.lower() == 'yes':
                print_script(choice_day)

        interest_day = input("If you want the solution to another challenge, "
                             "enter 'yes'\n")
        
        if not interest_day.lower() == 'yes':
            break
