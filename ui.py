import pygame
import time
from GridParser import Parser
from main import *
# raiz = Node(parser.start)
# traverse(raiz)
# recorrer(raiz)
# # print(sol(raiz))
# print(solc)
from main import Solver

solver = Solver()
print(solver.profundidad)

class Square:
    """The square class creates a square on the pygame screen
    with the coordinates provided for its top left corner"""

    def __init__(self, screen, x, y, width, height, color):
        self.screen = screen
        self.color = color
        self.width = width
        self.heigth =height
        self.x = x
        self.y = y

    def create(self):
        """The create method displays the square object to the screen
        after it is initialized"""
        self.rect = pygame.Rect(self.x, self.y, self.width, self.heigth)
        pygame.draw.rect(self.screen, self.color, self.rect)


class Grid:

    colors = {
        "0": (0,0,0),
        "1": (255,255,255),
        "A": (0,255,0),
        "B": (255,0,0),
        "2": (140,70,158),
        "3": (240, 170, 255)
    }

    def __init__(self, matrix, screen):
        self.matrix = matrix
        self.screen = screen

    def draw(self):
        sizex = 900//(parser.dimensions[0]+1)
        sizey = 600//(parser.dimensions[1]+1)
        for y, i in enumerate(self.matrix):
            for x, j in enumerate(i):
                Square(self.screen, x*sizex, y*sizey, sizex, sizey, self.colors[j]).create()

def run():
    """The run function creates a functional pygame app"""
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("C:\Windows\Fonts\Arial", 24)
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Juego")
    # cuadrado = Square(screen, 0,0,30, (0,0,255))
    parser = Parser("laberinto_4.in")
    parser2 = Parser("laberinto_4.in")
    parser3 = Parser("laberinto_4.in")
    grid = Grid(parser.matrix, screen)
    grid2 = Grid(parser2.matrix, screen)
    grid3 = Grid(parser3.matrix, screen)
    start = time.time()

    def show():
        """The show function handles the pieces that will be displayed
        to the screen and continuously update in the loop method"""
        nonlocal start
        delta = time.time() - start
        start = time.time()
        screen.fill([14, 41, 72])
        grid.draw()
        pygame.display.flip()
        time.sleep(0.1)
        for i in solver.profundidad:
            x, y = i
            grid.matrix[x][y] = "2"
            grid.draw()
            time.sleep(0.1)
            pygame.display.flip()
        screen.fill([14, 41, 72])
        grid2.draw()
        pygame.display.flip()
        for i in solver.amplitud:
            x, y = i
            grid2.matrix[x][y] = "2"
            grid2.draw()
            # time.sleep(0.00001)
            pygame.display.flip()
        screen.fill([14, 41, 72])
        grid3.draw()
        pygame.display.flip()
        for i in solver.respuesta:
            x, y = i.data
            grid3.matrix[x][y] = "2"
            grid3.draw()
            time.sleep(0.1)
            pygame.display.flip()
        time.sleep(100)
        pygame.quit()

    def loop():
        """The loop function ensures the window stays open indefinitely until
        it is closed, it calls the show function to dynamically update its
        contents"""
        run = True
        while run is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    return

            show()
            pygame.display.flip()
            clock.tick()

    loop()

run()