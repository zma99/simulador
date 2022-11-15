import sys
from .proceso import Proceso
from .lista import list


class LargoPlazo(object):
    def __init__(self, mmu):
        self.__multiprog = 5        # nivel de multiprogramación del sistema
        self.__tiTotal = 0          # tiempo de irrupción total
        self.__mmu = mmu            # módulo controlador de memoria
        self.__nuevos = list()      # lista o cola de procesos nuevos que ingresan al sistema
        self.__listos = list()      # lista o cola de procesos admitidos y cargados en memorias
        self.__admitidos = list()   # lista o cola de procesos admitidos en el sistema

    def getAdmitidosEn(self, ubi):
        pass

    def getMultiprog(self):
        return self.__multiprog
    
    def getTiTotal(self):
        return self.__tiTotal

    def getMMU(self):
        return self.__mmu

    def getNuevos(self):
        return self.__nuevos

    def getListos(self):
        return self.__listos

    def getAdmitidos(self):
        return self.__admitidos

    def setMultiprog(self, multiprog):
        self.__multiprog = multiprog

    def setTiTotal(self):
        for proceso in self.__nuevos:
            self.__tiTotal += proceso.getTi()

    def setMMU(self, MMU):
        self.__mmu = MMU

    def setListos(self, lista_procesos):
        self.__listos = lista_procesos

    def setAdmitidos(self, lista_procesos):
        self.__admitidos = lista_procesos

    def setNuevos(self, lista_procesos):
        self.__nuevos = lista_procesos

    def addNuevos(self, proceso):
        self.__nuevos.append(proceso)

    def addListos(self, proceso):
        self.__listos.append(proceso)

    def addAdmitidos(self, proceso):
        self.__admitidos.append(proceso)

    def cantAdmitidos(self):
        return len(self.__admitidos)

    def ejecutar(self, datos_procesos):
        # Ejecuta el planificador de SO a largo plazo
        # Toma los datos procesos validados y crea una instancia de Proceso
        # por cada uno, luego asigna a particiones disponibles

        while True:
            if not datos_procesos is None:
                self.crearListaProcesos(datos_procesos)
                self.setTiTotal()
                print('\nTiempo de irrupción total: ', self.getTiTotal())
                # Se ordena por tiempo de arribo (TA)
                #print('Cola de nuevo sin ordenar:', self.__nuevos)
                self.__nuevos.ordenar('TA')
                # print('Cola de nuevo ordenada:', self.__nuevos)
                # os.system('pause')
                self.admitirProcesos()
                break
            sys.exit('No hay procesos para tratar.\nSaliendo...')    



    def crearListaProcesos(self, datos_procesos):
        # Devuelve una lista de instancias de Proceso()
        
        #nuevos = list()
        for datos in datos_procesos:
            self.__nuevos.append(self.nuevoProceso(datos))

    def nuevoProceso(self, datos):
        # Crea y retorna una instancia de la clase Proceso

        nuevo_proc = Proceso(
            datos[0], # ID
            datos[1], # TA
            datos[2], # TI
            datos[3]  # TAM
        )
        return nuevo_proc

    def ingresanProc(self):
        if len(self.__nuevos) > 0:
            return True
        else:
            return False
        

    
    def admitirProcesos(self):
        # Recibe una lista de listas de procesos y memoria sobre la que va a trabajar,
        # Cada elemento de la lista tiene formato [ID,TA,TI,TAM]


        while self.ingresanProc() and self.cantAdmitidos() < self.__multiprog:
            proceso = self.__nuevos.pop(0)  # Se toma un proceso de la cola de nuevos
            if self.__mmu.memoriaLibre():   # Se consulta si hay memoria disponible
                # Si hay memoria el mmu se encarga
                try:
                    if self.__mmu.worstfit(proceso): 
                        self.__listos.append(proceso)
                except ValueError:
                    print('Algo salió mal en la admisión del proceso')
            else:
                # Sino no hay memoria el proceso se suspende (pasa a disco)
                proceso.setEst('S')

            self.__admitidos.append(proceso)    # Se agrega el proceso a cola de admitidos



        # admitidos = 0
        # while len(self.__nuevos) > 0:
        #     while admitidos < self.getMultiprog():
        #         while self.__mmu.memorialibre():
        #             try:
        #                 self.__mmu.worstfit(nuevos)
        #                 admitidos = self.__mmu.cantProcAsignados()
        #             except ValueError:
        #                 print('ALGO SALIO MAL EN LA ASIGANACIPON DE MEMORIA')
                
        #     self.__listos = self.__mmu.procAsignados()
        #     print('Cola de listos:', self.__listos)
        #     sys.exit('\nMEMORIA LLENA\n\nSaliendo...')
         

    def verificar(self, reloj):
        for proceso in self.__nuevos:
            if proceso.getTa() == reloj:
                #self.admitirProcesos()
                return True

        return False

    def admitir(self):
        pass