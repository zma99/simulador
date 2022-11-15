from tabulate import tabulate # Es necesario instalar


class Tabla(object):
    def __init__(self, titulo, encabezados, datos):
        self.__titulo = titulo                # titulo a mostrar
        self.__encabezados = encabezados      # list of strings: [ 'fila 1 col 1', 'fila 1 col 2', ... , 'fila 1 col N' ]
        self.__datos = datos                  # list of list: [ [datos fila 1], [ datos fila dos ], ... , [datos fila N] ]

    def getTitulo(self):
        return self.__titulo

    def getEncabezados(self):
        return self.__encabezados

    def getDatos(self):
        return self.__datos

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setEncabezados(self, lista_encabezados):
        self.__encabezados = lista_encabezados

    def setDatos(self, lista_datos):
        self.__datos = lista_datos


    def construir(self):
        # 'tabulate' permite imprimir datos en formato de tabla muy fácil
        print(self.__titulo)
        print(tabulate(self.__datos, headers=self.__encabezados, tablefmt='fancy_grid'))

