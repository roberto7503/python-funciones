#Escritura en un archivo nuevo: Diseña un programa que pida al usuario ingresar varias líneas de texto y guarde esas líneas en un archivo llamado “notas.txt”.
archivo_notas = "notas.txt"

while True:
    entrada = input("Escribe tu entrada (o escribe 'salir' para terminar): ")

    if entrada.lower() == "salir":
        print("Notas guadadas. Hasta la próxima.")
        break

    # Escribir la entrada en el archivo
    with open(archivo_notas, "a") as archivo:
        archivo.write(f"{entrada}\n")

    print("Entrada guardada.\n")