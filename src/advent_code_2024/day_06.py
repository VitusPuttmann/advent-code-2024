"""
This module contains functions that solve the challenges of day 6 of the
Advent of Code 2024 (https://adventofcode.com/).
"""


import copy
import itertools
import os
import time


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_06_input.txt")


class Walker():
    """ Class to represent a 'guard' moving over a grid. """

    def __init__(self, grid: list[list[str]], start: tuple):
        self.directions = {
            't': (-1, 0),
            'r': (0, 1),
            'b': (1, 0),
            'l': (0, -1)
        }
        self.direction_cycle = itertools.cycle(self.directions.keys())
        self.direction = next(self.direction_cycle)
        self.grid = grid
        self.grid_y = len(grid) - 1
        self.grid_x = len(grid[0]) - 1
        self.y_coord = start[0]
        self.x_coord = start[1]

    def make_step(self):
        end_y = self.y_coord + self.directions[self.direction][0]
        end_x = self.x_coord + self.directions[self.direction][1]

        if end_y < 0 or end_y > self.grid_y:
            return False
        elif end_x < 0 or end_x > self.grid_x:
            return False
        elif self.grid[end_y][end_x] == '#':
            self.direction = next(self.direction_cycle)
            return self.make_step()
        else:
            self.y_coord = end_y
            self.x_coord = end_x
            return (end_y, end_x)


def calc_runtime(func):
    """ Measure runtime of function. """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = round(end_time - start_time, 5)
        return result, runtime
    return wrapper


def create_grid(filepath: str) -> list[list[str]]:
    """ Read a text file and create a grid in the form of a list
        of lists. """
    
    with open(filepath, 'r') as file_input:
        grid = []
        for line in file_input:
            str_line = line.strip()
            str_list = list(str_line)
            grid.append(str_list)
    
    return grid


@calc_runtime
def solve_puzzle_06_01(filepath: str) -> int:
    """ Create a grid from a text file, find the starting point, instantiate 
        'Walker' that follows the path out of the grid, and calculate its
        length. """
    
    grid = create_grid(filepath)

    start_point_y = None
    start_point_x = None

    for row in grid:
        if '^' in row:
            start_point_y = grid.index(row)
            start_point_x = row.index('^')

    
    grid[start_point_y][start_point_x] = '.'

    guard = Walker(grid, (start_point_y, start_point_x))
    grid_points = [(start_point_y, start_point_x)]
    
    proceed = True
    while proceed:
        proceed = guard.make_step()
        if proceed and (proceed not in grid_points):
                grid_points.append(proceed)

    return len(grid_points)


@calc_runtime
def solve_puzzle_06_02(filepath: str) -> int:
    """ Create a grid from a text file, find the starting point, create altered
        grids, initiate a 'Walker' for each grip, and calculate the number of
        grids that loop. """
    
    grid = create_grid(filepath)

    start_point_y = None
    start_point_x = None

    for row in grid:
        if '^' in row:
            start_point_y = grid.index(row)
            start_point_x = row.index('^')

    
    grid[start_point_y][start_point_x] = '.'


    row_numbers = range(len(grid))
    col_numbers = range(len(grid[0]))
    
    sum_grids = 0
    for y, x in itertools.product(row_numbers, col_numbers):
        if (y, x) == (start_point_y, start_point_x):
            continue
        
        if grid[y][x] == '#':
            continue
        
        new_grid = copy.deepcopy(grid)
        new_grid[y][x] = '#'
            
        guard = Walker(new_grid, (start_point_y, start_point_x))
        grid_pos = {(start_point_y, start_point_x, guard.direction)}
    
        proceed = True
        while proceed:
            proceed = guard.make_step()
            if proceed:
                pos = (proceed[0], proceed[1], guard.direction)
                if pos in grid_pos:
                    sum_grids += 1
                    break
                else:
                    grid_pos.add(pos)

    return sum_grids


def main():
    """ Execute the main functions with the main input. """

    result_1, runtime_1 = solve_puzzle_06_01(filepath)
    print(f"Solution to the first puzzle of day 6: {result_1}\n"
          f"Runtime: {runtime_1} seconds\n")

    result_2, runtime_2 = solve_puzzle_06_02(filepath)
    print(f"Solution to the second puzzle of day 6: {result_2}\n"
          f"Runtime: {runtime_2} seconds\n")


if __name__ == '__main__':
    main()
