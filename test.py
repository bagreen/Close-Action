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

from pygame.locals import *
import math, random, pygame, sys, time


WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

FPS = 60

SIDE = 50
PADDING = 10

#                    R    G    B
COLOR_BLACK     = (  0,   0,   0)
COLOR_BLUE      = (  0,   0, 255)
COLOR_CYAN      = (  0, 255, 255)
COLOR_GRAY      = (100, 100, 100)
COLOR_GREEN     = (  0, 255,   0)
COLOR_HIGHLIGHT = (255, 255, 255)
COLOR_NAVY_BLUE = (  0,   0, 128)
COLOR_ORANGE    = (255, 165,   0)
COLOR_PURPLE    = (128,   0, 128)
COLOR_RED       = (255,   0,   0)
COLOR_WHITE     = (255, 255, 255)
COLOR_YELLOW    = (255, 255,   0)

# store hexagons as their layout is on the board?
HEXAGONS = []

class Hexagon:
    def __init__(self, center_x, center_y, radius, color, drawing):
        # info about hex
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
        self.color = color
        self.drawing = drawing

        # neighbors
        # instead, calculate the distance between center and other hex's centers
        # and if the distance is correct, they're neighbors?
        # or, store them as hexs are stored and then check out their adjacent?
            # probably most efficent
        self.neighbors = {}
        self.neighbors['upper_left'] = None
        self.neighbors['upper_right'] = None
        self.neighbors['left'] = None
        self.neighbors['right'] = None
        self.neighbors['lower_left'] = None
        self.neighbors['lower_right'] = None



def draw_hex(center_x, center_y, radius, color):
    points = []

    for i in range(6):
        point_x = center_x + SIDE * math.cos(math.pi * 2 * i / 6)
        point_y = center_y + SIDE * math.sin(math.pi * 2 * i / 6)
        points.append([int(point_x), int(point_y)])

    return pygame.draw.polygon(DISPLAY, color, points)

def draw_board():
    global HEXAGONS
    # hex dimensions?
    width = 3 * (SIDE + 5)
    height = (math.sqrt(3) * (SIDE + 5)) / 2

    hexagons_row = 0
    hexagons_col = 0

    for i in range(WINDOW_HEIGHT):
        if height * (i + 2) > WINDOW_HEIGHT:
            break
        elif i % 2 == 1:
            width_padding = 2.5 * (SIDE + 5)
        else:
            width_padding = 1 * (SIDE + 5)
        for j in range(WINDOW_WIDTH):
            if (SIDE + 5) + width_padding + width * j > WINDOW_WIDTH:
                break
            hex_drawing = draw_hex(width_padding + width * j, height * (i + 1), SIDE, COLOR_BLUE)
            new_hex = Hexagon(width_padding + width * j, height * (i + 1), SIDE, COLOR_BLUE, hex_drawing)
            HEXAGONS.append(new_hex)

def get_hex_at_point(x, y):
    for hex in HEXAGONS:
        if hex.drawing.collidepoint(x, y):
            return hex
    return None

def get_neighbors(hex):
    neighbors = []

    # neighbors are +-height, +-height/2 +- side?
    neighbors.append(get_hex_at_point(hex.center_x, hex.center_y))

def highlight_hex(hex_hover):
    draw_hex(hex_hover.center_x, hex_hover.center_y, hex_hover.radius + 2, COLOR_HIGHLIGHT)
    #hex_hover.drawing = draw_hex(hex_hover.center_x, hex_hover.center_y, hex_hover.radius, hex_hover.color)


def main():
    pygame.init()

    fps_clock = pygame.time.Clock()

    global DISPLAY
    DISPLAY = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption('Test!')

    mouse_x = None # stores x component of mouse
    mouse_y = None # stores y compoennt of mouse

    while True:
        mouse_clicked = False

        DISPLAY.fill(COLOR_WHITE) # makes background white
        draw_board()

        for event in pygame.event.get():
            if event.type == QUIT or event.type == K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                #print('X:', mouse_x, 'Y:', mouse_y)
            elif event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                #print('X:', mouse_x, 'Y:', mouse_y)
                mouse_clicked = True

        if mouse_x is not None and mouse_y is not None:
            hex_hover = get_hex_at_point(mouse_x, mouse_y)

            if hex_hover is not None:
                highlight_hex(hex_hover)

        fps_clock.tick(FPS)
        pygame.display.update()
        #time.sleep(10)


if __name__ == '__main__':
    main()
