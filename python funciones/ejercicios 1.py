import datetime

# Nombre del archivo donde se guardará el diario
archivo_diario = "mi_diario.txt"

while True:
    entrada = input("Escribe tu entrada (o escribe 'salir' para terminar): ")

    if entrada.lower() == "salir":
        print("Diario guardado. Hasta la próxima.")
        break

    # Obtener la fecha y hora actual
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Escribir la entrada en el archivo
    with open(archivo_diario, "a") as archivo:
        archivo.write(f"[{fecha_hora}] {entrada}\n")
    
    print("Entrada guardada.\n")