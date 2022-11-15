class Proceso(object):
    def __init__(self, id=None, ta=None, ti=None, tam=None, est=None, ubi=None):
        self.__id = id    #identificador de proceso
        self.__ta = ta    #tiempo de arribo a cola de listos
        self.__ti = ti    #tiempo de irrupción en CPU
        self.__tam = tam  #tamaño de proceso en KB
        self.__est = est  #estado E=ejecutándose / L=listo / B=bloqueado / LS=listo-suspendido / BS=bloqueado-suspendido
        self.__ubi = ubi  #ubicación M = Memoria, D = Disco

    def getId(self):
        return self.__id

    def getTa(self):
        return self.__ta

    def getTi(self):
        return self.__ti

    def getTam(self):
        return self.__tam

    def getEst(self):
        return self.__est

    def setUbi(self):
        return self.__ubi

    def setId(self, id):
        self.__id = id

    def setTa(self, ta):
        self.__ta = ta

    def setTi(self, ti):
        self.__ti = ti

    def setTam(self, tam):
        self.__tam = tam

    def setEst(self, estado):
        self.__est = estado

    def setUbi(self, ubi):
        self.__ubi = ubi

    def __str__(self):
        salida = f'[ID={self.__id}, TA={self.__ta}, TI={self.__ti}, TAM={self.__tam} KB]\n'
        return salida


    def __repr__(self):
        return f'\n[ID={self.__id}, \tTA={self.__ta}, \tTI={self.__ti}, \tTAM={self.__tam} KB, \tEST={self.__est}]'

