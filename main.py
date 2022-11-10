<<<<<<< HEAD

from clases import *

OPCIONES_MENU ={
    '1':'Cargar procesos manualmente',
    '2':'Cargar procesos desde archivo',
    '3':'Acerca del Simulador',
    '4':'Salir'
}

if __name__ == '__main__':
    ventana = Consola()
    ventana.limpiar()
    menu = Menu(OPCIONES_MENU)
    menu.mostrar()
    datos_procesos = menu.capturar()
    titulo = 'Planificación de procesos:'
    encabezados = datos_procesos.pop(0)
    tabla_planificacion = Tabla(titulo, encabezados, datos_procesos)
    ventana.limpiar()
    tabla_planificacion.construir()

    # Praparando memoria
    datos_particiones = [100,250,120,60]
<<<<<<< HEAD
    memo = Memoria(datos_particiones)

    datos_particiones = list()

    for part in memo.getParticiones():
        particion = list()
        particion.append(part.getId())
        particion.append(part.getDirInicio())
        particion.append(part.getTam())
        datos_particiones.append(particion)

    titulo = '\nDistribución de particiones en MP:'
    encabezados = ['Num', 'Dir inicio', 'Tamaño (KB)']
    monitor_memo = Tabla(titulo, encabezados, datos_particiones)
    monitor_memo.construir()

=======
from interfaz import *

#mauri
>>>>>>> 7137fcc79d475e0ac76a14cbc0447bd809c30a2b

    print('Cantidad de particiones: ', memo.getCantPart())
    print(f'Tamaño total de la memoria: {memo.getTam()} KB')
=======
    mmu = MMU(datos_particiones)
    mmu.getDistribucion()
>>>>>>> master

    ventana.esperar()
    ventana.limpiar()
    p_largo = LargoPlazo()
    p_largo.llamar(datos_procesos, mmu)
