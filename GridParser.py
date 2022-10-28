import numpy as np

class Parser:
    def parse(self):
        file = open(self.path, "r")
        self.dimensions = list(map(int, file.readline().split(" ")))
        self.matrix = []
        for i in range(self.dimensions[0]):
            row = list(file.readline())[:-1:]
            if "A" in row:
                self.start = np.array([i, row.index("A")])
            if "B" in row:
                self.end = np.array([i, row.index("B")])
            self.matrix.append(row)
        self.matrix = np.array(self.matrix)

    def __init__(self, path):
        self.end = None
        self.start = None
        self.dimensions = None
        self.path = path
        self.parse()
