
from clases import *

OPCIONES_MENU ={
    '1':'Cargar procesos manualmente',
    '2':'Cargar procesos desde archivo',
    '3':'Acerca del Simulador',
    '4':'Salir'
}

if __name__ == '__main__':
    ventana = Consola()
    #ventana.limpiar()
    menu = Menu(OPCIONES_MENU)
    menu.mostrar()
    datos_procesos = menu.capturar()
    encabezados = datos_procesos.pop(0)
    tabla_planificacion = Tabla('1', encabezados, datos_procesos)
    ventana.limpiar()
    print('Planificación de procesos:')
    tabla_planificacion.construir()

    # Praparando memoria
    datos_particiones = [100,250,120,60]
    #print(f'Las particiones se crearán con los siguiente datos: {datos_particiones}\n\n')
    memo = Memoria(datos_particiones)
    #print(memo.particiones[0].getId())

    datos_particiones = list()

    for part in memo.getParticiones():
        particion = list()
        particion.append(part.getId())
        particion.append(part.getDirInicio())
        particion.append(part.getTam())
        datos_particiones.append(particion)

    encabezados = ['Num', 'Dir inicio', 'Tamaño (KB)']
    monitor_memo = Tabla('monitor_memo', encabezados, datos_particiones)
    print('\nDistribución de particiones en MP:')
    monitor_memo.construir()


    print('Cantidad de particiones: ', memo.getCantPart())
    print(f'Tamaño total de la memoria: {memo.getTam()} KB')

    ventana.esperar()
    ventana.limpiar()
    p_largo = LargoPlazo()
    p_largo.llamar(datos_procesos, memo)
