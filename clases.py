import os
from tabulate import tabulate # Es necesario instalar


class Consola():
    #falta definir
    def __init__(self, columnas=0, lineas=0):
        self.columnas = columnas
        self.lineas = lineas
    
    def limpiar(self):
        os.system('cls')

    def pausa(self):
        os.system('pause')
        
    def formato(self, columnas, lineas):
        self.__init__(columnas, lineas)
        self.limpiar()
        os.system('TITLE Simulador')
        os.system(f'MODE con:cols={columnas} lines={lineas}')
        #os.system('pause')

    


class Menu():
    def __init__(self, mensaje, opciones):
        self.mensaje = mensaje   
        self.opciones = opciones # diccionario

    def mostrar(self):
        print(self.mensaje)

        for clave in self.opciones:
            print(f'{clave}) {self.opciones[clave][0]}')


class Tabla():
    def __init__(self, id, encabezados, datos):
        self.id = id                        # un identificador
        self.encabezados = encabezados      # list of strings: [ 'fila 1 col 1', 'fila 1 col 2', ... , 'fila 1 col N' ]
        self.datos = datos                  # list of list: [ [datos fila 1], [ datos fila dos ], ... , [datos fila N] ]

    def construir(self):
        # 'tabulate' permite imprimir datos en formato de tabla muy fácil
        print(tabulate(self.datos, headers=self.encabezados, tablefmt='fancy_grid'))



class Proceso():
    def __init__(self, id=None, ta=None, ti=None, tam=None): # ta=tiempo arribo, ti=tiempo irrumpción, tam=tamaño
        self.id = id
        self.ta = ta
        self.ti = ti
        self.tam = tam





class Particion():
    pass