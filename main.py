from GridParser import Parser
from Arbol import Node
from collections import deque
from threading import stack_size
import sys
sys.setrecursionlimit(10**6)
parser = Parser("laberinto_4.in")

def arrsum(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        arr.append(arr1[i] + arr2[i])
    return arr

def posibilities(start, dimensions):
    posibilities = (
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0)
    )
    movements = []
    for i in posibilities:
        x,y = arrsum(start, i)
        if 0 <= x <= dimensions[0] and 0 <= y <= dimensions[0]:
            movements.append((x,y))
    return movements


class Solver:

    def __init__(self):
        self.solucion = None
        self.raiz = Node(parser.start)
        self.cache = []
        self.traverse(self.raiz)
        self.profundidad = []
        self.amplitud = []
        self.respuesta = []
        self.Profundidad(self.raiz)
        self.Amplitud(self.raiz)
        # print(self.solucion)
        # self.Solucionn(self.solucion)


    # def traverse(self, node):
    #     posibilities = (
    #         (0, -1),
    #         (0, 1),
    #         (-1, 0),
    #         (1, 0)
    #     )
    #     if node.data in self.cache:
    #         return
    #     self.cache.append(node.data)
    #     for posibility in posibilities:
    #         x, y = arrsum(node.data, posibility)
    #         if 0 <= x <= parser.dimensions[0] and 0 <= y <= parser.dimensions[0]:
    #             if parser.matrix[x][y] == "1":
    #                 nnode = Node([x, y])
    #                 node.agregar_hijo(nnode)
    #                 nnode.padre = node
    #                 self.traverse(nnode)
    #             if parser.matrix[x][y] == "B":
    #                 nnode = Node([x, y])
    #                 node.agregar_hijo(nnode)
    #                 nnode.padre = node
    #                 self.solucion = nnode


    def traverse(self, raiz):
        stack = deque()
        stack.append(raiz)
        while(stack):
            node = stack.popleft()
            if node.data not in self.cache:
                self.cache.append(node.data)
                movements = posibilities(node.data, parser.dimensions)
                print("Nodo",node,movements)
                for posibility in movements:
                    x, y = posibility
                    # print(x,y)
                    if parser.matrix[x][y] == "1":
                        nuevo_nodo = Node([x, y])
                        node.agregar_hijo(nuevo_nodo)
                        nuevo_nodo.padre = node
                        stack.append(nuevo_nodo)
                    if parser.matrix[x][y] == "B":
                        nuevo_nodo = Node([x, y])
                        node.agregar_hijo(nuevo_nodo)
                        nuevo_nodo.padre = node
                        self.solucion = nuevo_nodo
            else:
                print("Etsito")

    def Profundidad(self, nodo):
        self.profundidad.append(nodo.data)
        if nodo.hijos:
            for i in nodo.hijos:
                self.Profundidad(i)

    def Amplitud(self, nodo):
        cola = deque([nodo])
        while cola:
            actual = cola.pop()
            self.amplitud.append(actual.data)
            for hijo in actual.hijos:
                cola.appendleft(hijo)

    def Solucionn(self, nodo):
        while True:
            if nodo.padre:
                self.respuesta.append(nodo)
                nodo = nodo.padre
            else:
                return


solver = Solver()
print(solver.profundidad)
# print(posibilities((3,3), parser.dimensions))