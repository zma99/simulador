
from src.consola import Consola
from src.menu import Menu
from src.tabla import Tabla
from src.memoria import MMU
from src.PLP import LargoPlazo
from src.PCP import CortoPlazo
from src.PMP import MedioPlazo
from src.cpu import Cpu



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
    ventana.esperar()

    # Iniciando planificador a corto plazo
    ventana.limpiar()
    cpu = Cpu(1)
    cola_espera = PLP.getListos()
    PCP = CortoPlazo(cpu, cola_espera)
    
    PMP = MedioPlazo(mmu)
    
    ti_total = PLP.getTiTotal()
    reloj = 0
    PCP.ejectuar()
    while reloj != ti_total:
        print('RELOJ = ', reloj)
        if PLP.verificar(reloj):  # Verifica si se puede admitir nuevo proceso
            PLP.admitir()
            PMP.setSuspendidos(PLP.getAdmitidosEstado('S'))
            procesoAdmitido = PMP.swap()
            if not procesoAdmitido is None:
                PLP.addListos(procesoAdmitido)
            

          # ordena cola de espera (listos), utiliza dispatcher y asigna proceso a cpu
        PCP.getCpu().ejecutar()    # El cpu ejecutar proceso = ti-1

        if PCP.getCpu().getTi() == 0:   # Consulta si el proceso actualmente en cpu terminó la ejecución
            print('\nLiberando CPU\n')
            ventana.esperar()
            proceso = PCP.getCpu().getProceso()
            mmu.liberarParticion(proceso)
            proceso.setEst('T')
            PCP.getCpu().liberar()
            PCP.setEsperando(PLP.getListos())   # Renueva cola de espera por si hubo cambios
            print(f'TERMINÓ EL PROCESO: {proceso}')
            PCP.ejectuar()
        
        ventana.monitor()   # Muestra actualizaciones por pantalla



        ventana.esperar()
        reloj += 1  # Incrementa reloj

 