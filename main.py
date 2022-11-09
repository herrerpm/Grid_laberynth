from GridParser import Parser
from Arbol import Node
from collections import deque


def arrsum(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        arr.append(arr1[i] + arr2[i])
    return arr


def posibilities(start, dimensions):
    posibility = (
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0)
    )
    movements = []
    for i in posibility:
        x, y = arrsum(start, i)
        if 0 <= x <= dimensions[0] and 0 <= y <= dimensions[0]:
            movements.append((x, y))
    return movements


class Solver:

    def __init__(self, path):
        self.parser = Parser(path)
        self.solucion = None
        self.raiz = Node(self.parser.start)
        self.cache = []
        self.traverse(self.raiz)
        self.profundidad = []
        self.amplitud = []
        self.respuesta = []
        self.Profundidad(self.raiz)
        self.Amplitud(self.raiz)
        # print(self.solucion)
        self.Solucionn(self.solucion)

    def traverse(self, raiz):
        stack = deque()
        stack.append(raiz)
        while stack:
            print("Calculando")
            node = stack.popleft()
            if node.data not in self.cache:
                self.cache.append(node.data)
                movements = posibilities(node.data, self.parser.dimensions)
                for posibility in movements:
                    x, y = posibility
                    if self.parser.matrix[x][y] == "1" and [x,y] not in self.cache:
                        nuevo_nodo = Node([x, y])
                        node.agregar_hijo(nuevo_nodo)
                        nuevo_nodo.padre = node
                        stack.append(nuevo_nodo)
                    if self.parser.matrix[x][y] == "B" and [x,y] not in self.cache:
                        nuevo_nodo = Node([x, y])
                        node.agregar_hijo(nuevo_nodo)
                        nuevo_nodo.padre = node
                        self.solucion = nuevo_nodo

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