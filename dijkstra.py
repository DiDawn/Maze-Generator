from custom_queue import Queue


class DijkstraSolver:
    def __init__(self, maze, start, end):
        self.maze = maze
        self.start = start
        print(start)
        self.end = end
        print(end)

        self.graph = self.convert_maze_to_graph()
        self.distances = {node: float('inf') for node in self.graph}
        self.distances[start] = 0

        self.shortest_path = {node: [] for node in self.graph}

        self.queue = Queue([(0, start)])

    @staticmethod
    def get_neighbouring_tiles_with_path(tile):
        tiles = []
        tile_neighbours = maze.get_neighbouring_tiles(tile)
        tile_path = tile.where_path()
        for tile_n in tile_neighbours:
            if tile.get_direction(tile_n.x, tile_n.y) in tile_path:
                if tile.x == 4 and tile.y == 5:
                    print("oho")
                tiles.append(tile_n)
        if tile.x == 4 and tile.y == 5:
            print(tile_neighbours, tile_path)
        return tiles

    def convert_maze_to_graph(self):
        graph = {}
        for tile in self.maze.maze:
            neighbouring_tiles = self.get_neighbouring_tiles_with_path(tile)
            if neighbouring_tiles:
                graph[tile] = neighbouring_tiles

        return graph

    def solve(self):
        while self.queue:
            current_distance, current_node = self.queue.head_pop()

            if current_node == self.end:
                break

            if current_distance > self.distances[current_node]:
                continue

            for neighbor in self.graph[current_node]:
                distance = current_distance + 1

                if distance < self.distances[neighbor]:
                    self.distances[neighbor] = distance
                    self.shortest_path[neighbor] = self.shortest_path[current_node] + [current_node]
                    self.queue.head_push((distance, neighbor))

        return self.distances[self.end], self.shortest_path[self.end] + [self.end]

    @staticmethod
    def convert_solution_to_vectors(solution):
        path = []
        for i, tile in enumerate(solution[:-1]):
            next_tile = solution[i+1]
            path.append((next_tile.x - tile.x, next_tile.y - tile.y))

        return path


if __name__ == "__main__":
    from maze import Maze
    from txt_to_maze_converter import TxtToMazeConverter
    from time import time
    from maze_drawer import MazeDrawer
    time0 = time()
    converter = TxtToMazeConverter("maze.txt", wall_char="*")
    maze = converter.convert_txt_to_maze()
    # maze = Maze(10, 10)
    # maze.generate_maze()
    print(f"Generating maze took: {time() - time0} s")
    time0 = time()
    start, end = maze.maze[0], maze.maze[-1]
    solver = DijkstraSolver(maze, start, end)
    distance, path = solver.solve()
    print(f"Solving took: {time() - time0} s")
    print(distance, path)
    print(solver.convert_solution_to_vectors(path))
    print(f"start pos: {(start.x, start.y), start.neighbours} | end pos: {(end.x, end.y)}")
    drawer = MazeDrawer(maze)
    drawer.draw()
    drawer.run()
