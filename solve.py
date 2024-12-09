""" Script for obtaining the solutions to the challenges of the
    advent of code 2024 (https://adventofcode.com/).
"""

if __name__ == '__main__':
    import src.advent_code_2024 as aoc

    print("For which day of the advent of code do you want the solution?")
    try:
        choice_day = int(input("Day: "))
    except ValueError:
        print("Please enter a valid number.")
        exit()
   
    if not (1 <= choice_day <= 24):
        print("Please enter a number between 1 and 24.")
        exit()
    
    function_name = f"main_day_{choice_day}"

    try:
        main_function = getattr(aoc, function_name)
        main_function()
    except AttributeError:
        print(f"The challenge has not been solved yet.")
