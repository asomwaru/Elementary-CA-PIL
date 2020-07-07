import time
import numpy as np
from PIL import Image, ImageDraw

ROWS, COLS = [60, 60]
SIZE = 10
WINDOW_SIZE = [ROWS*SIZE, COLS*SIZE]
IMAGES = []

RULES = [0,1,0,1,1,0,1,0][::-1]

def check_rules(curr_arr:list) -> list:
    new_arr = [0 for _ in range(len(curr_arr))]

    for x in range(len(curr_arr)):
        left = (x - 1) % (len(curr_arr))
        center = x
        right = (x + 1) % (len(curr_arr))

        bits = [curr_arr[left], curr_arr[center], curr_arr[right]]
        index = int("".join([str(y) for y in bits]), 2)

        new_arr[x] = RULES[index]

    return new_arr

# Print board
def display_board(arr:list):
    for x in arr:
        print(" ".join(['#' if y == 1 else '.' for y in x]))

# Create image of triangle
def to_image(automata:list, save:bool = True):
    black = (0, 0, 0)
    white = (255, 255, 255)

    im = Image.new('RGB', WINDOW_SIZE, (255, 255, 255))
    draw = ImageDraw.Draw(im)
    start = 0

    for y in range(len(automata)):
        for x in range(len(automata[y])):
            if automata[y][x]:
                draw.rectangle([(x*SIZE, y*SIZE), ((x+1)*SIZE, (y+1)*SIZE)], fill=black)
            else:
                draw.rectangle([(x*SIZE, y*SIZE), ((x+1)*SIZE, (y+1)*SIZE)], fill=white)
    
    if not save:
        return im
    else:
        im.save('picture.png')

# Generate triangle and create a picture
def generate_pic():
    triangle = [[0]*COLS]
    triangle[0][int(COLS/2)] = 1

    for x in range(ROWS):
        current = check_rules(triangle[x])
        triangle.append(current)
    
    to_image(triangle)

# Generate triangle and create an image of each iteration for gif
def generate_gif():
    triangle = [[0]*COLS]
    triangle[0][int(COLS/2)] = 1

    IMAGES.append(to_image(triangle, save=False))
    for x in range(ROWS):
        current = check_rules(triangle[x])
        triangle.append(current)

        IMAGES.append(to_image(triangle, save=False))
    
    IMAGES[0].save('build.gif',
               save_all=True, append_images=IMAGES[1:], optimize=False, duration=40, loop=0)

def main():
    # Initialize the triangle
    triangle = [[0]*COLS]
    triangle[0][int(COLS/2)] = 1

    # Generate the triangle
    for x in range(ROWS):
        current = check_rules(triangle[x])
        triangle.append(current)
    
    # display triangle
    display_board(triangle)
    

if __name__ == '__main__':
    main()
