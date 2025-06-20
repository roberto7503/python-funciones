# Programa para calcular las comisiones y sueldos totales de vendedores

# Función que calcula la comisión del 10% de tres ventas
def calcular_comision(venta1, venta2, venta3):
    total_ventas = venta1 + venta2 + venta3
    comision = total_ventas * 0.10
    return comision

# Pedimos cuántos vendedores hay
n = int(input("Ingrese el número de vendedores: "))

# Recorremos cada vendedor
for i in range(1, n + 1):
    print(f"\nVendedor {i}:")
    sueldo_base = float(input("Ingrese el sueldo base: $"))
    
    # Ingresar las tres ventas
    venta1 = float(input("Ingrese el valor de la primera venta: $"))
    venta2 = float(input("Ingrese el valor de la segunda venta: $"))
    venta3 = float(input("Ingrese el valor de la tercera venta: $"))
    
    #Calculamos la comisión con la función
    comision = calcular_comision(venta1, venta2, venta3)
    
    #Calculamos el sueldo total
    sueldo_total = sueldo_base + comision

    # Mostramos los resultados
    print(f"Comisión por las 3 ventas: ${comision:.2f}")
    print(f"Sueldo total (base + comisión): ${sueldo_total:.2f}")
