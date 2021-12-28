
#El siguiente programa será una nómina de personal de una empresa que contenga la siguiente información:
#ID de empleado, Apellido, Nombre, Fecha de ingreso y Puesto de trabajo
#El propósito es tener una base de consulta.
#Se debe poder ingresar, modificar y consultar la información por consola

import datetime
from os import close, write
import random
import csv
import os


def cargar(empleados):
    csvfile = open('nomina.csv', 'w')
    
    print('Ingrese el numero de id del nuevo ingresante:')
    empleados = []
    id = int(input())
    if id in empleados:
        print('El ID ingresado ya se encuentra asignado a otra persona.')
    else:
        empleados.append(id)
    print('Ingrese el apellido del nuevo ingresante:')
    apellido = str(input()).upper
    empleados.append(apellido)
    print('Ingrese el nombre del nuevo ingresante:')
    nombre = str(input()).upper
    empleados.append(nombre)
    print('Ingrese la fecha de ingreso del nuevo ingresante con el siguiente formato DD/MM/AAAA:')
    fecha = str(input())
    empleados.append(fecha)
    print('Ingrese el puesto del nuevo ingresante:')
    puesto = str(input()).upper
    empleados.append(puesto)


    csvfile = open('nomina.csv')
    file_name = 'nomina.csv'
    header = ['ID', 'Apellido', 'Nombre', 'Fecha de ingreso', 'Antigüedad', 'Puesto de trabajo']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    fila = {}
    fila['ID'] = id
    fila['Apellido'] = apellido
    fila['Nombre'] = nombre
    fila['Fecha de ingreso'] = fecha
    fila['Puesto de trabajo'] = puesto


def modificar(empleados):
    archivo = open('nomina.csv', 'r+')
    empleados = {}
    print('Ingrese el numero de id del empleado:')
    id = int(input())
    while True:
        if id in empleados:
                print('ingrese el valor que desea modificar: "apellido", "nombre", "fecha de ingreso" o "puesto"')
                valor = str(input).lower
                for id in empleados:
                    if valor == 'apellido':
                        print('Ingrese el nuevo apellido:')
                        apellido = str(input()).upper
                    elif valor == 'nombre':
                        print('Ingrese el nuevo nombre:')
                        nombre = str(input()).upper
                    elif valor == 'fecha de ingreso':
                        fecha = str(input())
                    elif valor == 'puesto':
                        print('Ingrese el nuevo puesto:')
                        puesto = str(input()).upper          
                    else:
                        print('La opción ingresada es incorrecta, ingresela nuevamente.')
                else:
                    print('El ID ingresado es incorrecto, por favor ingreselo nuevamente:')        
                
        for k, v in empleados:
            header = ['ID', 'Apellido', 'Nombre', 'Fecha de ingreso', 'Antigüedad', 'Puesto de trabajo']        
            writer = csv.DictWriter(fieldnames=header)
            fila = {}
            fila['ID'] = id
            fila['Apellido'] = apellido
            fila['Nombre'] = nombre
            fila['Fecha de ingreso'] = fecha
            fila['Puesto de trabajo'] = puesto



def consultar(empleados):
    archivo = open('nomina.csv', 'r')
    print('Ingrese el ID de la persona que desea consultar:')
    id = int(input)
    while id in empleados:
        for id in empleados:
            for k, v in empleados:
                print(v, k)




#MAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAIN
#MAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAIN
#MAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAIN

if __name__ == '__main__':
    print('Bienvenido al programa de gestión de personal')
    print('Por favor, ingrese su nombre para iniciar el sistema:')
    usuario = str(input())
    print('Hola {}, indique a continuación que acción desea realizar:'.format(usuario))
    print('Cargar datos nuevos: 1, Modificar datos existentes: 2, Consultar información: 3, Finalizar el programa: 4')
       
    while True:
        funcion = int(input())
        funcion == 1 or 2 or 3 or 4
        if funcion == 1:
            empleados = {}
            cargar(empleados)
            break
        if funcion == 2:
            empleados = {}
            modificar(empleados)
            break
        elif funcion == 3:
            empleados = {}
            consultar(empleados)
            break
        elif funcion == 4:
            break
        else:
            print('La opción ingresada es incorrecta, por favor ingresela nuevamente.')

quit()