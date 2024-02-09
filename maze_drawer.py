import pygame
from config import *
from maze import Maze


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
                image = self.cell_images[wall_map[neighbours]]
                self.display_surface.blit(image, (x * CELL_SIZE_SCALED + self.maze_offset_x, y * CELL_SIZE_SCALED + self.maze_offset_y))

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
    maze = Maze(20, 20)
    maze.generate_maze()
    drawer = MazeDrawer(maze)
    drawer.draw()
    drawer.run()
