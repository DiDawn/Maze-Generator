from config import *


class Tile:
    def __init__(self, x: int, y: int, neighbours=None):
        self.x = x
        self.y = y
        if neighbours:
            self.neighbours = neighbours
        else:
            self.neighbours = {NORTH: WALL, SOUTH: WALL, EAST: WALL, WEST: WALL}

    def add_neighbour(self, tile):
        nx, ny = tile.x, tile.y
        direction = self.get_direction(nx, ny)
        self.neighbours[direction] = PATH

    def get_direction(self, nx, ny):
        if nx == self.x and ny == self.y - 1:
            return NORTH
        elif nx == self.x and ny == self.y + 1:
            return SOUTH
        elif nx == self.x - 1 and ny == self.y:
            return WEST
        else:
            return EAST

    def where_path(self):
        path = []
        for direction in DIRECTIONS:
            if self.neighbours[direction] == PATH:
                path.append(direction)
        path.sort()

        return tuple(path)

    # (x-1; y-1) (x; y-1) (x+1; y-1)
    # (x-1; y)   (x; y)   (x+1; y)
    # (x-1; y+1) (x; y+1) (x+1; y+1)
    def get_neighbours_position(self):
        neighbours_position = []
        for i in range(3):
            for j in range(3):
                # check if the position correspond to one of the for tiles
                if abs(i-1) + abs(j-1) == 1:
                    nx = self.x + i-1
                    ny = self.y + j-1
                    neighbours_position.append((nx, ny))

        return neighbours_position

    def __repr__(self):
        return f'{self.x, self.y}'