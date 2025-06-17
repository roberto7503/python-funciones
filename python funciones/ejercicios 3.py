# Paso 1: Abrir el archivo en modo escritura
with open("compras.txt", "w") as archivo:
    print("Introduce los productos de tu lista de compras.")
    print("Escribe 'fin' para terminar.")

    # Paso 2: Bucle infinito
    while True:
        # Paso 3: Solicitar al usuario un producto
        producto = input("Producto: ")

        # Paso 4: Verificar si es 'fin'
        if producto.lower() == "fin":
            break

        # Paso 5: Escribir el producto en el archivo
        archivo.write(producto + "\n")

# Paso 6: Notificar al usuario
print("La lista de compras ha sido guardada en 'compras.txt'.")
