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


def encontrar_inicio(matriz, filas, columnas):
    for fila in range(filas):
        for columna in range(columnas):
            if matriz[fila][columna] == 'S':
                return fila, columna


def encontrar_distancias(sr, sc, filas, columnas, matriz):
    distancias = {}
    cola = deque([(0, 0, sr, sc, 0)])
    while cola:
        tr, tc, r, c, d = cola.popleft()
        if r < 0:
            tr -= 1
            r += filas
        if r >= filas:
            tr += 1
            r -= filas
        if c < 0:
            tc -= 1
            c += columnas
        if c >= columnas:
            tc += 1
            c -= columnas
        if not (0 <= r < filas and 0 <= c < columnas and matriz[r][c] != '#'):
            continue
        if (tr, tc, r, c) in distancias:
            continue
        if abs(tr) > 4 or abs(tc) > 4:
            continue
        distancias[(tr, tc, r, c)] = d
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            cola.append((tr, tc, r+dr, c+dc, d+1))
    return distancias


def resolver(d, v, L, filas, soluciones):
    cantidad = (L-d)//filas
    if (d, v, L) in soluciones:
        return soluciones[(d, v, L)]
    resultado = 0
    for x in range(1, cantidad+1):
        if d+filas*x <= L and (d+filas*x) % 2 == (L % 2):
            resultado += ((x+1) if v == 2 else 1)
    soluciones[(d, v, L)] = resultado
    return resultado


def resolver21(part1, filas, columnas, matriz, distancias, soluciones):
    L = (64 if part1 else 26501365)
    respuesta = 0
    for r in range(filas):
        for c in range(columnas):
            if (0, 0, r, c) in distancias:
                def rapido(tr, tc):
                    respuesta = 0
                    B = 3
                    if tr > B:
                        respuesta += filas*(abs(tr)-B)
                        tr = B
                    if tr < -B:
                        respuesta += filas*(abs(tr)-B)
                        tr = -B
                    if tc > B:
                        respuesta += columnas*(abs(tc)-B)
                        tc = B
                    if tc < -B:
                        respuesta += columnas*(abs(tc)-B)
                        tc = -B
                    respuesta += distancias[(tr, tc, r, c)]
                    return respuesta

                OPT = [-3, -2, -1, 0, 1, 2, 3]
                for tr in OPT:
                    for tc in OPT:
                        if part1 and (tr != 0 or tc != 0):
                            continue
                        d = distancias[(tr, tc, r, c)]
                        if d % 2 == L % 2 and d <= L:
                            respuesta += 1
                        if tr in [min(OPT), max(OPT)] and tc in [min(OPT), max(OPT)]:
                            respuesta += resolver(d, 2, L, filas, soluciones)
                        elif tr in [min(OPT), max(OPT)] or tc in [min(OPT), max(OPT)]:
                            respuesta += resolver(d, 1, L, filas, soluciones)
    return respuesta


def main(ruta):
    datos = abrir_archivo(ruta)
    lineas = dividir_lineas(datos)
    matriz = generar_matriz(lineas)
    filas, columnas = obtener_dimensiones(matriz)
    sr, sc = encontrar_inicio(matriz, filas, columnas)
    distancias = encontrar_distancias(sr, sc, filas, columnas, matriz)
    soluciones = {}
    print(resolver21(True, filas, columnas, matriz, distancias, soluciones))
    print(resolver21(False, filas, columnas, matriz, distancias, soluciones))


main(sys.argv[1])
