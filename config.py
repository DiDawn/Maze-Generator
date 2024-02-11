NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3
DIRECTIONS = (NORTH, SOUTH, EAST, WEST)

WALL = 0
PATH = 1

MAZE_SIZE = 15, 15

WINDOW_WIDTH = 1920//1.1
WINDOW_HEIGHT = 1080//1.1
CELL_SIZE = 96       # cell width/height in pixels in tile sheet
SCALE_FACTOR = 1
CELL_SIZE_SCALED = CELL_SIZE * SCALE_FACTOR

PathNSEW = 0
PathNSW = 1
PathNSE = 2
PathNS = 3
PathNEW = 4
PathNW = 5
PathNE = 6
PathN = 7
PathSEW = 8
PathSW = 9
PathSE = 10
PathS = 11
PathEW = 12
PathW = 13
PathE = 14
WallNSEW = 16
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
    (): WallNSEW
}
