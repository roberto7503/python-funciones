#Archivo de texto en una lista
arch1=open("datos.txt","r")
lineas=arch1.readlines() 
print("El archivo tiene",len lineas,"lineas")
print("El contenido el archivo")
for linea in lineas:
    print(linea, end="")

