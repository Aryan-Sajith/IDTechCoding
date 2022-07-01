import numpy as np
import random

map_height = 10  # Sets height through rows
map_width = 10  # Sets width through columns

grid = np.full((map_height, map_width), 0)  # Creates a grid with a specified shape, filled with zeroes).

for row in range(map_height):  # Iterates through every row
    for col in range(map_width):  # Iterates through every column
        if row == 0 or row == map_height - 1 or col == 0 or col == map_width - 1:  # Checks if first row or last and if first column or last'''
            grid[row, col] = 1  # Sets to 1 to indicate walls

# 2d array splices
grid[2:4, 2:9:2] = 5  # For rows 2-3, and columns from 2-6 by strides of 2 to 1(array slice).
grid[5:8, 1:9:3] = 1
grid[8:11, 2:9:2] = 1


class Player:  # Creates a class called player.
    def __init__(self):  # Initial constructor for self to assign properties to class.
        self.pos = (1, 1)  # Creates an attribute of the class, starting point for player top left

    def move(self, move_pos, grid):  # Creates a method of the class with grid and move_pos as parameters to pass in.
        new_pos = (self.pos[0] + move_pos[0], self.pos[1] + move_pos[1])
        # /\ creates a new position by taking and combining indexes of move_pos with self.pos)
        if grid[new_pos[1], new_pos[0]] == 0:  # Creates loop to check if landing on space
            self.pos = new_pos  # Then successfully update self.pos
            return True
        elif grid[new_pos[1], new_pos[0]] == 5:  # Creates loop to check if landing on teleporter
            self.pos = (random.randint(0,10), random.randint(0,10))
            return True  # return true because function worked
        return False  # The position is not an empty space and thus failed to update.


def print_map(grid, player):  # Creates a function that takes grid and player as parameters.
    map_str = " "  # Creates a new array with specific functions based on the number as input
    for row in range(map_height):  # Iterates through every row
        for col in range(map_width):  # Iterates through every column
            if (row, col) == player.pos:  # If the coordinate = player. pos from previous class...
                map_str += "P"  # Change to a P to represent the player
            elif grid[row, col] == 5:
                map_str += "?"
            elif grid[row, col] == 0:  # If the value of the row/column in grid is 0...
                map_str += "-"  # Use - to represent empty space
            elif grid[row, col] == 1:  # If the value of the row/column in grid is 1...
                map_str += "#"  # Use # to represent walls
            else:  # Finally to make sure each new row/column is printed seperately...
                map_str += " "  # Then nothing is added to the actual array...
        map_str += "\n"  # But the array is printed with spaces per column/row now.
    print(map_str)  # Finally prints the updated map after the iteration.


p = Player()  # Creates an instance/object of class Player which requires no parameters.

print_map(grid, p)  # Runs the print_map function for the initial grid with the new p object.

move_dict = {  # Creates a new dictionary: Unordered, changeable, and indexed). Created using curly brackets.
    "left": (0, -1),  # An example of a key: "left" and values (0,-1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

while True:  # Runs an infinite loop asking player for input
    move_str = input("Move? (up/down/left/right)")  # Creates a variable that stores user input
    if move_str in move_dict:  # If the user input is part of the dictionary...
        move_pos = move_dict[move_str]  # move_pos from the move method in player class...
        move_success = p.move(move_pos, grid)  # if successful p object is using move function from class.
        if move_success:  # and if the move is successful then have to...
            print_map(grid, p)  # run the print_map function to update with new position
