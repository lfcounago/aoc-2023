import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
import heapq
import math


def abrir_archivo(ruta):
    return open(ruta).read().strip()


def dividir_lineas(datos):
    return datos.split('\n')


def generar_matriz(lineas):
    return [[c for c in fila] for fila in lineas]


def obtener_dimensiones(matriz):
    return len(matriz), len(matriz[0])


def encontrar_bloques(lineas):
    bloques = []
    for linea in lineas:
        inicio, fin = linea.split('~')
        sx, sy, sz = [int(x) for x in inicio.split(',')]
        ex, ey, ez = [int(x) for x in fin.split(',')]
        bloque = []
        if sx == ex and sy == ey:
            assert sz <= ez
            for z in range(sz, ez+1):
                bloque.append((sx, sy, z))
        elif sx == ex and sz == ez:
            assert sy <= ey
            for y in range(sy, ey+1):
                bloque.append((sx, y, sz))
        elif sy == ey and sz == ez:
            assert sx <= ex
            for x in range(sx, ex+1):
                bloque.append((x, sy, sz))
        else:
            assert False
        assert len(bloque) >= 1
        bloques.append(bloque)
    return bloques


def encontrar_vistos(bloques):
    vistos = set()
    for bloque in bloques:
        for (x, y, z) in bloque:
            vistos.add((x, y, z))
    return vistos


def mover_bloques(bloques, vistos):
    while True:
        alguno = False
        for i, bloque in enumerate(bloques):
            ok = True
            for (x, y, z) in bloque:
                if z == 1:
                    ok = False
                if (x, y, z-1) in vistos and (x, y, z-1) not in bloque:
                    ok = False
            if ok:
                alguno = True
                for (x, y, z) in bloque:
                    assert (x, y, z) in vistos
                    vistos.discard((x, y, z))
                    vistos.add((x, y, z-1))
                bloques[i] = [(x, y, z-1) for (x, y, z) in bloque]
        if not alguno:
            break
    return bloques, vistos


def calcular_puntos(bloques, vistos):
    vistos_antiguos = deepcopy(vistos)
    bloques_antiguos = deepcopy(bloques)

    p1 = 0
    p2 = 0
    for i, bloque in enumerate(bloques):
        vistos = deepcopy(vistos_antiguos)
        bloques = deepcopy(bloques_antiguos)
        for C in bloques:
            for (x, y, z) in C:
                assert (x, y, z) in vistos

        for (x, y, z) in bloque:
            vistos.discard((x, y, z))

        caida = set()
        while True:
            alguno = False
            for j, C in enumerate(bloques):
                if j == i:
                    continue
                ok = True
                for (x, y, z) in C:
                    if z == 1:
                        ok = False
                    if (x, y, z-1) in vistos and (x, y, z-1) not in C:
                        ok = False
                if ok:
                    caida.add(j)
                    for (x, y, z) in C:
                        assert (x, y, z) in vistos
                        vistos.discard((x, y, z))
                        vistos.add((x, y, z-1))
                    bloques[j] = [(x, y, z-1) for (x, y, z) in C]
                    alguno = True
            if not alguno:
                break
        if len(caida) == 0:
            p1 += 1
        p2 += len(caida)
    return p1, p2


def main(ruta):
    datos = abrir_archivo(ruta)
    lineas = dividir_lineas(datos)
    bloques = encontrar_bloques(lineas)
    vistos = encontrar_vistos(bloques)
    bloques, vistos = mover_bloques(bloques, vistos)
    p1, p2 = calcular_puntos(bloques, vistos)
    print(p1)
    print(p2)


main(sys.argv[1])
