"""
AoC 2024: Provision of solutions

This script provides solutions to the challenges of the Advent of Code (AoC)
2024 (https://adventofcode.com/) in response to user input, including the
respective execution time and code.

Author: Vitus Püttmann
Date:   26.03.2025
"""


import os


def input_day():
    """ Obtains and checks user input for selection of day. """

    print("For which day of the Advent of Code 2024 do you want the solution?")
    
    while True:
        try:
            choice_day = int(input("Day: "))
            if 1 <= choice_day <= 24:
                return choice_day
            else:
                print("Please enter a number between 1 and 24.")
        except ValueError:
            print("Please enter a valid number.")


if __name__ == '__main__':
    """ Imports scripts with solutions for days, obtains user input, and
        provides solutions, execution time and code as requested. """
    
    import src.advent_code_2024 as aoc

    while True:
        choice_day = input_day()
   
        function_name = f"main_day_{choice_day}"

        if len(str(choice_day)) == 1:
            choice_day_long = "0" + str(choice_day)
        else:
            choice_day_long = str(choice_day)

        try:
            main_function = getattr(aoc, function_name)
            main_function()

            interest_script = input("If you want to see the code, "
                                    "enter 'yes'.\n")
            
            if interest_script.lower() == 'yes':
                script_path = (
                    os.getcwd() + r"\src\advent_code_2024\day_" +
                    choice_day_long + ".py"
                )
                with open(script_path, 'r') as script:
                    print(script.read())

        except AttributeError:
            print(f"The challenge has not been solved yet.")

        interest_day = input("If you want the solution to another challenge, "
                             "enter 'yes'\n")
        
        if not interest_day.lower() == 'yes':
            break
