#Lectura de un archivo de texto línea a línea
arch1=open("datos.txt","r")
linea=arch1.readline()
while linea!="":
    print(linea, end="")
    linea=arch1.readline()
arch1.close()
