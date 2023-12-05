import sys
from collections import defaultdict


def leer_archivo(nombre_archivo):
    with open(nombre_archivo) as archivo:
        datos = archivo.read().strip()
    return datos


def inicializar_matriz(datos):
    lineas = datos.split('\n')
    matriz = [[c for c in linea] for linea in lineas]
    return matriz


def calcular_p1(matriz):
    R = len(matriz)
    C = len(matriz[0])
    p1 = 0
    nums = defaultdict(list)
    for r in range(R):
        gears = set()
        n = 0
        has_part = False
        for c in range(len(matriz[r])+1):
            if c < C and matriz[r][c].isdigit():
                n = n*10 + int(matriz[r][c])
                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        if 0 <= r+rr < R and 0 <= c+cc < C:
                            ch = matriz[r+rr][c+cc]
                            if not ch.isdigit() and ch != '.':
                                has_part = True
                            if ch == '*':
                                gears.add((r+rr, c+cc))
            elif n > 0:
                for gear in gears:
                    nums[gear].append(n)
                if has_part:
                    p1 += n
                n = 0
                has_part = False
                gears = set()
    return p1, nums


def calcular_p2(nums):
    p2 = 0
    for k, v in nums.items():
        if len(v) == 2:
            p2 += v[0] * v[1]
    return p2


def main():
    nombre_archivo = sys.argv[1]
    datos = leer_archivo(nombre_archivo)
    matriz = inicializar_matriz(datos)
    p1, nums = calcular_p1(matriz)
    print(p1)
    p2 = calcular_p2(nums)
    print(p2)


if __name__ == "__main__":
    main()
