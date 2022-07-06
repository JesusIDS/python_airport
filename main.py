from ClaseEmpleado import *

def abrir_archivo():
    archivo = open("Clientes.txt")
    datos = []
    for linea in archivo:
        datos.append(linea.strip("\n").split(","))
    archivo.close
    return datos

def peticion(datos):
    for n in datos:
        empleado = Empleado(n[0],n[1],n[2],n[3],n[4])
        print(empleado)


peticion(abrir_archivo())