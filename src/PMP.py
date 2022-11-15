from src.lista import list

class MedioPlazo(object):
    def __init__(self, mmu):
        self.__suspendidos = list()
        self.__mmu = mmu

    def swap(self):
        if self.__mmu.memoriaLibre():
            self.__suspendidos.ordenar('TI')
            #print(f'Cola de suspendidos {self.__suspendidos}')
            for proceso in self.__suspendidos:
                #print('Estamos en el for de swap()')
                if self.__mmu.worstfit(proceso):
                    #print('ahora en el if para asignacion por worsfit')
                    return proceso
                
        return None


    def getSuspendidos(self):
        return self.__suspendidos

    def setSuspendidos(self, lista_procesos):
        self.__suspendidos = lista_procesos
