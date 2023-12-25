import sys
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
import heapq
import math
import networkx as nx


def abrir_archivo(ruta):
    return open(ruta).read().strip()


def dividir_lineas(datos):
    return datos.split('\n')


def generar_grafo(lineas):
    grafo = defaultdict(set)
    for linea in lineas:
        inicio, fin = linea.split(':')
        for nodo in fin.split():
            grafo[inicio].add(nodo)
            grafo[nodo].add(inicio)
    return grafo


def crear_digrafo(grafo):
    digrafo = nx.DiGraph()
    for nodo, vecinos in grafo.items():
        for vecino in vecinos:
            digrafo.add_edge(nodo, vecino, capacity=1.0)
            digrafo.add_edge(vecino, nodo, capacity=1.0)
    return digrafo


def calcular_cortes(grafo):
    nodos = list(grafo.nodes())
    for nodo_inicio in nodos:
        for nodo_fin in nodos:
            if nodo_inicio != nodo_fin:
                valor_corte, (conjunto1, conjunto2) = nx.minimum_cut(
                    grafo, nodo_inicio, nodo_fin)
                if valor_corte == 3:
                    return len(conjunto1) * len(conjunto2)


def main(ruta):
    datos_archivo = abrir_archivo(ruta)
    lineas = dividir_lineas(datos_archivo)
    grafo = generar_grafo(lineas)
    digrafo = crear_digrafo(grafo)
    resultado = calcular_cortes(digrafo)
    print(resultado)


main(sys.argv[1])
