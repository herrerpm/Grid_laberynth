class Node:
    def __init__(self, data):
        self.padre = None
        self.hijos = []
        self.data = data

    def agregar_hijo(self, nodo):
        self.hijos.append(nodo)

    def __repr__(self):
        return str(self.data)