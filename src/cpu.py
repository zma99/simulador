class Cpu(object):
    def __init__(self, id):
        self.__id = id
        self.__proceso = None
        self.__ti = 0

    def getId(self):
        return self.__id

    def getProceso(self):
        return self.__proceso

    def getTi(self):
        return self.__ti

    def setId(self, id):
        self.__id = id

    def setProceso(self, proceso):
        self.__proceso = proceso

    def setTi(self, ti):
        self.__ti = ti

    def ejecutar(self, proceso):
        self.__proceso = proceso
        self.__ti = proceso.getTi()
        print(f'EJECTUANDO PROCESO: {self.__proceso}\n')
        while self.__ti != 0:
            print('TI actual: ', self.__ti)
            self.__ti -= 1

        print('*'*30)
        print('\nFIN DE LA EJECUCIÓN')


