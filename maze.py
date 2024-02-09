from tile import Tile
from random import choice, randint
from time import time


class Maze:
    def __init__(self, w, h):
        self.w = w
        self.h = h

        self.tiles = [[Tile(x, y) for x in range(w)] for y in range(h)]
        self.maze = []
        self.frontier = []

    def choose_random_starting_tile(self) -> Tile:
        row = choice(self.tiles)
        return choice(row)

    def add_neighbours_to_frontier(self, tile):
        for pos in tile.get_neighbours_position():
            nx, ny = pos
            if 0 <= nx < self.w and 0 <= ny < self.h:
                tile = self.tiles[ny][nx]
                if tile not in self.frontier and tile not in self.maze:
                    self.frontier.append(tile)

    def get_neighbouring_tiles_in_maze(self, tile):
        neighbouring_tiles = []
        for pos in tile.get_neighbours_position():
            nx, ny = pos
            for maze_tile in self.maze:
                if (maze_tile.x, maze_tile.y) == (nx, ny):
                    neighbouring_tiles.append(maze_tile)

        return neighbouring_tiles

    def get_random_neighbouring_tile(self, tile):
        tiles = self.get_neighbouring_tiles_in_maze(tile)
        tile_to_link = choice(tiles)
        return tile_to_link

    def choose_random_tile_from_frontier(self):
        return self.frontier.pop(randint(0, len(self.frontier)-1))

    def generate_maze(self):
        tile = self.choose_random_starting_tile()
        self.maze.append(tile)
        self.add_neighbours_to_frontier(tile)
        while len(self.maze) < self.w*self.h:
            tile = self.choose_random_tile_from_frontier()
            self.maze.append(tile)
            self.add_neighbours_to_frontier(tile)
            tile_to_link = self.get_random_neighbouring_tile(tile)
            tile.add_neighbour(tile_to_link)
            tile_to_link.add_neighbour(tile)


if __name__ == "__main__":
    time0 = time()
    for i in range(1000):
        maze = Maze(100, 100)
        maze.generate_maze()
    print(time()-time0)
