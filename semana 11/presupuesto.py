#Programa que muestra el presupuesto anual de una fabrica de cada departamenteo

def calcular_presupuesto_departamentos(monto_total):
    
    # Porcentajes asignados a cada departamento
    porcentajes = {
        "Recursos Humanos": 0.50,
        "Manufactura": 0.25,
        "Empaquetado": 0.15,
        "Publicidad": 0.10
    }

    # Cálculo del presupuesto para cada departamento
    presupuesto = {}
    for departamento, porcentaje in porcentajes.items():
        presupuesto[departamento] = monto_total * porcentaje

    return presupuesto

# Ejemplo de uso
monto_presupuesto = float(input("Ingrese el monto del presupuesto anual: $"))
resultados = calcular_presupuesto_departamentos(monto_presupuesto)

# Mostrar resultados
print("\nDistribución del presupuesto:")
for departamento, monto in resultados.items():
    print(f"{departamento}: ${monto:,.2f}")

