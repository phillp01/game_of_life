import random
import sys
import time
import pygame

from colours import *

def draw_grid():
    for x in range(0, width, cell_size):
        pygame.draw.line(screen, dark_blue, (x, 0), (x, height))
    for y in range(0, height, cell_size):
        pygame.draw.line(screen, dark_blue, (0, y), (width, y))


def get_cells(density=0.2):
    print {(c, r): random.random() < density for c in range(columns) for r in range(rows)}
    return {(c, r): random.random() < density for c in range(columns) for r in range(rows)}


def draw_cells():
    for(x, y) in cells:
        colour = green if cells[x, y] else black
        rectangle = (x * cell_size, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, colour, rectangle)

def get_neighbours((x, y)):
    positions = [(x-1,y-1), (x,y-1), (x+1,y-1), (x+1,y), (x+1, y+1), (x, y+1), (x-1,y+1), (x-1,y)]
    # print positions
    return [cells [r, c] for (r, c) in positions if 0<= r < rows and 0 <= c < columns]
    # print [cells[r, c] for (r, c) in positions if 0 <= r < rows and 0 <= c < columns]

def evolve():
    cells2 = cells.copy()

    for position, alive in cells.items():
        live_neighbours = sum(get_neighbours(position))
        if alive:
            if live_neighbours < 2:
                cells2[position] = False
            elif live_neighbours > 3:
                cells2[position] = False
        elif live_neighbours == 3:
            cells2[position] = True

    cells.clear()
    cells.update(cells2)

pygame.init()

columns, rows = 100, 100
cells = get_cells(0.1)

# cells = {(0,0):False,(0,1):False,(0,2):False,(0,3):False,(0,4):False,(1,0):False,(1,1):False,(1,2):False,(1,3):False,(1,4):False,(3,0):False,(3,1):False,(3,2):False,(3,3):False,(3,4):False,(4,0):False,(4,1):False,(4,2):False,(4,3):False,(4,4):False,(2,0):False,(2,1):True,(2,2):True,(2,3):True,(2,4):False}
live_neighbours = sum(get_neighbours((1,2)))
print live_neighbours

cell_size = 10
size = width, height = columns * cell_size, rows * cell_size
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

while True:
    clock.tick(500)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    draw_cells()
    evolve()
    draw_grid()
    pygame.display.update()