
from src.consola import Consola
from src.menu import Menu
from src.tabla import Tabla
from src.memoria import MMU
from src.PLP import LargoPlazo



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
    encabezados = ['ID', 'TA', 'TI', 'TAM']
    tabla_planificacion = Tabla(titulo, encabezados, datos_procesos)
    ventana.limpiar()
    tabla_planificacion.construir()

    # Praparando memoria
    datos_particiones = [100,250,120,60]
    mmu = MMU(datos_particiones)
    mmu.getDistribucion()

    ventana.esperar()
    ventana.limpiar()

    # Iniciando planificador a largo plazo
    PLP = LargoPlazo(mmu)
    PLP.ejecutar(datos_procesos)

    ventana.esperar()
    ventana.limpiar()
    print('Acá terminó la ejecución del PLP.')
    print('\nCola de nuevos: ', PLP.getNuevos())
    print('\nCola de admitidos: ', PLP.getAdmitidos())
    print('\nCola de listos: ', PLP.getListos())
