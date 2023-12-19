def leer_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return [list(line) for line in archivo.read().split("\n")]


def encontrar_posicion_inicial(grid):
    for row, line in enumerate(grid):
        for column, char in enumerate(line):
            if char == 'S':
                return row, column


def buscar_pipes(grid, starting_row, starting_column):
    check_pipes = [(starting_row, starting_column)]
    seen_pipes = {(starting_row, starting_column)}
    potential_s = {'|', '-', 'L', 'J', '7', 'F'}

    while check_pipes:
        row, column = check_pipes.pop(0)
        current_pipe = grid[row][column]

        if row > 0 and current_pipe in "S|LJ" and grid[row - 1][column] in "|7F" and (row - 1, column) not in seen_pipes:
            seen_pipes.add((row - 1, column))
            check_pipes.append((row - 1, column))
            if current_pipe == 'S':
                potential_s = potential_s.intersection({'|', 'L', 'J'})

        if row < len(grid) - 1 and current_pipe in "S|7F" and grid[row + 1][column] in "|LJ" and (row + 1, column) not in seen_pipes:
            seen_pipes.add((row + 1, column))
            check_pipes.append((row + 1, column))
            if current_pipe == 'S':
                potential_s = potential_s.intersection({'|', '7', 'F'})

        if column > 0 and current_pipe in "S-7J" and grid[row][column - 1] in "-LF" and (row, column - 1) not in seen_pipes:
            seen_pipes.add((row, column - 1))
            check_pipes.append((row, column - 1))
            if current_pipe == 'S':
                potential_s = potential_s.intersection({'-', '7', 'J'})

        if column < len(grid[row]) - 1 and current_pipe in "S-LF" and grid[row][column + 1] in "-J7" and (row, column + 1) not in seen_pipes:
            seen_pipes.add((row, column + 1))
            check_pipes.append((row, column + 1))
            if current_pipe == 'S':
                potential_s = potential_s.intersection({'-', 'L', 'F'})

    return seen_pipes, potential_s.pop()


def actualizar_grid(grid, seen_pipes, s_pipe):
    return [['.' if (row, column) not in seen_pipes else grid[row][column]
             for column in range(len(grid[row]))] for row in range(len(grid))]


def contar_interior(grid):
    interior = 0
    for row in grid:
        for i, char in enumerate(row):
            if char != ".":
                continue

            intersect = 0
            corner_pipes = []
            for j in range(i + 1, len(row)):
                if row[j] in "|":
                    intersect += 1
                if row[j] in "FL":
                    corner_pipes.append(row[j])
                if len(corner_pipes) != 0 and row[j] == "J" and corner_pipes[-1] == "F" or row[j] == "7" and corner_pipes[-1] == "L":
                    corner_pipes.pop(-1)
                    intersect += 1

            if intersect % 2 == 1:
                interior += 1

    return interior


if __name__ == "__main__":
    nombre_archivo = "input10.txt"
    grid = leer_archivo(nombre_archivo)
    starting_row, starting_column = encontrar_posicion_inicial(grid)

    seen_pipes, s_pipe = buscar_pipes(grid, starting_row, starting_column)
    grid = actualizar_grid(grid, seen_pipes, s_pipe)

    interior = contar_interior(grid)
    print(interior)
