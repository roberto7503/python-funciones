# Función para calcular el factorial de un número
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Captura de número por teclado
numero = int(input("Ingrese un número para calcular su factorial: "))

# Llamada a la función y muestra del resultado
print(f"El factorial de {numero} es {factorial(numero)}")