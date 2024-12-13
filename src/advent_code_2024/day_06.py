""" This module contains functions that solve the challenges of day 6
    of the advent of code 2024 (https://adventofcode.com/).
"""

import copy
import itertools
import os


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_06_input.txt")


def create_grid(filepath):
    """ Read a text file and create a grid in the form of a list
        of lists. """
    
    fin = open(filepath, 'r')

    grid = []
    for line in fin:
        str_line = line.strip()
        str_list = list(str_line)
        grid.append(str_list)
    
    return grid


def make_step(start, direction):
    """ Obtain coordinates of a target cell in a specified direction
        from a start cell. """
    
    if direction == 't':
        end = (start[0]-1, start[1])
    elif direction == 'r':
        end = (start[0], start[1]+1)
    elif direction == 'b':
        end = (start[0]+1, start[1])
    elif direction == 'l':
        end = (start[0], start[1]-1)
    else:
        print("Invalid direction specification.")
    
    return end


def in_grid(grid, point):
    """ Check whether a point is within a grid. """

    in_grid = True

    point_x = point[0]
    point_y = point[1]

    if point_x < 0 or point_x > (len(grid[0]) - 1):
        in_grid = False
    if point_y < 0 or point_y > (len(grid) - 1):
        in_grid = False
    
    return in_grid


def solve_puzzle_06_01(filepath):
    """ Create a grid from a text file, find the starting point, 
        calculate the path out of the grid, and calculate its length. """
    
    grid = create_grid(filepath)

    start_point_x = None
    start_point_y = None

    for row in grid:
        if '^' in row:
            start_point_x = grid.index(row)
            start_point_y = row.index('^')
    
    center_shift = (start_point_x, start_point_y)
    grid[start_point_x][start_point_y] = '.'

    directions = ['t', 'r', 'b', 'l']
    directions_cycle = itertools.cycle(directions)
    current_direction = next(directions_cycle)

    field_list = []
    max_steps = 1000
    for round in range(max_steps):
        field_list.append(center_shift)
        target_cor = make_step(center_shift, current_direction)

        if in_grid(grid, target_cor) == False:
            break
        
        target_val = grid[target_cor[0]][target_cor[1]]
        if target_val == '.':
            center_shift = make_step(center_shift, current_direction)
        elif target_val == '#':
            current_direction = next(directions_cycle)
            center_shift = make_step(center_shift, current_direction)

    sum_steps = len(set(field_list))

    return sum_steps


def solve_puzzle_06_02(filepath):
    """ Create a grid from a text file, find the starting point, 
        create altered grids, and calculate the number of grids
        that loop. """
    
    grid = create_grid(filepath)

    start_point_x = None
    start_point_y = None
    for row in grid:
        if '^' in row:
            start_point_x = grid.index(row)
            start_point_y = row.index('^')
    
    grid[start_point_x][start_point_y] = '.'

    row_numbers = range(len(grid))
    col_numbers = range(len(grid[0]))
    
    grid_list = []
    for x, y in itertools.product(row_numbers, col_numbers):
        new_grid = copy.deepcopy(grid)
        if (x, y) != (start_point_x, start_point_y):
            new_grid[x][y] = '#'
            grid_list.append(new_grid)

    sum_grids = 0
    for grid_alt in grid_list:
        center_shift = (start_point_x, start_point_y)

        directions = ['t', 'r', 'b', 'l']
        directions_cycle = itertools.cycle(directions)
        current_direction = next(directions_cycle)

        field_dict = {}

        loop = False
        while loop == False:
            target_cor = make_step(center_shift, current_direction)
            if in_grid(grid_alt, target_cor) == False:
                break
            
            target_val = grid_alt[target_cor[0]][target_cor[1]]
            if target_val == '.':
                center_shift = make_step(center_shift, current_direction)
            elif target_val == '#':
                current_direction = next(directions_cycle)
                target_cor = make_step(center_shift, current_direction)
                target_val = grid_alt[target_cor[0]][target_cor[1]]
                if target_val == '.':
                    center_shift = make_step(center_shift, current_direction)
                elif target_val == '#':
                    current_direction = next(directions_cycle)
                    target_cor = make_step(center_shift, current_direction)
                    target_val = grid_alt[target_cor[0]][target_cor[1]]
                    if target_val == '.':
                        center_shift = make_step(center_shift, current_direction)
                    else:
                        print('-----')
                        print('Problem when turning to cell:')
                        print(center_shift)
            
            if center_shift not in field_dict:
                field_dict[center_shift] = 1
            else:
                field_dict[center_shift] += 1

            if field_dict[center_shift] > 4:
                loop = True
            
        if loop == True:
            sum_grids += 1
        
    return sum_grids

def main():
    """ Execute the main functions with the main input. """

    result_1 = solve_puzzle_06_01(filepath)
    print(f"Solution of the first puzzle of day 6: {result_1}.")

    result_2 = solve_puzzle_06_02(filepath)
    print(f"Solution of the second puzzle of day 6: {result_2}.")


if __name__ == '__main__':
    main()
