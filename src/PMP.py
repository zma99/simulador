from src.lista import list

class MedioPlazo(object):
    def __init__(self):
        self.__suspendidos = list()

    def swapping(self):
        pass

    def getSuspendidos(self):
        return self.__suspendidos

    def setSuspendidos(self, lista_procesos):
        self.__suspendidos = lista_procesos
