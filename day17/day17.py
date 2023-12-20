import sys
import heapq


def leer_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        datos = archivo.read().strip().split('\n')
    return datos


def crear_matriz(datos):
    return [[c for c in row] for row in datos]


def resolver(part2, matriz):
    R = len(matriz)
    C = len(matriz[0])
    Q = [(0, 0, 0, -1, -1)]
    D = {}

    while Q:
        dist, r, c, dir_, indir = heapq.heappop(Q)

        if (r, c, dir_, indir) in D:
            continue

        D[(r, c, dir_, indir)] = dist

        movimientos = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for i, (dr, dc) in enumerate(movimientos):
            rr = r + dr
            cc = c + dc
            new_dir = i
            new_indir = (1 if new_dir != dir_ else indir + 1)

            isnt_reverse = ((new_dir + 2) % 4 != dir_)
            isvalid_part1 = (new_indir <= 3)
            isvalid_part2 = (new_indir <= 10 and (
                new_dir == dir_ or indir >= 4 or indir == -1))
            isvalid = (isvalid_part2 if part2 else isvalid_part1)

            if 0 <= rr < R and 0 <= cc < C and isnt_reverse and isvalid:
                cost = int(matriz[rr][cc])

                if (rr, cc, new_dir, new_indir) in D:
                    continue

                heapq.heappush(Q, (dist + cost, rr, cc, new_dir, new_indir))

    ans = float('inf')
    for (r, c, dir_, indir), v in D.items():
        if r == R - 1 and c == C - 1 and (indir >= 4 or not part2):
            ans = min(ans, v)

    return ans


if __name__ == "__main__":
    nombre_archivo = sys.argv[1]
    datos = leer_archivo(nombre_archivo)
    matriz = crear_matriz(datos)

    resultado_parte1 = resolver(False, matriz)
    resultado_parte2 = resolver(True, matriz)

    print(resultado_parte1)
    print(resultado_parte2)
