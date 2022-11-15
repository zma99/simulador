import os
from sys import platform


class Consola(object):
    #falta definir
    def __init__(self, columnas=800):
        #self.formato(columnas)
        pass

    
    def limpiar(self):
        if platform == 'win32':
            os.system('cls')
        else:
            os.system('clear')

    def esperar(self):
        os.system('pause')
        
    def formato(self, columnas):
        #self.__init__(columnas, lineas)
        self.limpiar()
        os.system('TITLE Simulador')
        os.system(f'MODE con:cols={columnas}')

    def monitor(self):
        pass

