#Ejemplificando archivos de texto en python
#Creando el archivo datos.txt
arch1=open("datos.txt","w", encoding="utf-8") #Modo escritura
arch1.write("Priera línea \n")
arch1.write("Segunda línea \n")
arch1.write("Tercera línea \n")
arch1.close()
print("Fin del programa")
