from src.lista import list

class CortoPlazo(object):

    def __init__(self, cpu=None, cola_espera=list()):
        self.__cpu = cpu
        self.__esperando = cola_espera

        if self.__cpu is None:
            print('ATENCIÓN: No hay CPU para trabajar, se presentarán errores durante la ejecución.')

        if self.__esperando == []:
            print('ATENCIÓN: No hay procesos en cola de espera.')

    def getCpu(self):
        return self.__cpu

    def getEsperando(self):
        return self.__esperando

    def setCpu(self, id_cpu):
        self.__cpu = id_cpu

    def setEsperando(self, lista_procesos):
        self.__esperando = lista_procesos

    def SJF(self):
        self.__esperando.ordenar('TI')

    def dispatcher(self):
        self.__cpu.asignar(self.__esperando.pop(0))
        

    def ejectuar(self):
        self.SJF()
        self.dispatcher()
        
        

    

        