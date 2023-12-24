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


def encontrar_intersecciones(matriz, filas, columnas):
    intersecciones = set()
    for fila in range(filas):
        for columna in range(columnas):
            vecinos = 0
            for caracter, df, dc in [['^', -1, 0], ['v', 1, 0], ['<', 0, -1], ['>', 0, 1]]:
                if (0 <= fila+df < filas and 0 <= columna+dc < columnas and matriz[fila+df][columna+dc] != '#'):
                    vecinos += 1
            if vecinos > 2 and matriz[fila][columna] != '#':
                intersecciones.add((fila, columna))
    return intersecciones


def encontrar_entradas_salidas(matriz, filas, columnas, intersecciones):
    inicio = None
    fin = None
    for columna in range(columnas):
        if matriz[0][columna] == '.':
            intersecciones.add((0, columna))
            inicio = (0, columna)
        if matriz[filas-1][columna] == '.':
            intersecciones.add((filas-1, columna))
            fin = (filas-1, columna)
    return inicio, fin, intersecciones


def generar_grafo(matriz, filas, columnas, intersecciones, parte1):
    grafo = {}
    for (fila_v, columna_v) in intersecciones:
        grafo[(fila_v, columna_v)] = []
        cola = deque([(fila_v, columna_v, 0)])
        visitados = set()
        while cola:
            fila, columna, distancia = cola.popleft()
            if (fila, columna) in visitados:
                continue
            visitados.add((fila, columna))
            if (fila, columna) in intersecciones and (fila, columna) != (fila_v, columna_v):
                grafo[(fila_v, columna_v)].append(((fila, columna), distancia))
                continue
            for caracter, df, dc in [['^', -1, 0], ['v', 1, 0], ['<', 0, -1], ['>', 0, 1]]:
                if (0 <= fila+df < filas and 0 <= columna+dc < columnas and matriz[fila+df][columna+dc] != '#'):
                    if parte1 and matriz[fila][columna] in ['<', '>', '^', 'v'] and matriz[fila][columna] != caracter:
                        continue
                    cola.append((fila+df, columna+dc, distancia+1))
    return grafo


def resolver(grafo, filas, columnas, inicio):
    maxima_distancia = 0
    visitados = [[False for _ in range(columnas)] for _ in range(filas)]

    def dfs(nodo, distancia):
        nonlocal maxima_distancia
        fila, columna = nodo
        if visitados[fila][columna]:
            return
        visitados[fila][columna] = True
        if fila == filas-1:
            maxima_distancia = max(maxima_distancia, distancia)
        for (vecino, distancia_vecino) in grafo[nodo]:
            dfs(vecino, distancia+distancia_vecino)
        visitados[fila][columna] = False

    dfs(inicio, 0)
    return maxima_distancia


def main(ruta):
    datos = abrir_archivo(ruta)
    lineas = dividir_lineas(datos)
    matriz = generar_matriz(lineas)
    filas, columnas = obtener_dimensiones(matriz)
    intersecciones = encontrar_intersecciones(matriz, filas, columnas)
    inicio, fin, intersecciones = encontrar_entradas_salidas(
        matriz, filas, columnas, intersecciones)
    grafo = generar_grafo(matriz, filas, columnas, intersecciones, True)
    resultado1 = resolver(grafo, filas, columnas, inicio)
    grafo = generar_grafo(matriz, filas, columnas, intersecciones, False)
    resultado2 = resolver(grafo, filas, columnas, inicio)
    print(resultado1)
    print(resultado2)


main(sys.argv[1])
