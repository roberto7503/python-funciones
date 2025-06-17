#Solicitarr datos al usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
salario = input("Ingrese su salario: ")

#Formatear los datos en una linea
linea=f"{nombre},{apellido},{edad},{salario}\n"

#Guardar los datos en un archivo
with open("datos_usuarios.txt","a") as archivo:
    archivo.write(linea)
    
print("Datos guardados correctamente en ´datos_usuarios.txt´")

