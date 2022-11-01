from GridParser import Parser
from Arbol import Node

parser = Parser("laberinto_3.in")


def arrsum(arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        arr.append(arr1[i] + arr2[i])
    return arr

solc = []


def sol(nodo):
    while nodo.padre:
        solc.append(nodo)
        nodo = nodo.padre

cache = []
plista = []

def recorrer(nodo):
    plista.append(nodo.data)
    if nodo.hijos:
        for i in nodo.hijos:
            recorrer(i)

def traverse(node):
    posibilities = (
        (0, -1),
        (0, 1),
        (-1, 0),
        (1, 0)
    )
    if node.data in cache:
        return
    cache.append(node.data)
    for posibility in posibilities:
        x, y = arrsum(node.data, posibility)
        if 0 <= x <= parser.dimensions[0] and 0 <= y <= parser.dimensions[0]:

            if parser.matrix[x][y] == "1":
                nnode = Node([x, y])
                node.agregar_hijo(nnode)
                nnode.padre = node
                traverse(nnode)
            if parser.matrix[x][y] == "B":
                nnode = Node([x, y])
                node.agregar_hijo(nnode)
                nnode.padre = node
                sol(nnode)

# raiz = Node(parser.start)
# traverse(raiz)
# recorrer(raiz)