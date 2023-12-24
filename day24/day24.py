import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
import heapq
import math
from z3 import *


def abrir_archivo(ruta):
    return open(ruta).read().strip()


def dividir_lineas(datos):
    return datos.split('\n')


def generar_matriz(lineas):
    return [[c for c in fila] for fila in lineas]


def obtener_dimensiones(matriz):
    return len(matriz), len(matriz[0])


def obtener_datos(lineas):
    datos = []
    for linea in lineas:
        pos, vel = linea.split('@')
        x, y, z = pos.split(', ')
        vx, vy, vz = vel.split(', ')
        x, y, z = int(x), int(y), int(z)
        vx, vy, vz = int(vx), int(vy), int(vz)
        datos.append((x, y, z, vx, vy, vz))
    return datos


def calcular_intersecciones(datos):
    total = 0
    for i in range(len(datos)):
        for j in range(i+1, len(datos)):
            x1 = datos[i][0]
            x2 = datos[i][0]+datos[i][3]
            x3 = datos[j][0]
            x4 = datos[j][0]+datos[j][3]
            y1 = datos[i][1]
            y2 = datos[i][1]+datos[i][4]
            y3 = datos[j][1]
            y4 = datos[j][1]+datos[j][4]

            den = ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
            if den != 0:
                px = ((x1*y2 - y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)) / \
                    ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
                py = ((x1*y2 - y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / \
                    ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
                validoA = (px > x1) == (x2 > x1)
                validoB = (px > x3) == (x4 > x3)

                if 200000000000000 <= px <= 400000000000000 and 200000000000000 <= py <= 400000000000000 and validoA and validoB:
                    total += 1
    return total


def resolver_z3(datos):
    x, y, z, vx, vy, vz = Int('x'), Int('y'), Int(
        'z'), Int('vx'), Int('vy'), Int('vz')
    T = [Int(f'T{i}') for i in range(len(datos))]
    SOLUCION = Solver()
    for i in range(len(datos)):
        SOLUCION.add(x + T[i]*vx - datos[i][0] - T[i]*datos[i][3] == 0)
        SOLUCION.add(y + T[i]*vy - datos[i][1] - T[i]*datos[i][4] == 0)
        SOLUCION.add(z + T[i]*vz - datos[i][2] - T[i]*datos[i][5] == 0)
    res = SOLUCION.check()
    M = SOLUCION.model()
    return M.eval(x+y+z)


def main(ruta):
    datos_archivo = abrir_archivo(ruta)
    lineas = dividir_lineas(datos_archivo)
    matriz = generar_matriz(lineas)
    filas, columnas = obtener_dimensiones(matriz)
    datos = obtener_datos(lineas)
    resultado1 = calcular_intersecciones(datos)
    resultado2 = resolver_z3(datos)
    print(resultado1)
    print(resultado2)


main(sys.argv[1])
