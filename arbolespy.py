positions = [None]*20
positions[1] = 31
positions[2] = 20
positions[3] = 42
positions[4] = 7
positions[5] = 25
positions[11] = 28
positions[6] = 36
positions[7] = 50
positions[3] = 42

print(positions)


def agregar(lista, valor):
    pos = 1
    while(True):
        try:
            nodo1 = lista[pos]
            if valor < nodo1:
                pos *= 2
            elif valor > nodo1:
                pos = (pos*2)+1
        except TypeError:
            positions[pos] = valor
            break
    print(f"Se agrego {valor} en la posicion {pos}")

def busquedaAmplitud(lista):
    for i in lista:
        if i:
            print(i)

def busquedaProfundidad(lista, pos=1):
    if positions[pos]:
        print(positions[pos])
    try:
        busquedaProfundidad(lista, pos*2)
        busquedaProfundidad(lista, (pos*2)+1)
    except IndexError:
        return

# agregar(positions, 6)
# busquedaAmplitud(positions)
busquedaProfundidad(positions)
