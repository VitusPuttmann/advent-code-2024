"""
AoC 2024: Provision of solutions

This script provides solutions to the challenges of the Advent of Code (AoC)
2024 (https://adventofcode.com/) in response to user input, including the
respective execution time and code.

Author: Vitus Püttmann
Date:   26.03.2025
"""


import os


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


def print_script(day: int):
    """ Display the content of the script of the selected day. """

    script_path = os.path.join(os.getcwd(), f"src", "advent_code_2024",
                               f"day_{day:02d}.py")
    
    with open(script_path) as script:
        print(script.read())


if __name__ == '__main__':
    """ Import scripts with solutions for days, obtain user input, and
        provide solution, execution time and scripts as requested. """
    
    import src.advent_code_2024 as aoc

    while True:
        choice_day = prompt_day()
        function_name = f"main_day_{choice_day}"

        try:
            main_function = getattr(aoc, function_name)
            main_function()

            interest_script = input("If you want to see the code, "
                                    "enter 'yes'.\n")
            
            if interest_script.lower() == 'yes':
                print_script(choice_day)

        except AttributeError:
            print(f"The challenge of day {choice_day} has not been solved yet.")

        interest_day = input("If you want the solution to another challenge, "
                             "enter 'yes'\n")
        
        if not interest_day.lower() == 'yes':
            break
