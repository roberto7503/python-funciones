import math

# Programa para calcular el área de un círculo dado su radio


def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    :param radio: Radio del círculo (float o int)
    :return: Área del círculo (float)
    """
    return math.pi * radio ** 2

# Ejemplo de uso
radio = float(input("Ingrese el radio del círculo: "))
area = area_circulo(radio)
print(f"El área del círculo de radio {radio} es: {area:.2f}")