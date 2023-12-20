import sys
from typing import List
from dataclasses import dataclass


@dataclass
class Instruccion:
    direccion: str
    cantidad: int


def parsear_entrada(entrada: str, parte2: bool) -> List[Instruccion]:
    instrucciones = []
    for linea in entrada.split('\n'):
        direccion, cantidad, hex_ = linea.split()
        if not parte2:
            instrucciones.append(Instruccion(direccion, int(cantidad)))
        else:
            hex_ = hex_[1:-1]
            direccion = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}[int(hex_[-1])]
            cantidad = int(hex_[1:-1], 16)
            instrucciones.append(Instruccion(direccion, cantidad))
    return instrucciones


def calcular_area_shoelace(instrucciones: List[Instruccion]) -> int:
    vertices = []
    posicion = (0, 0)

    for instruccion in instrucciones:
        direccion, cantidad = instruccion.direccion, instruccion.cantidad
        if direccion == 'R':
            posicion = (posicion[0] + cantidad, posicion[1])
        elif direccion == 'D':
            posicion = (posicion[0], posicion[1] - cantidad)
        elif direccion == 'L':
            posicion = (posicion[0] - cantidad, posicion[1])
        elif direccion == 'U':
            posicion = (posicion[0], posicion[1] + cantidad)
        vertices.append(posicion)

    area = 0
    for i in range(len(vertices)):
        area -= vertices[i][0] * vertices[(i + 1) % len(vertices)][1]
        area += vertices[i][1] * vertices[(i + 1) % len(vertices)][0]
    area //= 2
    return area


def calcular_area_green(instrucciones: List[Instruccion]) -> int:
    area = 0
    y = 0

    for instruccion in instrucciones:
        if instruccion.direccion == 'R':
            area += y * instruccion.cantidad
        elif instruccion.direccion == 'L':
            area -= y * instruccion.cantidad
        elif instruccion.direccion == 'U':
            y += instruccion.cantidad
        elif instruccion.direccion == 'D':
            y -= instruccion.cantidad

    return area


entrada = open(sys.argv[1]).read().strip()

for parte2 in [False, True]:
    instrucciones = parsear_entrada(entrada, parte2)
    perimetro = sum(instruccion.cantidad for instruccion in instrucciones)
    area_shoelace = calcular_area_shoelace(instrucciones)
    area_green = calcular_area_green(instrucciones)
    assert area_shoelace == area_green, f'shoelace={area_shoelace} green={area_green}'
    respuesta = area_shoelace + (perimetro // 2) + 1
    print(respuesta)
