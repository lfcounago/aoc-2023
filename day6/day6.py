import sys


def calculate_ways(time, distance):
    ways = 0
    for i in range(time + 1):
        if i * (time - i) > distance:
            ways += 1
    return ways


def calcular_p1(input_file):
    total_ways = 1
    with open(input_file, 'r') as file:
        lines = file.readlines()
        times = [int(x) for x in lines[0].split(':')[1].split()]
        distances = [int(x) for x in lines[1].split(':')[1].split()]
        races = list(zip(times, distances))
    for time, distance in races:
        total_ways *= calculate_ways(time, distance)
    return total_ways


def calcular_p2(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        time = int(''.join(lines[0].split(':')[1].split()))
        distance = int(''.join(lines[1].split(':')[1].split()))
    return calculate_ways(time, distance)


def main():
    nombre_archivo = sys.argv[1]
    p1 = calcular_p1(nombre_archivo)
    p2 = calcular_p2(nombre_archivo)
    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
