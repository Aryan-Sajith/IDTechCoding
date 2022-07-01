import heapq
from enum import Enum

import numpy as np
import pygame
import sys

pygame.init()

size = width, height = 640, 480

screen = pygame.display.set_mode(size)


class TileType(Enum):
    EMPTY = -1
    GROUND = 0
    WALL = 1


TILE_TYPE_DICT = {
    TileType.EMPTY: " ",
    TileType.GROUND: "-SE",
    TileType.WALL: "#"
}

TILE_COLOR_DICT = {
    TileType.EMPTY: (10, 10, 10),
    TileType.GROUND: (42, 86, 98),
    TileType.WALL: (7, 44, 54)
}

# Added code

PLAYER_COLOR = (48, 117, 69)
NPC_COLOR = (158, 77, 64)

class PriorityQueue:
    def __init__(self):
        self.elements = []
    def empty(self):
        return len(self.elements) == 0
    def put(self, item, priority):
        heapq.heappush(self.elements,(priority,item))
    def get(self):
        return heapq.heappop(self.elements)[1]


# TODO: Create classes, functions, and variables for pathfinding



def is_position_empty(pos, grid, occupied_spaces=None):
    return 0 <= pos[0] < grid.shape[1] and 0 <= pos[1] < grid.shape[0] \
           and grid[pos[1], pos[0]] == TileType.GROUND.value \
           and (occupied_spaces is None or pos not in occupied_spaces)


def is_valid_move(pos, move, grid, occupied_spaces=0):
    return move == (0, 0) or is_position_empty((pos[0] + move[0], pos[1] + move[1]), grid, occupied_spaces)


NEIGHBOURS = [(-1, -1), (0, -1), (1, -1),
              (-1, 0), (0, 0), (1, 0), (0, 1), (1, 1)]


def get_neighbors(pos, grid, occupied_spaces=None):
    x, y = pos
    return [(x + direction[0], y + direction[1]) for direction in NEIGHBOURS if
            is_valid_move(pos, direction, grid, occupied_spaces)]


def dist(a, b):
    return np.linalg.norm((a[0] - b[0], a[1] - b[1]))  # Calculating distance between find distance


# Player and NPC classes
class Character:

    def __init__(self, position):
        self.pos = position
        self.goal = None
        self.path_points = []

    # each turn, a character will pathfind towards its goal. The player's goals will be set by user input, NPCs will
    # have a function that decides the AI's goal.
    def turn(self, grid, occupied_spaces=None):
        if self.goal is not None:
            # TODO: If character has a goal, find path from position to goal, then move to the next point in the path.
            closest_neighbour = min(get_neighbors(self.pos, grid, occupied_spaces), key=lambda p:
            dist(p, self.goal))
            self.pos = closest_neighbour
        if self.pos == self.goal:
            # goal reached, reset goal to None.
            self.goal = None
        # Once turn is taken, check if goal was reached.


class Npc(Character):

    def __init__(self, position):
        super().__init__(position)
        # TODO: Add variables for tracking and changing AI states.

    #  Set the goals of the NPC's AI
    def set_goals(self, grid, target=None, occupied_spaces=None):
        # TODO: Write code to choose AI states
        self.goal = target


def load_map(filename):
    map_height, map_width = 10, 10

    # Default character position, we'll update while loading the map
    player = Character((1, 1))

    # list of npcs
    npcs = []

    try:
        file = open(filename)
        lines = [line.rstrip() for line in file.readlines()]

        print("File opened")

        # If the file doesn't have any lines it's not a valid map_grid.
        assert len(lines) > 0

        # Updating map_width and map_height based on what we read from the file.
        map_width = max([len(line) for line in lines])
        map_height = len(lines)

        map_grid = np.full((map_height, map_width), TileType.EMPTY.value)

        player_start_found = False

        for row, line in enumerate(lines):
            for col, char in enumerate(line):
                # Add if statements to check for player start and enemy positions.
                if not player_start_found and char == "S":
                    # Move player position
                    player.pos = (col, row)
                    player_start_found = True
                if char == "E":
                    new_npc = Npc((col, row))
                    npcs.append(new_npc)
                for type in TileType:
                    if char in TILE_TYPE_DICT[type]:
                        map_grid[row, col] = type.value
                        break

        print("Valid")
        # update return value to return player and npc list
        return map_grid, player, npcs

    except (OSError, AssertionError):
        print("Map file not found or invalid, using default grid.")
        # update return value to return player and npc list
        npcs.append(Npc((8, 8)))
        return np.full((map_height, map_width), TileType.GROUND.value), player, npcs


# Pixel size of a tile, used for tile/pixel conversions
tile_size = 16


def tile_position(pixel):
    tile_x, tile_y = pixel
    tile_x //= tile_size
    tile_y //= tile_size
    return tile_x, tile_y


def pixel_position(tile, center=False):
    pixel_x, pixel_y = tile
    pixel_x *= tile_size
    pixel_y *= tile_size
    if center:
        pixel_x += tile_size // 2
        pixel_y += tile_size // 2
    return pixel_x, pixel_y


def tile_rect(tile):
    pixel_pos = pixel_position(tile)
    return pygame.Rect(pixel_pos, (tile_size, tile_size))


##
# Test Map
# #################
# #------------#--#
# #--#######---#--########
# #--#-----#---#---------#
# #--#--S--#-E-#--#--##--###
# #--#-----#---#--#--#E--#E#
# ######-#######--#--##--###
# #----------------------#
# ########################
##

# Set up game variables


# Update map loading to get player and npc lists
loaded_map, player, npcs = load_map("./one-room.txt")

map_height, map_width = loaded_map.shape

clock = pygame.time.Clock()

# How many milliseconds between turns. Larger numbers will slow down the turn speed so it's easier to see movement.
turn_milliseconds = 500
# counter to track how long since last turn.
turn_timer = 0

# Game loop
while True:

    # Increase turn timer with number of milliseconds since last frame.
    turn_timer += clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # TODO: Set player goals with user input.
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.goal = tile_position(event.pos)
            print(player.goal)

        for npc in npcs:
            npc.set_goals(loaded_map, player.pos)

    # If the player has a goal (which means they want to take a turn) and turn timer is high enough, take a turn
    if turn_timer >= turn_milliseconds and player.goal is not None:
        turn_timer = 0

        # Debug print to test turn speed. Delete once you've got actual code here!
        print("Turn taken")
        # TODO: add code to take npc and player turns.
        player.turn(loaded_map, occupied_spaces=[npc.pos for npc in npcs] + [player.pos])

        for npc in npcs:
            npc.turn(loaded_map, occupied_spaces=[npc.pos for npc in npcs] + [player.pos])

    screen.fill((0, 0, 0))
    for row, col in np.ndindex(loaded_map.shape):
        color = TILE_COLOR_DICT[TileType(loaded_map[row, col])]
        rect = tile_rect((col, row))
        screen.fill(color, rect=rect)

    # Draw player on screen
    screen.fill(PLAYER_COLOR, rect=tile_rect(player.pos))
    # TODO: Draw lines for player pathfinding paths.

    # Draw each npc on screen
    for npc in npcs:
        screen.fill(NPC_COLOR, rect=tile_rect(npc.pos))
        # TODO: Draw lines for npc pathfinding paths.

    pygame.display.flip()
