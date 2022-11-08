from GridParser import Parser
from Arbol import Node
from collections import deque
from threading import stack_size
import sys
sys.setrecursionlimit(10**6)
stack_size(32768)

parser = Parser("laberinto_3.in")

def arrsum(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        arr.append(arr1[i] + arr2[i])
    return arr

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
        self.Solucionn(self.solucion)


    def traverse(self, node):
        posibilities = (
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0)
        )
        if node.data in self.cache:
            return
        self.cache.append(node.data)
        for posibility in posibilities:
            x, y = arrsum(node.data, posibility)
            if 0 <= x <= parser.dimensions[0] and 0 <= y <= parser.dimensions[0]:
                if parser.matrix[x][y] == "1":
                    nnode = Node([x, y])
                    node.agregar_hijo(nnode)
                    nnode.padre = node
                    self.traverse(nnode)
                if parser.matrix[x][y] == "B":
                    nnode = Node([x, y])
                    node.agregar_hijo(nnode)
                    nnode.padre = node
                    self.solucion = nnode

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