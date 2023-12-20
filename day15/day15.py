import sys
from collections import defaultdict


def hash_string(s):
    hash_value = 0
    for c in s:
        hash_value = ((hash_value + ord(c)) * 17) % 256
    return hash_value


def calcular_p1(comandos):
    p1 = 0
    for cmd in comandos:
        p1 += hash_string(cmd)
    return p1


def procesar_comandos(comandos):
    cajas = defaultdict(list)

    for cmd in comandos:
        if cmd.endswith('-'):
            nombre = cmd[:-1]
            hash_value = hash_string(nombre)
            cajas[hash_value] = [(n, v)
                                 for (n, v) in cajas[hash_value] if n != nombre]
        elif cmd.endswith('='):
            nombre = cmd[:-2]
            hash_value = hash_string(nombre)
            longitud = int(cmd[-1])
            if any(nombre == n for (n, v) in cajas[hash_value]):
                cajas[hash_value] = [(n, longitud) if nombre == n else (
                    n, v) for (n, v) in cajas[hash_value]]
            else:
                cajas[hash_value].append((nombre, longitud))

    return cajas


if __name__ == "__main__":
    archivo = open(sys.argv[1], "r")
    lineas = archivo.read().strip().split('\n')
    comandos = lineas[0].split(',')

    p1 = calcular_p1(comandos)
    print(p1)
