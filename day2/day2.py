import sys
file = open(sys.argv[1]).read().strip()

possible = 0
power_sum = 0

print("Inicio del programa")


for linea in file.split('\n'):
    id_juego, rondas = linea.split(':')
    id_juego = int(id_juego.split()[1])
    rondas = rondas.split(';')
    max_cubos = {'red': 0, 'green': 0, 'blue': 0}
    min_cubos = {'red': 0, 'green': 0, 'blue': 0}
    for ronda in rondas:
        cubos = ronda.split(',')
        cubos_ronda = {'red': 0, 'green': 0, 'blue': 0}
        for cubo in cubos:
            numero, color = cubo.split()
            numero = int(numero)
            cubos_ronda[color] = max(cubos_ronda[color], numero)
        for color in min_cubos:
            min_cubos[color] = max(min_cubos[color], cubos_ronda[color])
            max_cubos[color] = max(max_cubos[color], cubos_ronda[color])
    if max_cubos['red'] <= 12 and max_cubos['green'] <= 13 and max_cubos['blue'] <= 14:
        possible += id_juego
    power_sum += min_cubos['red'] * min_cubos['green'] * min_cubos['blue']

print("Parte 1: ", possible)
print("Parte 2: ", power_sum)

print("Fin del programa")
