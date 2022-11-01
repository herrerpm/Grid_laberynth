import pygame
import time
from GridParser import Parser
from main import *
raiz = Node(parser.start)
traverse(raiz)
recorrer(raiz)
# print(sol(raiz))
print(solc)

class Square:
    """The square class creates a square on the pygame screen
    with the coordinates provided for its top left corner"""

    def __init__(self, screen, x, y, length, color):
        self.screen = screen
        self.color = color
        self.length = length
        self.x = x
        self.y = y

    def create(self):
        """The create method displays the square object to the screen
        after it is initialized"""
        self.rect = pygame.Rect(self.x, self.y, self.length, self.length)
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
        for y, i in enumerate(self.matrix):
            for x, j in enumerate(i):
                Square(self.screen, x*30, y*30, 30, self.colors[j]).create()

def run():
    """The run function creates a functional pygame app"""
    pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("C:\Windows\Fonts\Arial", 24)
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Juego")
    # cuadrado = Square(screen, 0,0,30, (0,0,255))
    parser = Parser("laberinto_3.in")
    grid = Grid(parser.matrix, screen)
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
        for i in plista:
            x, y = i
            grid.matrix[x][y] = "2"
            grid.draw()
            time.sleep(0.1)
            pygame.display.flip()
        # for i in solc:
        #     x, y = i.data
        #     grid.matrix[x][y] = "3"
        #     grid.draw()
        #     time.sleep(0.1)
        #     pygame.display.flip()

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