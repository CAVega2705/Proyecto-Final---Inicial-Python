
#El siguiente programa será una nómina de personal de una empresa que contenga la siguiente información:
#ID de empleado, Apellido, Nombre, Fecha de ingreso y Puesto de trabajo
#El propósito es tener una base de consulta.
#Se debe poder ingresar y consultar la información por consola

import csv, os

def cargar(id):
    if os.path.exists("nomina.csv") == True:
        csvfile = open('nomina.csv', 'r', newline='')
        empleados = list(csv.DictReader(csvfile))
        lista_id = []
        for persona in empleados:
            lista_id.append(persona['ID'])
            for i in range(len(lista_id)):
                lista_id[i] = int(lista_id[i])
        if id in (lista_id):
            print('El ID {} ingresado ya se encuentra asignado a otra persona.'.format(id))
            return
        else:
            print('Ingrese el apellido del nuevo ingresante:')
            apellido = str(input()).upper()
            print('Ingrese el nombre del nuevo ingresante:')
            nombre = str(input()).upper()
            print('Ingrese la fecha de ingreso del nuevo ingresante con el siguiente formato DD/MM/AAAA:')
            fecha = str(input())
            print('Ingrese el puesto del nuevo ingresante:')
            puesto = str(input()).upper()
            csvfile = open('nomina.csv', 'a', newline='')
            file_name = 'nomina.csv'
            header = ['ID', 'Apellido', 'Nombre', 'Fecha de ingreso', 'Puesto de trabajo']
            writer = csv.DictWriter(csvfile, fieldnames=header)
            fila = {}
            fila['ID'] = id
            fila['Apellido'] = apellido
            fila['Nombre'] = nombre
            fila['Fecha de ingreso'] = fecha
            fila['Puesto de trabajo'] = puesto
            writer.writerow(fila)

    else:
        csvfile = open('nomina.csv', 'a', newline='')
        print('Ingrese el apellido del nuevo ingresante:')
        apellido = str(input()).upper()
        print('Ingrese el nombre del nuevo ingresante:')
        nombre = str(input()).upper()
        print('Ingrese la fecha de ingreso del nuevo ingresante con el siguiente formato DD/MM/AAAA:')
        fecha = str(input())
        print('Ingrese el puesto del nuevo ingresante:')
        puesto = str(input()).upper()
        csvfile = open('nomina.csv', 'a', newline='')
        file_name = 'nomina.csv'
        header = ['ID', 'Apellido', 'Nombre', 'Fecha de ingreso', 'Puesto de trabajo']
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        fila = {}
        fila['ID'] = id
        fila['Apellido'] = apellido
        fila['Nombre'] = nombre
        fila['Fecha de ingreso'] = fecha
        fila['Puesto de trabajo'] = puesto
        writer.writerow(fila)
        csvfile.close()


def consultar(apellido):
    if os.path.exists("nomina.csv") == True:
        csvfile = open('nomina.csv', 'r', newline='')
        empleados = list(csv.DictReader(csvfile))
        lista_apellidos = []
        for persona in empleados:
            lista_apellidos.append(persona['Apellido'])
        while apellido in lista_apellidos:
            for i in range(len(empleados)):
                if empleados[i]['Apellido'] == apellido:
                    print(empleados[i]['ID'], empleados[i]['Apellido'], empleados[i]['Nombre'], empleados[i]['Fecha de ingreso'], empleados[i]['Puesto de trabajo'])
                    return
        else:
            print('El apellido ingresado no se encuentra en la nómina')

    else:
        print('No existen empleados en la nómina')
        return



#MAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAIN
#MAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAIN
#MAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAINMAIN

if __name__ == '__main__':
    print('Bienvenido al programa de gestión de personal')
    print('Por favor, ingrese su nombre para iniciar el sistema:')
    usuario = str(input())

       
    while True:
        print('Hola {}, indique a continuación que acción desea realizar:'.format(usuario))
        print('Cargar datos nuevos: 1, Consultar nómina: 2, Finalizar el programa: 3')
        funcion = int(input())
        if funcion == 1:
            print('Ingrese el numero de id del nuevo ingresante:')
            id = int(input())
            cargar(id)
        elif funcion == 2:
            print('Ingrese el apellido del empleado:')
            apellido = str(input()).upper()
            consultar(apellido)
        elif funcion == 3:
            break
        else:
            print('La opción ingresada es incorrecta, por favor ingresela nuevamente.')

quit()