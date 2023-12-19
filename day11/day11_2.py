def leer_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return [list(line) for line in archivo.read().splitlines()]


def encontrar_filas_vacias(galaxy_map):
    return [i for i, fila in enumerate(galaxy_map) if all(char == '.' for char in fila)]


def encontrar_columnas_vacias(galaxy_map):
    return [i for i, columna in enumerate(zip(*galaxy_map)) if all(char == '.' for char in columna)]


def encontrar_galaxias(galaxy_map):
    return [(fila, columna) for fila, linea in enumerate(galaxy_map)
            for columna, char in enumerate(linea) if char == '#']


def calcular_distancia_total(galaxies, empty_rows, empty_cols):
    total_distancia = 0

    for i, (fila_galaxia, col_galaxia) in enumerate(galaxies):
        for (fila_otra_galaxia, col_otra_galaxia) in galaxies[:i]:
            for fila in range(min(fila_otra_galaxia, fila_galaxia), max(fila_otra_galaxia, fila_galaxia)):
                total_distancia += int(1e6) if fila in empty_rows else 1

            for col in range(min(col_otra_galaxia, col_galaxia), max(col_otra_galaxia, col_galaxia)):
                total_distancia += int(1e6) if col in empty_cols else 1

    return total_distancia


if __name__ == "__main__":
    nombre_archivo = "input11.txt"
    galaxy_map = leer_archivo(nombre_archivo)

    filas_vacias = encontrar_filas_vacias(galaxy_map)
    columnas_vacias = encontrar_columnas_vacias(galaxy_map)
    galaxias = encontrar_galaxias(galaxy_map)

    distancia_total = calcular_distancia_total(
        galaxias, filas_vacias, columnas_vacias)
    print(distancia_total)
