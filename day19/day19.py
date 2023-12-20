import sys
from collections import deque

D = open(sys.argv[1]).read().strip()
L = D.split('\n')
G = [[c for c in row] for row in L]

reglas, partes = D.split('\n\n')
R = {}
for regla in reglas.split('\n'):
    nombre, resto = regla.split('{')
    R[nombre] = resto[:-1]


def es_aceptado(parte):
    estado = 'in'
    while True:
        regla = R[estado]
        for cmd in regla.split(','):
            aplica = True
            res = cmd
            if ':' in cmd:
                cond, res = cmd.split(':')
                var = cond[0]
                op = cond[1]
                n = int(cond[2:])
                if op == '>':
                    aplica = parte[var] > n
                else:
                    aplica = parte[var] < n
            if aplica:
                if res == 'A':
                    return True
                if res == 'R':
                    return False
                estado = res
                break


ans = 0
for parte in partes.split('\n'):
    parte = parte[1:-1]
    parte = {x.split('=')[0]: int(x.split('=')[1]) for x in parte.split(',')}
    if es_aceptado(parte):
        ans += parte['x'] + parte['m'] + parte['a'] + parte['s']
print(ans)

# Parte 2

# Si comenzamos con un conjunto de partes con rango [lo,hi], ¿cuáles de esas partes siguen la regla op(n)?


def nuevo_rango(op, n, lo, hi):
    if op == '>':
        lo = max(lo, n+1)
    elif op == '<':
        hi = min(hi, n-1)
    elif op == '>=':
        lo = max(lo, n)
    elif op == '<=':
        hi = min(hi, n)
    else:
        assert False
    return (lo, hi)


def nuevos_rangos(var, op, n, xl, xh, ml, mh, al, ah, sl, sh):
    if var == 'x':
        xl, xh = nuevo_rango(op, n, xl, xh)
    elif var == 'm':
        ml, mh = nuevo_rango(op, n, ml, mh)
    elif var == 'a':
        al, ah = nuevo_rango(op, n, al, ah)
    elif var == 's':
        sl, sh = nuevo_rango(op, n, sl, sh)
    return (xl, xh, ml, mh, al, ah, sl, sh)


# x m a s
ans = 0
Q = deque([('in', 1, 4000, 1, 4000, 1, 4000, 1, 4000)])
while Q:
    estado, xl, xh, ml, mh, al, ah, sl, sh = Q.pop()
    if xl > xh or ml > mh or al > ah or sl > sh:
        continue
    if estado == 'A':
        score = (xh-xl+1)*(mh-ml+1)*(ah-al+1)*(sh-sl+1)
        ans += score
        continue
    elif estado == 'R':
        continue
    else:
        regla = R[estado]
        for cmd in regla.split(','):
            aplica = True
            res = cmd
            if ':' in cmd:
                cond, res = cmd.split(':')
                var = cond[0]
                op = cond[1]
                n = int(cond[2:])
                Q.append((res, *nuevos_rangos(
                    var, op, n, xl, xh, ml, mh, al, ah, sl, sh)))
                xl, xh, ml, mh, al, ah, sl, sh = nuevos_rangos(
                    var, '<=' if op == '>' else '>=', n, xl, xh, ml, mh, al, ah, sl, sh)
            else:
                Q.append((res, xl, xh, ml, mh, al, ah, sl, sh))
                break
print(ans)
