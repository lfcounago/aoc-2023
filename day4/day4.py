import sys


def leer_archivo(nombre_archivo):
    with open(nombre_archivo) as archivo:
        datos = archivo.read().strip()
    return datos


def calcular_p1(datos):
    p1 = 0

    for linea in datos.split('\n'):
        id_carta, rondas = linea.split(':')
        ganadores, numeros = rondas.split('|')
        ganadores = set(ganadores.split())
        numeros = numeros.split()
        ronda = 0
        for numero in numeros:
            if numero in ganadores:
                ronda = ronda * 2 if ronda else 1
        p1 += ronda

    return p1


def calcular_p2(datos):
    tarjetas = datos.split('\n')
    c = [1]*len(tarjetas)
    for i, linea in enumerate(tarjetas):
        id_carta, rondas = linea.split(':')
        ganadores, numeros = rondas.split('|')
        ganadores = set(ganadores.split())
        numeros = set(numeros.split())
        puntos = len(ganadores.intersection(numeros))
        for j in range(puntos):
            if j+i+1 < len(c):
                c[j+i+1] += c[i]
    return sum(c)


def main():
    nombre_archivo = sys.argv[1]
    datos = leer_archivo(nombre_archivo)
    p1 = calcular_p1(datos)
    print(p1)
    p2 = calcular_p2(datos)
    print(p2)


if __name__ == "__main__":
    main()
