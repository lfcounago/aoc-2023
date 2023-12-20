import sys
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque


def calcular_simetria(grilla, parte2):
    resultado = 0
    filas = len(grilla)
    columnas = len(grilla[0])

    for columna in range(columnas - 1):
        malos = 0
        for dc in range(columnas):
            izquierda = columna - dc
            derecha = columna + 1 + dc
            if 0 <= izquierda < derecha < columnas:
                for fila in range(filas):
                    if grilla[fila][izquierda] != grilla[fila][derecha]:
                        malos += 1
        if malos == (1 if parte2 else 0):
            resultado += columna + 1

    for fila in range(filas - 1):
        malos = 0
        for dr in range(filas):
            arriba = fila - dr
            abajo = fila + 1 + dr
            if 0 <= arriba < abajo < filas:
                for columna in range(columnas):
                    if grilla[arriba][columna] != grilla[abajo][columna]:
                        malos += 1
        if malos == (1 if parte2 else 0):
            resultado += 100 * (fila + 1)

    return resultado


def procesar_entrada(entrada):
    for parte2 in [False, True]:
        resultado = 0
        for grilla in entrada.split('\n\n'):
            grilla = [list(fila) for fila in grilla.split('\n')]
            resultado += calcular_simetria(grilla, parte2)
        print(resultado)


# Leer el archivo de entrada
with open(sys.argv[1], 'r') as archivo:
    entrada = archivo.read().strip()
    procesar_entrada(entrada)
