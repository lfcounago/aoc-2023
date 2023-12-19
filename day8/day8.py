import sys
from math import gcd
from collections import defaultdict


def mcm(numeros):
    respuesta = 1
    for numero in numeros:
        respuesta = (numero * respuesta) // gcd(numero, respuesta)
    return respuesta


def obtener_reglas(entrada):
    reglas = {'Izquierda': {}, 'Derecha': {}}
    pasos, regla = entrada.split('\n\n')
    for linea in regla.split('\n'):
        estado, lr = linea.split('=')
        estado = estado.strip()
        izquierda, derecha = lr.split(',')
        izquierda = izquierda.strip()[1:].strip()
        derecha = derecha[:-1].strip()
        reglas['Izquierda'][estado] = izquierda
        reglas['Derecha'][estado] = derecha
    return pasos, reglas


def resolver(parte2, entrada):
    pasos, reglas = obtener_reglas(entrada)
    posiciones = [estado for estado in reglas['Izquierda']
                  if estado.endswith('A' if parte2 else 'AAA')]
    tiempos = {}
    tiempo = 0
    while True:
        nuevas_posiciones = []
        for i, posicion in enumerate(posiciones):
            paso = pasos[tiempo % len(pasos)]
            if posicion not in reglas['Izquierda'] and posicion not in reglas['Derecha']:
                print(
                    f"Error: Estado '{posicion}' no encontrado en las reglas.")
                return
            if paso == 'L':
                posicion = reglas['Izquierda'][posicion]
            else:
                posicion = reglas['Derecha'][posicion]
            if posicion.endswith('Z'):
                tiempos[i] = tiempo + 1
                if len(tiempos) == len(posiciones):
                    return mcm(tiempos.values())
            nuevas_posiciones.append(posicion)
        posiciones = nuevas_posiciones
        tiempo += 1


def main():
    with open(sys.argv[1]) as archivo:
        entrada = archivo.read().strip()
    print(resolver(False, entrada))
    print(resolver(True, entrada))


if __name__ == "__main__":
    main()
