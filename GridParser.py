class Parser:
    def parse(self):
        file = open(self.path, "r")
        self.dimensions = list(map(int, file.readline().split(" ")))
        self.matrix = []
        for i in range(self.dimensions[0]):
            row = list(file.readline())[:-1:]
            if "A" in row:
                self.start = (i, row.index("A"))
            if "B" in row:
                self.end = (i, row.index("B"))
            self.matrix.append(row)

    def __init__(self, path):
        self.end = None
        self.start = None
        self.dimensions = None
        self.path = path
        self.parse()
