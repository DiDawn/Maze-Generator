import pygame
from config import *
from maze import Maze


WINDOW_WIDTH = 1920//2
WINDOW_HEIGHT = 1080//2
CELL_SIZE = 96       # cell width/height in pixels in tilesheet
SCALE_FACTOR = 0.5
CELL_SIZE_SCALED = CELL_SIZE * SCALE_FACTOR

PathNSEW = 0
PathNSE = 1
PathNSW = 2
PathNS = 3
PathNEW = 4
PathNE = 5
PathNW = 6
PathN = 7
PathSEW = 8
PathSE = 9
PathSW = 10
PathS = 11
PathEW = 12
PathE = 13
PathW = 14
WallNSEW = 15
wall_map = {
    (NORTH, SOUTH, EAST, WEST): PathNSEW,
    (NORTH, EAST, WEST): PathNEW,
    (SOUTH, EAST, WEST): PathSEW,
    (EAST, WEST): PathEW,
    (NORTH, SOUTH, EAST): PathNSE,
    (NORTH, EAST): PathNE,
    (SOUTH, EAST): PathSE,
    (EAST,): PathE,
    (NORTH, SOUTH, WEST): PathNSW,
    (NORTH, WEST): PathNW,
    (SOUTH, WEST): PathSW,
    (WEST,): PathW,
    (NORTH, SOUTH): PathNS,
    (NORTH,): PathN,
    (SOUTH,): PathS,
    (): 15
}


class MazeDrawer:
    def __init__(self, maze):
        self.maze = maze
        pygame.init()
        # open window
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        # load tile sheet, and extract the cell images
        self.tilesheet = pygame.image.load("assets\\MazeTileset.png").convert_alpha()
        self.cell_images = []
        for y in range(4):
            for x in range(4):
                rect = (128 * x, 128 * y, CELL_SIZE, CELL_SIZE)
                image = self.tilesheet.subsurface(rect)
                image = pygame.transform.scale_by(image, (SCALE_FACTOR, SCALE_FACTOR))
                self.cell_images.append(image)

        self.maze_offset_x = (WINDOW_WIDTH - self.maze.w * CELL_SIZE_SCALED) // 2
        self.maze_offset_y = (WINDOW_HEIGHT - self.maze.h * CELL_SIZE_SCALED) // 2

    def draw(self):
        for y in range(self.maze.h):
            for x in range(self.maze.w):
                tile = self.maze.tiles[y][x]
                neighbours = tile.where_path()
                print(x, y, neighbours)
                image = self.cell_images[wall_map[neighbours]]
                self.display_surface.blit(image, (x * CELL_SIZE_SCALED +self.maze_offset_x, y * CELL_SIZE_SCALED + self.maze_offset_y))

        pygame.display.update()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
        quit()


if __name__ == "__main__":
    maze = Maze(10, 10)
    maze.generate_maze()
    drawer = MazeDrawer(maze)
    drawer.draw()
    drawer.run()
