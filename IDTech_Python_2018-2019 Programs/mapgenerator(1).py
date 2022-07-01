import numpy as np
import heapq
from enum import Enum


class TileType(Enum):
    EMPTY = -1
    GROUND = 0
    WALL = 1
    START = 2
    ENEMY = 3

def is_in_bounds(pos, grid):
    # Is index inside the grid, is the tile ground, and is there anyone standing there already?
    return 0 <= pos[0] < grid.shape[1] and 0 <= pos[1] < grid.shape[0]\

def is_valid_move(pos, move, grid):
    return move == (0,0) or is_in_bounds((pos[0] + move[0], pos[1] + move[1]), grid)


# Neighbors of a tile
NEIGHBORS = [(0, -1), (-1, 0), (0, 0), (1, 0), (0, 1)]


def get_neighbors(pos, grid):
    x, y = pos
    return [(x + direction[0], y + direction[1]) for direction in NEIGHBORS if is_valid_move(pos, direction, grid)]


def dist(a, b):
    # easy distance for two tuples so we don't have to type this so much.
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

# Priority Queue class, needed for A*
class PriorityQueue:

    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def find_path(pos, goal, grid):

    search_queue = PriorityQueue()
    search_queue.put(pos, 0)
    node_paths = {pos: None}
    node_costs = {pos: 0}

    # We'll use the closest we managed to get if no path exists.
    closest_distance = dist(pos, goal)
    closest_point = pos

    while not search_queue.empty():
        current_pos = search_queue.get()

        if current_pos == goal:
            # we did it
            break
        neighbors = get_neighbors(current_pos, grid)
        for position in neighbors:
            position_cost = node_costs[current_pos] + 1
            # Every position costs 1 to move to.
            if position not in node_costs or position_cost < node_costs[position]:
                node_costs[position] = position_cost
                distance_score = dist(position, goal)
                if distance_score < closest_distance:
                    closest_distance = distance_score
                    closest_point = position
                position_priority = position_cost + distance_score
                search_queue.put(position, position_priority)
                node_paths[position] = current_pos

    # Start path from the closest point found.
    next_move = closest_point

    path_points = [next_move]
    while node_paths[next_move] is not None and node_paths[next_move] != pos:
        next_move = node_paths[next_move]
        path_points.append(next_move)

    return path_points

TILE_TYPE_DICT = {
    TileType.EMPTY: " ",
    TileType.GROUND: " - ",
    TileType.WALL: " # ",
    TileType.START: " S ",
    TileType.ENEMY: " E ",
}

def print_map(grid, player):
    map_str = ""
    map_height, map_width = grid.shape


    for row in range(map_height):
        for col in range(map_width):
            tile = TileType(grid[row, col])
            map_str += TILE_TYPE_DICT[tile]
        map_str += "\n"
    return map_str

class Room:
    def __init__(self,pos,size):
        self.pos = pos
        self.size = size
    def center(self):
        x,y = self.pos
        width, height = self.size
        return x+width // 2, y + height // 2

    def set_tiles(self,grid):
        x,y = self.pos
        width, height = self.size
        room_chunk = grid[y:y+height, x:x+width]
        room_chunk[1:height-1, 1:width-1] = TileType.GROUND.value

        set_slice_walls(room_chunk[0:height,0])
        set_slice_walls(room_chunk[0:height, width-1])
        set_slice_walls(room_chunk[0,1:width-1])
        set_slice_walls(room_chunk[height-1, 1:width-1])

def set_slice_walls(self, slice):
    for index in np.index(slice.shape):
        if slice[index] != TileType.GROUND.value:
            slice[index] = TileType.WALL
