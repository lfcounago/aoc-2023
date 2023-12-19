import sys
import re
from math import gcd
from collections import defaultdict, Counter


def calcular_diferencias(lista, parte2):
    if all(x == 0 for x in lista):
        return 0
    diferencias = []
    for i in range(len(lista) - 1):
        diferencias.append(lista[i + 1] - lista[i])
    return lista[0 if parte2 else -1] + (-1 if parte2 else 1) * calcular_diferencias(diferencias, parte2)


def procesar_entrada(entrada):
    lineas = entrada.split('\n')
    for parte2 in [False, True]:
        resultado = 0
        for linea in lineas:
            numeros = [int(x) for x in linea.split()]
            resultado += calcular_diferencias(numeros, parte2)
        print(resultado)


# Leer el archivo de entrada
with open(sys.argv[1], 'r') as archivo:
    entrada = archivo.read().strip()
    procesar_entrada(entrada)
