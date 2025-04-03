"""
This module contains functions that solve the challenges of day 10 of the
Advent of Code 2024 (https://adventofcode.com/).
"""


import os
import time


""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_10_input.txt")


trailheads_scores = {}


def calc_runtime(func):
    """ Measure runtime of function. """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = round(end_time - start_time, 5)
        return result, runtime
    return wrapper


def compile_adjacent_cells(
    grid: list[list[int]], coordinates: tuple, start: int
):
    """ Identify all adjacent cells of a specific cell on a grid (i.e. map)
        that contain the value of the initial cell plus 1. """

    max_y_index = len(grid) - 1
    max_x_index = len(grid[0]) - 1
    y_coordinate = coordinates[0]
    x_coordinate = coordinates[1]
    next = start + 1

    cell_list = []
    
    if y_coordinate - 1 >= 0:
        if grid[y_coordinate - 1][x_coordinate] == next:
            cell_list.append((y_coordinate - 1, x_coordinate))
    if x_coordinate + 1 <= max_x_index:
        if grid[y_coordinate][x_coordinate + 1] == next:
            cell_list.append((y_coordinate, x_coordinate + 1))
    if y_coordinate + 1 <= max_y_index:
        if grid[y_coordinate + 1][x_coordinate] == next:
            cell_list.append((y_coordinate + 1, x_coordinate))
    if x_coordinate - 1 >= 0:
        if grid[y_coordinate][x_coordinate - 1] == next:
            cell_list.append((y_coordinate, x_coordinate - 1))
    
    return cell_list


class Hiker():
    """ Object to identify patterns on the grids (i.e. map) by moving from cell
        to cell. """

    def __init__(self,
        grid: list[list[int]],
        trailhead: tuple[int, int],
        coordinates: tuple[int, int],
        start: int = 0
    ):
        self.grid = grid
        self.trailhead = trailhead
        self.coordinates = coordinates
        self.y_coordinate = coordinates[0]
        self.x_coordinate = coordinates[1]
        self.start = start

    
    def explore(self):
        """ Compile list of adjacent cells. """

        global trailheads_scores
        
        cell_list = compile_adjacent_cells(
            self.grid, self.coordinates, self.start
        )

        if not cell_list:
            pass
        elif self.start == 8:
            if not self.trailhead in trailheads_scores:
                trailheads_scores[self.trailhead] = cell_list
            else:
                trailheads_scores[self.trailhead].extend(cell_list)
        else:
            # Start new 'hikers' on each valid path.
            for cell in cell_list:
                Hiker(
                    self.grid, self.trailhead, cell, (self.start + 1)
                ).explore()


def create_grid(file: str) -> list[list[int]]:
    """ Read in a text file and create a grid (i.e. map) as a list of lists
        of integers. """

    with open(file, 'r') as input_file:
        grid = []
        for line in input_file:
            string_line = line.strip()
            string_list = list(string_line)
            int_list = [int(x) for x in string_list]
            grid.append(int_list)
    
    return grid


def identify_heads(grid: list[list[int]]) -> list[tuple[int, int]]:
    """ Take grid, identify all 'trailheads' ('0'), and combine their
        coordinates as tuples in list. """
    
    trailheads = []
    for row_index, row_content in enumerate(grid):
        for cell_index, cell_content in enumerate(row_content):
            if cell_content == 0:
                y_coordinate = row_index
                x_coordinate = cell_index
                trailheads.append((y_coordinate, x_coordinate))

    return trailheads


@calc_runtime
def solve_puzzle_10(filepath: str, count: str ='heads') -> int:
    """ Create a grid (i.e. map) as a list of lists of integers, identify all 
        cells with '0' (i.e. trailheads), compile all sequences from 0 to 9
        (i.e. full trails) in a dictionary, and calculate the sum of values
        per dictionary entry depending on the count method chosen. """

    global trailheads_scores

    grid = create_grid(filepath)
    trailheads = identify_heads(grid)

    trailheads_scores = {}

    for trailhead in trailheads:
        Hiker(grid, trailhead, trailhead).explore()

    scores = 0
    for value in trailheads_scores.values():
        if count=='heads':
            score = len(set(value))
            scores += score
        elif count=='trails':
            score = len(value)
            scores += score
    
    return scores


def main():
    """ Execute the main functions with the main input. """

    result_1, runtime_1 = solve_puzzle_10(filepath, count='heads')
    print(f"Solution to the first puzzle of day 10: {result_1}\n"
          f"Runtime: {runtime_1} seconds\n")

    result_2, runtime_2 = solve_puzzle_10(filepath, count='trails')
    print(f"Solution to the second puzzle of day 10: {result_2}\n"
          f"Runtime: {runtime_2} seconds\n")


if __name__ == '__main__':
    main()
