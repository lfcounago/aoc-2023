import sys


def leer_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        datos = archivo.read().strip().split('\n')
    return datos


def crear_matriz(datos):
    return [[c for c in row] for row in datos]


def siguiente_paso(r, c, d):
    movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    return (r + movimientos[d][0], c + movimientos[d][1], d)


def calcular_puntaje(sr, sc, sd, matriz):
    posiciones = [(sr, sc, sd)]
    visto = set()
    visto2 = set()

    while True:
        nuevas_posiciones = []
        if not posiciones:
            break

        for (r, c, d) in posiciones:
            if 0 <= r < R and 0 <= c < C:
                visto.add((r, c))

                if (r, c, d) in visto2:
                    continue

                visto2.add((r, c, d))
                caracter = matriz[r][c]

                if caracter == '.':
                    nuevas_posiciones.append(siguiente_paso(r, c, d))
                elif caracter == '/':
                    nuevas_posiciones.append(siguiente_paso(
                        r, c, {0: 1, 1: 0, 2: 3, 3: 2}[d]))
                elif caracter == '\\':
                    nuevas_posiciones.append(siguiente_paso(
                        r, c, {0: 3, 1: 2, 2: 1, 3: 0}[d]))
                elif caracter == '|':
                    if d in [0, 2]:
                        nuevas_posiciones.append(siguiente_paso(r, c, d))
                    else:
                        nuevas_posiciones.append(siguiente_paso(r, c, 0))
                        nuevas_posiciones.append(siguiente_paso(r, c, 2))
                elif caracter == '-':
                    if d in [1, 3]:
                        nuevas_posiciones.append(siguiente_paso(r, c, d))
                    else:
                        nuevas_posiciones.append(siguiente_paso(r, c, 1))
                        nuevas_posiciones.append(siguiente_paso(r, c, 3))
                else:
                    assert False

        posiciones = nuevas_posiciones

    return len(visto)


def calcular_puntaje_maximo(matriz):
    puntaje_maximo = 0

    for r in range(R):
        puntaje_maximo = max(puntaje_maximo, calcular_puntaje(r, 0, 1, matriz))
        puntaje_maximo = max(
            puntaje_maximo, calcular_puntaje(r, C - 1, 3, matriz))

    for c in range(C):
        puntaje_maximo = max(puntaje_maximo, calcular_puntaje(0, c, 2, matriz))
        puntaje_maximo = max(
            puntaje_maximo, calcular_puntaje(R - 1, c, 0, matriz))

    return puntaje_maximo


if __name__ == "__main__":
    nombre_archivo = sys.argv[1]
    datos = leer_archivo(nombre_archivo)
    matriz = crear_matriz(datos)

    R = len(matriz)
    C = len(matriz[0])

    print(calcular_puntaje(0, 0, 1, matriz))
    puntaje_maximo = calcular_puntaje_maximo(matriz)
    print(puntaje_maximo)
