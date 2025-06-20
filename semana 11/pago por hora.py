# Programa para calcular el pago por horas trabajadas

def calcular_pago(horas_trabajadas):
    """
    Calcula el valor a pagar según las horas trabajadas.
    Las primeras 160 horas se pagan a $6.5 y el resto a $7.5.
    """
    tarifa_normal = 6.5
    tarifa_extra = 7.5
    horas_normales = min(horas_trabajadas, 160)
    horas_extras = max(horas_trabajadas - 160, 0)
    pago = (horas_normales * tarifa_normal) + (horas_extras * tarifa_extra)
    return pago

# Captura de datos por teclado
try:
    horas = float(input("Ingrese el número de horas trabajadas: "))
    if horas < 0:
        print("El número de horas no puede ser negativo.")
    else:
        total_pagar = calcular_pago(horas)
        print(f"El valor a pagar es: ${total_pagar:.2f}")
except ValueError:
    print("Por favor, ingrese un número válido de horas.")