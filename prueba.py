arbol = list(" " + input())

def esHoja(i):
    try:
        if arbol[i*2] != "#":
            return False
        else:
            return True
    except IndexError:
        return True

def inorden(i):
    if i >= len(arbol):
        return ""
    if arbol[i] == "#":
        return ""
    if esHoja(i):
        return inorden(2 * i) + arbol[i] + inorden(2 * i + 1)
    return "(" + inorden(2*i) + arbol[i] + inorden(2*i+1) + ")"

print(inorden(1))