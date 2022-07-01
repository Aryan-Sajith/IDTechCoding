import pygame, sys, os

from enum import Enum

import numpy as np

# Set up pygame screen

pygame.init()

size = width, height = 640, 480

screen = pygame.display.set_mode(size)


# Enumeration for different tile types in the map. We'll use this instead of raw numbers like we did in the last lesson.

# This makes it easier to add new tile types later if we want without changing code!

class TileType(Enum):
    EMPTY = -1

    GROUND = 0

    WALL = 1


# Dict of what characters can represent each tile type, will be used when we load the map from a file.

TILE_TYPE_DICT = {

    TileType.EMPTY: " ",

    TileType.GROUND: "-SE",

    TileType.WALL: "#"

}

# Sets of RGB values. These will control what color each tile is when drawn to the screen.

TILE_COLOR_DICT = {

    TileType.EMPTY: (10, 10, 10),

    TileType.GROUND: (42, 86, 98),

    TileType.WALL: (7, 44, 54)

}


def load_map(filename):
    # TODO: Build a function that creates a grid map. Learn about triblock and empty map file error
    map_height = 10
    map_width = 10

    try:
        file = open(filename)
        lines = [line.rstrip() for line in
                 file.readlines()]  # removes end backslash n at end of text files of python read function in text.
        assert len(lines) > 0  # We have lines in a file, raise an assertion error
        map_width = max([len(line) for line in
                         lines])  # this list comprehension takes lenght of lines as argument and returns its maximum value
        map_height = len(lines)
        map_grid = np.full((map_height, map_width), TileType.EMPTY.value)

        '''The next few lines go through each line'''

        for row, line in enumerate(lines):  # Enumerate not only goes through lines but also gives index
            for col, char in enumerate(line):
                for type in TileType:
                    if char in TILE_TYPE_DICT[type]:
                        map_grid[row, col] = type.value
                        break  # we want to stop if we found the correct tile type

        return map_grid
    except (OSError, AssertionError):
        print("Map file not found(OSM) or invalid(Assertion), using regular grid ")
        return np.full((map_height, map_width), TileType.GROUND.Value)

    return grid


# Functions to make our lives drawing tiles easier.


# the width and height of a square tile in pixels.

tile_size = 16


# take a pixel postion (x,y) and convert it to a grid (x, y) we can use as an index in the grid map

def tile_position(pixel):
    tile_x, tile_y = pixel

    tile_x //= tile_size

    tile_y //= tile_size

    return tile_x, tile_y


# take a grid index (x, y) and return the pixel position. By default, returns the top left pixel position of the tile.

# if center=True, returns the center pixel position of the tile instead.

def pixel_position(tile, center=False):
    pixel_x, pixel_y = tile

    pixel_x *= tile_size

    pixel_y *= tile_size

    if center:
        pixel_x += tile_size // 2

        pixel_y += tile_size // 2

    return pixel_x, pixel_y


# gets a pygame Rect for a given tile (x, y) index for easy drawing

def tile_rect(tile):
    pixel_pos = pixel_position(tile)

    return pygame.Rect(pixel_pos, (tile_size, tile_size))


##

# Test Map - Copy this into a text file to test the loading once completed

#################

# ------------#--#

# --#######---#--########

# --#-----#---#---------#

# --#--S--#-E-#--#--##--###

# --#-----#---#--#--#E--#E#

######-#######--#--##--###

# ----------------------#

########################

##


# TODO: Set up game variables, load the map


loaded_map = load_map("one-room.txt")
map_height, map_width = loaded_map.shape

clock = pygame.time.Clock()

# Game loop

while True:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    # TODO: Draw the map to the screen.
    for row, col in np.ndindex(loaded_map.shape):
        color = TILE_COLOR_DICT[TileType(loaded_map[
                                             row, col])]  # Inner most: loaded map is 2-d array of numbers and has rows and columns, then pass that value to our tile type as an abstract idea, then pass that tile type to tile dictionary to assign colors for tiles.
        rect = tile_rect((col, row))  # Based on x and y coordinate, so flipped row and col
        screen.fill(color, rect=rect)
    pygame.display.flip()
