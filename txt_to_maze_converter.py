from tile import Tile
from maze import Maze
import os
from config import *


class TxtToMazeConverter:
    def __init__(self, filename, wall_char="#", path_char=" "):
        self.filename = filename
        self.wall_char = "#"
        if wall_char:
            if len(wall_char) < 1:
                self.wall_char = wall_char
            else:
                Exception("wall_char must have a length of one")
        else:
            raise Exception("You must provide a value for wall_char")
        if wall_char:
            if len(wall_char) < 1:
                self.path_char = wall_char
            else:
                Exception("path_char must have a length of one")
        else:
            raise Exception("You must provide a value for path_char")

        self.path_char = path_char
        self.maze = None
        self.lines = self.read_file()
        if self.lines:
            self.maze_h = len(self.lines)
            self.maze_w = len(self.lines[0])
        else:
            raise Exception("Empty file")

    def read_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                lines = file.readlines()
            for i, line in enumerate(lines):
                line = line.strip("\n")
                lines[i] = line
            return lines
        else:
            raise FileNotFoundError("File not found")

    # (x-1; y-1) (x; y-1) (x+1; y-1)
    # (x-1; y)   (x; y)   (x+1; y)
    # (x-1; y+1) (x; y+1) (x+1; y+1)
    def get_adjacent_chars(self, x, y):
        chars_position = []
        for i in range(3):
            for j in range(3):
                # check if the position correspond to one of the for tiles
                if abs(i - 1) + abs(j - 1) == 1:
                    nx = x + i - 1
                    ny = y + j - 1
                    chars_position.append((nx, ny))

        # check if the positions are in the maze
        final_positions = []
        for pos in chars_position:
            x, y = pos
            if 0 <= x < self.maze_w and 0 <= y < self.maze_h:
                final_positions.append((x, y))

        chars = []
        for pos in final_positions:
            x, y = pos
            chars.append((self.lines[y][x], x, y))

        return chars

    def get_path(self, x, y):
        adjacent_chars = self.get_adjacent_chars(x, y)
        path = {NORTH: None, SOUTH: None, EAST: None, WEST: None}
        for char, char_x, char_y in adjacent_chars:
            if char_x == x and char_y == y - 1:
                direction = NORTH
            elif char_x == x and char_y == y + 1:
                direction = SOUTH
            elif char_x == x - 1 and char_y == y:
                direction = WEST
            else:
                direction = EAST

            if char == self.wall_char:
                path[direction] = WALL
            elif char == self.path_char:
                path[direction] = PATH
            else:
                raise Exception(f"Unknown char: '{char}' at position: x={char_x};y={char_y}\n values currently used :"
                                f"wall: '{self.wall_char}'; path: '{self.path_char}'"
                                f"\n if you wanna use this char : '{char}'"
                                f"you must change one of the two following args : 'wall_char' or 'path_char'")

        return path

    def convert_txt_to_tiles(self):
        tiles = []
        for y, line in enumerate(self.lines):
            print(y, line)
            row = []
            for x, char in enumerate(line):
                if char == self.path_char:
                    path = self.get_path(x, y)
                else:
                    path = {NORTH: WALL, SOUTH: WALL, EAST: WALL, WEST: WALL}
                row.append(Tile(x, y, path))
            tiles.append(row[1:-1])

        return tiles[1:-1]

    def convert_txt_to_maze(self):
        tiles = self.convert_txt_to_tiles()
        maze = Maze(self.maze_w - 2, self.maze_h - 2, tiles)

        return maze
