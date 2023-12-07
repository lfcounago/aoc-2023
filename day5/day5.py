import sys


def leer_datos(archivo):
    with open(archivo, 'r') as f:
        lineas = f.read().split('\n')

    semillas = list(map(int, lineas[0].split(':')[1].split()))

    mapas = []
    mapa_actual = []
    for linea in lineas[1:]:
        if 'map:' in linea:
            if mapa_actual:
                mapas.append(mapa_actual)
            mapa_actual = []
        elif linea:
            mapa_actual.append(tuple(map(int, linea.split())))

    if mapa_actual:
        mapas.append(mapa_actual)

    return semillas, mapas


def convertir_numero(numero, mapa_conversion):
    for inicio_dest, inicio_origen, longitud in mapa_conversion:
        if inicio_origen <= numero < inicio_origen + longitud:
            return inicio_dest + (numero - inicio_origen)
    return numero


def calcular_p1(semillas, mapas):
    numeros_suelo = [convertir_numero(semilla, mapas[0])
                     for semilla in semillas]

    numeros_fertilizante = [convertir_numero(
        suelo, mapas[1]) for suelo in numeros_suelo]

    numeros_agua = [convertir_numero(fertilizante, mapas[2])
                    for fertilizante in numeros_fertilizante]

    numeros_luz = [convertir_numero(agua, mapas[3]) for agua in numeros_agua]

    numeros_temperatura = [convertir_numero(
        luz, mapas[4]) for luz in numeros_luz]

    numeros_humedad = [convertir_numero(
        temperatura, mapas[5]) for temperatura in numeros_temperatura]

    numeros_ubicacion = [convertir_numero(
        humedad, mapas[6]) for humedad in numeros_humedad]

    ubicacion_mas_baja = min(numeros_ubicacion)

    return ubicacion_mas_baja


def main():
    nombre_archivo = sys.argv[1]
    semillas, mapas = leer_datos(nombre_archivo)
    p1 = calcular_p1(semillas, mapas)
    print(p1)


if __name__ == "__main__":
    main()
