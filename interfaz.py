import os
from clases import Consola, Menu, Proceso, Tabla



def validar(opcion):
    if opcion in OPCIONES_MENU:
        return True
    else:
        cmd.limpiar()
        print('Ingresá un opción válida. Intenta de nuevo...\n')
        return False


def carga_manual():
    lista_nuevos_procesos = list()
    valido = False
    seguir = True
    opciones_menu = {
        '1': ('Sí',''),
        '2': ('No','')
    }
    menu = Menu('',opciones_menu)
    cmd.limpiar()
    print('-'*COLUMNAS)
    mensaje = 'Tendrás que cargar los datos de cada proceso a continuación. Podés cargar N cantidad de procesos.\n'
    print(mensaje)
    print('-'*COLUMNAS)
    while seguir:
        nuevo_proceso = Proceso()
        print('Nuevo proceso\n')
        nuevo_proceso.id = input('ID: ')
        nuevo_proceso.ta = input('Tiempo de arribo: ')
        nuevo_proceso.ti = input('Tiempo de irrupción: ')
        nuevo_proceso.tam = input('Tamaño (KB): ')

        print('\nSe agregó el proceso correctametne.\n')

        lista_nuevos_procesos.append(nuevo_proceso)

        while not valido:
            print('¿Cargar otro proceso?')
            menu.mostrar()
            opcion = input('> ')
            valido = validar(opcion)
        
        if opcion == '1':
            valido = False
            cmd.limpiar()
        else:
            seguir = False

    return lista_nuevos_procesos
    

def presentar_datos(contenido):
    # contendio es el contenido de un archivo
    id_tabla = 'PLANIFICACIÓN DE PROCESOS'
    lista_datos = []
    
    # procesando datos, se obtiene lista de lista de las lineas tipo str del archivo
    for linea in contenido:    
        lista_datos.append(linea.strip('[]').split(','))

    # primer elemento es la lista de encabezados
    lista_encabezados = lista_datos.pop(0)
    

    mi_tabla = Tabla(id_tabla, lista_encabezados, lista_datos)
    mi_tabla.construir()


def cargar_archivo(nombre_fichero):
    cmd.limpiar()
    print(f'Abriendo fichero: "{nombre_fichero}"')
    with open('procesos_precargados.txt', 'r') as fichero:
        # lectura del archivo como lista de strings quitando el salto de linea
        contenido = fichero.read().split('\n')
        presentar_datos(contenido)
        cmd.pausa()

    print(f'Cerrando fichero: "{nombre_fichero}"')





#------------------------
#       ALGORITMO
#------------------------

COLUMNAS = 80
LINEAS = 20
TITULO_MENU = 'MENU'
OPCIONES_MENU = {
    '1': ('Cargar procesos manualmente ', 'carga_manual()'),
    '2': ('Cargar procesos desde un archivo', 'carga_automatica()'),
    '3': ('Salir del simulador', '')
}
valido = False

cmd = Consola()
cmd.formato(COLUMNAS,LINEAS)


menu = Menu(TITULO_MENU, OPCIONES_MENU)

while not valido:
    menu.mostrar()
    opcion = input('> ')
    valido = validar(opcion)


if opcion == '1':
    lista_nuevos_procesos = carga_manual()
    print('Se cargaron los siguientes procesos:')
    #print(lista_nuevos_procesos)
    for proceso in lista_nuevos_procesos:
        print(f'ID proceso: {proceso.id}')
elif opcion == '2':
    cargar_archivo('procesos_precargados.txt')
else:
    print('Cerrando...')


