# Programa: Tabla de multiplicar de un número entero

def imprimir_tabla_multiplicar(numero):
    """
    Imprime la tabla de multiplicar del 1 al 10 para el número dado.
    """
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# Solicitar al usuario un número entero
num = int(input("Introduce un número entero: "))

# Llamar a la función para imprimir la tabla
imprimir_tabla_multiplicar(num)