import sys
from collections import defaultdict


def leer_archivo(ruta):
    with open(ruta, 'r') as archivo:
        return archivo.read().strip().split('\n')


def rotar(grilla):
    filas = len(grilla)
    columnas = len(grilla[0])
    nueva_grilla = [['?' for _ in range(filas)] for _ in range(columnas)]
    for fila in range(filas):
        for columna in range(columnas):
            nueva_grilla[columna][filas-1-fila] = grilla[fila][columna]
    return nueva_grilla


def rodar(grilla):
    filas = len(grilla)
    columnas = len(grilla[0])
    for columna in range(columnas):
        for _ in range(filas):
            for fila in range(filas):
                if grilla[fila][columna] == 'O' and fila > 0 and grilla[fila-1][columna] == '.':
                    grilla[fila][columna] = '.'
                    grilla[fila-1][columna] = 'O'
    return grilla


def puntuar(grilla):
    puntos = 0
    filas = len(grilla)
    columnas = len(grilla[0])
    for fila in range(filas):
        for columna in range(columnas):
            if grilla[fila][columna] == 'O':
                puntos += len(grilla)-fila
    return puntos


def main(ruta):
    datos = leer_archivo(ruta)
    grilla = [[c for c in fila] for fila in datos]
    grillas = {}

    objetivo = 10**9
    t = 0
    while t < objetivo:
        t += 1
        for j in range(4):
            grilla = rodar(grilla)
            if t == 1 and j == 0:
                print(puntuar(grilla))  # parte1
            grilla = rotar(grilla)
        grilla_hash = tuple(tuple(fila) for fila in grilla)
        if grilla_hash in grillas:
            longitud_ciclo = t-grillas[grilla_hash]
            cantidad = (objetivo-t)//longitud_ciclo
            t += cantidad * longitud_ciclo
        grillas[grilla_hash] = t
    print(puntuar(grilla))


main(sys.argv[1])
