# sudoku final project 12/3/2020

# TODO create win response
# my grid
grid = [
    [5, 0, 3, 0, 0, 4],
    [0, 1, 0, 4, 5, 0],
    [4, 0, 5, 2, 0, 0],
    [3, 0, 0, 1, 4, 0],
    [0, 4, 0, 0, 6, 5],
    [0, 3, 4, 0, 2, 0]

]


# prints the name of the game at the top of the gris


def game_name():
    print(" Sudoku game")

# creates the grid structure


def print_grid(display):
    # displays a line every two rows
    for i in range(len(display)):
        if i % 2 == 0 and i != 0:
            print("- - - - - - - -")
        # displays a line every three columns
        for j in range(len(display[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 5:
                print(display[i][j])
            else:
                print(str(display[i][j]) + " ", end="")


print_grid(grid)












