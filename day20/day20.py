import sys
from collections import defaultdict, deque

D = open(sys.argv[1]).read().strip()
lineas = D.split('\n')
grilla = [[c for c in fila] for fila in lineas]
filas = len(grilla)
columnas = len(grilla[0])


def minimo_comun_multiplo(lista):
    resultado = 1
    for numero in lista:
        resultado = (resultado * numero)
    return resultado


tipos = {}

reglas = {}
for linea in lineas:
    fuente, destino = linea.split('->')
    fuente = fuente.strip()
    destino = destino.strip()
    destino = destino.split(', ')
    reglas[fuente] = destino
    tipos[fuente[1:]] = fuente[0]


def ajustar_tipo(y):
    if y in tipos:
        return tipos[y] + y
    else:
        return y


provenientes = {}
invertida = defaultdict(list)
for x, ys in reglas.items():
    reglas[x] = [ajustar_tipo(y) for y in ys]
    for y in reglas[x]:
        if y[0] == '&':
            if y not in provenientes:
                provenientes[y] = {}
            provenientes[y][x] = 'lo'
        invertida[y].append(x)

assert len(invertida['rx']) == 1
assert invertida['rx'][0][0] == '&'
observar = invertida[invertida['rx'][0]]

lo = 0
hi = 0
cola = deque()
encendidos = set()
anterior = {}
cuenta = defaultdict(int)
a_mcm = []
for t in range(1, 10**8):
    cola.append(('broadcaster', 'button', 'lo'))

    while cola:
        x, desde_, tipo = cola.popleft()

        if tipo == 'lo':
            if x in anterior and cuenta[x] == 2 and x in observar:
                a_mcm.append(t - anterior[x])
            anterior[x] = t
            cuenta[x] += 1
        if len(a_mcm) == len(observar):
            print(minimo_comun_multiplo(a_mcm))
            sys.exit(0)

        if x == 'rx' and tipo == 'lo':
            print(t + 1)

        if tipo == 'lo':
            lo += 1
        else:
            hi += 1

        if x not in reglas:
            continue
        if x == 'broadcaster':
            for y in reglas[x]:
                cola.append((y, x, tipo))
        elif x[0] == '%':
            if tipo == 'hi':
                continue
            else:
                if x not in encendidos:
                    encendidos.add(x)
                    nuevo_tipo = 'hi'
                else:
                    encendidos.discard(x)
                    nuevo_tipo = 'lo'
                for y in reglas[x]:
                    cola.append((y, x, nuevo_tipo))
        elif x[0] == '&':
            provenientes[x][desde_] = tipo
            nuevo_tipo = ('lo' if all(
                y == 'hi' for y in provenientes[x].values()) else 'hi')
            for y in reglas[x]:
                cola.append((y, x, nuevo_tipo))
        else:
            assert False, x
    if t == 1000:
        print(lo * hi)
