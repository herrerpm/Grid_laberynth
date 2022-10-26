from GridParser import Parser

parser = Parser("laberinto_1.in")
for i in parser.matrix:
    print(i)
print(parser.end)
print(parser.start)