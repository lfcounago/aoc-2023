import sys

print("Inicio del programa")

suma_digitos = 0
suma_letras = 0
digito = 0
num_letras = ['one', 'two', 'three', 'four',
              'five', 'six', 'seven', 'eight', 'nine']
file = open(sys.argv[1]).read().strip()

for linea in file.split('\n'):
    numeros = []
    letras = []
    for i, digito in enumerate(linea):
        if digito.isdigit():
            numeros.append(digito)
            letras.append(digito)
        for j, letra in enumerate(num_letras):
            if linea[i:].startswith(letra):
                letras.append(str(j + 1))

    primer_numero = numeros[0]
    ultimo_numero = numeros[-1]

    primera_letra = letras[0]
    ultima_letra = letras[-1]

    digito = int(primer_numero + ultimo_numero)
    letra = int(primera_letra + ultima_letra)

    suma_digitos += digito
    suma_letras += letra

print("Ejercicio 1: ", suma_digitos)
print("Ejercicio 2: ", suma_letras)

print("Fin del programa")
