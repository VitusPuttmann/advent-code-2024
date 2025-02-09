""" This module contains functions that solve the challenges of day 10
    of the advent of code 2024 (https://adventofcode.com/).
"""

import os

""" Prepare filepath for reading in input. """
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir))
filepath = os.path.join(parent_dir, "data", "day_10_input.txt")


trailheads_scores = {}


def compile_adjacent_cells(
    map: list[list[int]], coordinates: tuple, start: int
):
    max_y_index = len(map) - 1
    max_x_index = len(map[0]) - 1
    y_coordinate = coordinates[0]
    x_coordinate = coordinates[1]
    next = start + 1

    cell_list = []
    
    if y_coordinate - 1 >= 0:
        if map[y_coordinate - 1][x_coordinate] == next:
            cell_list.append((y_coordinate - 1, x_coordinate))
    if x_coordinate + 1 <= max_x_index:
        if map[y_coordinate][x_coordinate + 1] == next:
            cell_list.append((y_coordinate, x_coordinate + 1))
    if y_coordinate + 1 <= max_y_index:
        if map[y_coordinate + 1][x_coordinate] == next:
            cell_list.append((y_coordinate + 1, x_coordinate))
    if x_coordinate - 1 >= 0:
        if map[y_coordinate][x_coordinate - 1] == next:
            cell_list.append((y_coordinate, x_coordinate - 1))
    
    return cell_list


class Hiker():
    """ Object to 'explore maps' by moving along 'coordinates'. """

    def __init__(self,
        map: list[list[int]],
        trailhead: tuple,
        coordinates: tuple,
        start: int = 0
    ):
        self.map = map
        self.trailhead = trailhead
        self.coordinates = coordinates
        self.y_coordinate = coordinates[0]
        self.x_coordinate = coordinates[1]
        self.start = start

    
    def explore(self):
        """ Compile list of adjacent cells. """

        global trailheads_scores
        
        cell_list = compile_adjacent_cells(
            self.map, self.coordinates, self.start
        )

        if not cell_list:
            pass
        elif self.start == 8:
            if not self.trailhead in trailheads_scores:
                trailheads_scores[self.trailhead] = cell_list
            else:
                trailheads_scores[self.trailhead].extend(cell_list)
        else:
            """ Start new 'hikers' on each valid path. """
            
            for cell in cell_list:
                Hiker(
                    self.map, self.trailhead, cell, (self.start + 1)
                ).explore()


def create_map(file: str):
    """ Read in text file and create 'map' as list of list of strings. """

    with open(file, 'r') as input_file:
        map = []
        for line in input_file:
            string_line = line.strip()
            string_list = list(string_line)
            int_list = [int(x) for x in string_list]
            map.append(int_list)
    
    return map


def identify_heads(map: list[list[int]]):
    """ Take map, identify all 'trailheads' ('0'), and combine their
        coordinates as tuples in list. """
    
    trailheads = []
    for row_index, row_content in enumerate(map):
        for cell_index, cell_content in enumerate(row_content):
            if cell_content == 0:
                y_coordinate = row_index
                x_coordinate = cell_index
                trailheads.append((y_coordinate, x_coordinate))

    return trailheads


def solve_puzzle_10(filepath: str, count: str ='heads'):
    """ Create 'map' as list of lists of integers, identify 'trailheads' (= 0),
        compile 'full trails' in dictionary, and calculate sum of values
        per dictionary entry depending on the count method chosen. """

    global trailheads_scores

    map = create_map(filepath)
    trailheads = identify_heads(map)

    trailheads_scores = {}

    for trailhead in trailheads:
        Hiker(map, trailhead, trailhead).explore()

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

    result_1 = solve_puzzle_10(filepath, count='heads')
    print(f"Solution of the first puzzle of day 10: {result_1}.")

    result_2 = solve_puzzle_10(filepath, count='trails')
    print(f"Solution of the second puzzle of day 10: {result_2}.")


if __name__ == '__main__':
    main()
