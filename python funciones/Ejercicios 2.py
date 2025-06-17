nombre_archivo = input("Ingrese el nombre del archivo (ej: poema.txt): ")
try:
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        print(f"El archivo tiene {len(lineas)} líneas.")
except FileNotFoundError:
    print("Error: El archivo no se encontró.")
