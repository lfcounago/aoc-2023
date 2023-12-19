MAPEO_CARTAS = {'T': 'A', 'J': 'B', 'Q': 'C', 'K': 'D', 'A': 'E'}


def obtener_tipo(mano):
    conteos = {carta: mano.count(carta) for carta in mano}
    if len(conteos) == 1:
        return 6
    if len(conteos) == 2:
        if 4 in conteos.values():
            return 5
        if 3 in conteos.values() and 2 in conteos.values():
            return 4
    if len(conteos) == 3:
        if 3 in conteos.values() and list(conteos.values()).count(1) == 2:
            return 3
        if list(conteos.values()).count(2) == 2:
            return 2
    if len(conteos) == 4:
        return 1
    return 0


def obtener_orden(mano):
    orden = []
    for carta in mano:
        if carta in MAPEO_CARTAS:
            orden.append(MAPEO_CARTAS[carta])
        else:
            orden.append(carta)
    return orden


def ordenar(mano):
    return obtener_tipo(mano), obtener_orden(mano)


def encontrar_todas_combinaciones(mano):
    if not mano:
        return [""]

    carta_actual = mano[0]
    if carta_actual == 'J':
        valores_posibles = "23456789TQKA"
    else:
        valores_posibles = carta_actual

    combinaciones = [
        primera_mitad + segunda_mitad
        for primera_mitad in valores_posibles
        for segunda_mitad in encontrar_todas_combinaciones(mano[1:])
    ]

    return combinaciones


def encontrar_tipo_maximo(mano):
    return max(map(obtener_tipo, encontrar_todas_combinaciones(mano)))


def ordenar2(mano):
    return encontrar_tipo_maximo(mano), obtener_orden(mano)


jugadas = []
with open("input7.txt") as archivo:
    datos = archivo.readlines()
    for linea in datos:
        mano, apuesta = linea.strip().split()
        jugadas.append((mano, int(apuesta)))

jugadas1 = sorted(jugadas, key=lambda jugada: ordenar(jugada[0]))

p1 = sum(apuesta * rango for rango,
         (mano, apuesta) in enumerate(jugadas1, 1))

jugadas2 = sorted(jugadas, key=lambda jugada: ordenar2(jugada[0]))
p2 = 0
for rank, (mano, apuesta) in enumerate(jugadas2, 1):
    p2 += apuesta * rank

print("P1: ", p1)

print("P2: ", p2)
