def leer_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return [list(line) for line in archivo.read().split("\n")]


def encontrar_posicion_inicial(grid):
    for row, line in enumerate(grid):
        for column, char in enumerate(line):
            if char == 'S':
                return row, column


def buscar_pipes(grid, row, column):
    check_pipes = [(row, column)]
    seen_pipes = {(row, column)}

    while check_pipes:
        row, column = check_pipes.pop(0)
        current_pipe = grid[row][column]

        if row > 0 and current_pipe in "S|LJ" and grid[row - 1][column] in "|7F" and (row - 1, column) not in seen_pipes:
            seen_pipes.add((row - 1, column))
            check_pipes.append((row - 1, column))

        if row < len(grid) - 1 and current_pipe in "S|7F" and grid[row + 1][column] in "|LJ" and (row + 1, column) not in seen_pipes:
            seen_pipes.add((row + 1, column))
            check_pipes.append((row + 1, column))

        if column > 0 and current_pipe in "S-7J" and grid[row][column - 1] in "-LF" and (row, column - 1) not in seen_pipes:
            seen_pipes.add((row, column - 1))
            check_pipes.append((row, column - 1))

        if column < len(grid[row]) - 1 and current_pipe in "S-LF" and grid[row][column + 1] in "-J7" and (row, column + 1) not in seen_pipes:
            seen_pipes.add((row, column + 1))
            check_pipes.append((row, column + 1))

    return seen_pipes


if __name__ == "__main__":
    nombre_archivo = "input10.txt"
    grid = leer_archivo(nombre_archivo)
    starting_row, starting_column = encontrar_posicion_inicial(grid)

    seen_pipes = buscar_pipes(grid, starting_row, starting_column)
    furthest_distance = len(seen_pipes) // 2
    print(furthest_distance)
