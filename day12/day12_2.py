cache = {}


def contar_combinaciones(resortes, numeros_dañados):
    if len(resortes) == 0:
        if numeros_dañados == ():
            return 1
        return 0

    if numeros_dañados == ():
        if "#" not in resortes:
            return 1
        return 0

    total_combinaciones = 0

    if (resortes, numeros_dañados) in cache:
        return cache[(resortes, numeros_dañados)]

    if resortes[0] in ".?":
        total_combinaciones += contar_combinaciones(
            resortes[1:], numeros_dañados)

    if resortes[0] in "#?":
        if numeros_dañados[0] <= len(resortes) and "." not in resortes[:numeros_dañados[0]] and (numeros_dañados[0] == len(resortes) or resortes[numeros_dañados[0]] != "#"):
            total_combinaciones += contar_combinaciones(
                resortes[numeros_dañados[0] + 1:], numeros_dañados[1:])

    cache[resortes, numeros_dañados] = total_combinaciones

    return total_combinaciones


with open("input12.txt", "r") as archivo:
    resortes_lista = archivo.read().splitlines()

total_combinaciones = 0
for linea in resortes_lista:
    resortes, numeros_dañados = linea.split()
    resortes = "?".join([resortes] * 5)
    numeros_dañados = tuple(map(int, numeros_dañados.split(",") * 5))
    total_combinaciones += contar_combinaciones(resortes, numeros_dañados)

print(total_combinaciones)
