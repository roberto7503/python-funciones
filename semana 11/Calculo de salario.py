# Programa: Cálculo de salarios y descuento de renta para empleados

def calcular_descuento(salario):
    """
    Calcula el descuento de renta (10%) sobre el salario.
    """
    return salario * 0.10

# Solicitar la cantidad de empleados
cantidad_empleados = int(input("Ingrese la cantidad de empleados: "))

# Procesar cada empleado
for i in range(1, cantidad_empleados + 1):
    salario = float(input(f"Ingrese el salario del empleado {i}: "))
    descuento = calcular_descuento(salario)
    total_pagar = salario - descuento
    print(f"Empleado {i}:")
    print(f"  Salario bruto: ${salario:.2f}")
    print(f"  Descuento de renta (10%): ${descuento:.2f}")
    print(f"  Total a pagar: ${total_pagar:.2f}\n")