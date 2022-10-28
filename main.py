from GridParser import Parser
from Arbol import Node
import numpy as np

parser = Parser("laberinto_1.in")
# for i in parser.matrix:
#     print(i)
# print(parser.matrix)
# print(parser.end)
# print(parser.start)

moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]

raiz = Node(np.array(parser.start))

start = parser.start

pos = []


# def func(start):
#     if start in pos:
#         return
#     pos.append(start)
#     for i in moves:
#         i, j = start + i
#         try:
#             element = parser.matrix[i][j]
#             if element == "1":
#                 new = np.array([i, j])
#                 raiz.agregar_hijo(Node(new))
#                 func(new)
#         except:
#             pass

def func(nodo):
    for i in pos:
        if np.array_equal(nodo.data, i):
            return
    pos.append(nodo.data)
    for i in moves:
        i, j = nodo.data + i
        if i < 0 or j < 0:
            return
        try:
            element = parser.matrix[i][j]
            if element == "1":
                new = np.array([i, j])
                nodonew = Node(new)
                nodo.agregar_hijo(nodonew)
                nodonew.padre = nodo
                func(nodonew)
            if element == "B":
                print("Su")
        except IndexError:
            pass


def iteracion(raiz):
    if raiz.hijos:
        for i in raiz.hijos:
            iteracion(i)
    print(raiz)
func(raiz)
iteracion(raiz)

print(parser.matrix[-1][-1])