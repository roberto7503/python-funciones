# Función que recibe tres números reales y devuelve el menor de ellos
def menor_de_tres(a, b, c):
    # Utilizamos la función min para encontrar el menor valor
    return min(a, b, c)

# Ejemplo de uso
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))

# Llamamos a la función y mostramos el resultado
menor = menor_de_tres(num1, num2, num3)
print(f"El menor de los tres números es: {menor}")