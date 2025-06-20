# Proyecto 3: Cálculo de salarios con descuento de renta

def calcular_descuento(salario):
    """Calcula el descuento de renta (10%) sobre el salario"""
    return salario * 0.10

def main():
    empleados = int(input("Ingrese la cantidad de empleados: "))
    for i in range(1, empleados + 1):
        salario = float(input(f"Ingrese el salario del empleado {i}: "))
        descuento = calcular_descuento(salario)
        salario_neto = salario - descuento
        print(f"Empleado {i}: Salario bruto = ${salario:.2f}, Descuento renta = ${descuento:.2f}, Salario neto = ${salario_neto:.2f}")

if _name_ == "_main_":
    main()