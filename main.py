
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
    mmu = MMU(datos_particiones)
    mmu.getDistribucion()

    ventana.esperar()
    ventana.limpiar()
    p_largo = LargoPlazo()
    p_largo.llamar(datos_procesos, mmu)
