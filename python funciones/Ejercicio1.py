archivo = input("Nombre del archivo (con .txt): ")

with open(archivo, 'a') as f:
    while True:
        frase = input("Escribe una frase (o 'SALIR' para terminar): ")
        if frase.upper() == 'SALIR':
            break
        f.write(frase + '\n')

print("Frases guardadas.")
