from pygame.locals import *
import math, pygame, sys

"""
Representing hex grid
 __    __    __
/  \__/  \__/  \    Even [0]
\__/  \__/  \__/    Odd  [1]
/  \__/  \__/  \    Even [2]
\__/  \__/  \__/    Odd  [3]
/  \__/  \__/  \    Even [4]
\__/  \__/  \__/    Odd  [5]
/  \__/  \__/  \    Even [6]
\__/  \__/  \__/    Odd  [7]


Could also be done like:
H H H H H H
 H H P H H
H H H H H H

[0, H, 0, H, 0, H, 0, H, 0, H, 0, H]
[H, 0, H, 0, H, 0, H, 0, H, 0, H, 0]
[0, H, 0, H, 0, P, 0, H, 0, H, 0, H]
[H, 0, H, 0, H, 0, H, 0, H, 0, H, 0]
[0, H, 0, H, 0, H, 0, H, 0, H, 0, H]

above is two rows up
upper left is one up, one left
upper right is one up, one right
lower left is one down, one left
lower right is one down, one right
below is two rows down

wastes a bit of space but makes sense
https://stackoverflow.com/questions/11373122/best-way-to-store-a-triangular-hexagonal-grid-in-python
"""

"""
Drawing hexagons
https://www.redblobgames.com/grids/hexagons/
Points are at angles of 0*, 60*, 120*, 180*, 240*, 300*

size = length of one side
width is 2 * size
height is sqrt(3) * size

horizontal distance between adjacent hexagon centers is width * 3/4
  vertical distance between adjacent hexagon centers is height
"""

water_color = (0, 0, 255)

# class Ship(country, hull, manpower, etc):
#     def __init__():
#         print()

def draw_regular_polygon(surface, color, num_sides, x, y, radius):
    points = []

    for i in range(num_sides):
        x = x + radius * math.cos(math.pi * 2 * i / num_sides)
        y = y + radius * math.sin(math.pi * 2 * i / num_sides)
        points.append([int(x), int(y)])

    pygame.draw.polygon(surface, color, points)

def draw_board(display):
    # sets background to white
    display.fill([255, 255, 255])

    # makes a hexagon
    draw_regular_polygon(display, water_color, 6, 100, 100, 50)

def main():
    pygame.init()
    display = pygame.display.set_mode((400, 300))

    #RGB blue is (0, 0, 255)
    #RGB navy blue is (0, 0, 128)

    pygame.display.set_caption('Hello world!')

    draw_board(display)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__== '__main__':
    main()
