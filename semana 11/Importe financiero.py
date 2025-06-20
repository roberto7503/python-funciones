# Programa para calcular el importe final de una compra aplicando descuentos

def calcular_importe_final(importe):
    """
    Calcula el importe final aplicando descuentos según el importe de la compra.
    - 5% de descuento para compras mayores a 300 €
    - 10% de descuento para compras mayores a 500 €
    - 12% de descuento para compras mayores a 1000 €
    """
    if importe > 1000:
        descuento = 0.12
    elif importe > 500:
        descuento = 0.10
    elif importe > 300:
        descuento = 0.05
    else:
        descuento = 0.0
    importe_final = importe * (1 - descuento)
    return importe_final

# Solicitar al usuario el importe de la compra
importe = float(input("Introduce el importe de la compra (€): "))

# Calcular el importe final a pagar
importe_a_pagar = calcular_importe_final(importe)

# Mostrar el resultado al usuario
print(f"El importe final a pagar es: {importe_a_pagar:.2f} €")