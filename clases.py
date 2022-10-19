import os
import sys
from sys import platform
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
    def __init__(self, opciones):
        # opciones debe ser un diccionario
        # opciones = { item : opción}
        self.opciones = opciones

    def mostrar(self):
        for item in self.opciones:
            print(f'{item}) {self.opciones[item]}')


    def cargar_archivo(self, nombre_archivo):
        datos_procesos = list()
        lista_temp = list()
        print(f'Abriendo fichero: "{nombre_archivo}"')
        with open(nombre_archivo, 'r') as fichero:
            # lectura del archivo como lista de strings quitando el salto de linea
            contenido = fichero.read().split('\n') # lista de string

        for elemento in contenido:
            lista_temp.append(elemento.strip('[]').split(','))
        
            
        for i in range(0, len(lista_temp)):
            elem_formateados = list()
            elem = lista_temp[i]
            for j in range(0, len(elem)):
                temp = elem[j]
                if temp.isdigit():
                    elem_formateados.append(int(temp))
                else:
                    try:
                        float(temp)
                        print('No se permiten números flotantes en los datos de los procesos.')
                        print('Verifique los datos en el archivo, deben respetar el formato establecido en la documentación.')
                        print('Una vez corrija el(los) error(es), vualva a ejecutar el programa.')
                        return exit()
                    except ValueError:
                        elem_formateados.append(temp)

            datos_procesos.append(elem_formateados)

        return datos_procesos

    def capturar(self):
        while True:
            try:
                opc = int(input('\n> '))
                if opc == 1:
                    pass
                elif opc == 2:
                    return self.cargar_archivo('procesos_precargados.txt')
                elif opc == 3:
                    encabezados = ['Autor', 'Rol']
                    autores = [
                        ['MASS Matias', ''],
                        ['ROMERO Sebastián',''],
                        ['SCHEFER Mauricio',''],
                        ['ZANAZZO M. Alan','']
                    ]
                    info = Tabla('', encabezados, autores)
                    print('Simulador de planificación de CPU y asignación de memoria')
                    print('Versión 1.0')
                    print('Sistemas Operativos')
                    print('Ingeniería en Sistemas de Información')
                    print('Universidad Tecnológica Nacional - Facultad Regional Resistencia')
                    info.construir()
                    return exit()
                else:
                    pass
            except ValueError:
                print('Debe ingresar una opción válida. Verifica que sea un número entero.')



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


class Memoria():
    def __init__(self, particiones):
        # 'particiones se pasa como lista, la cantidad de elementos es igual a cantidad de particiones
        # 'particiones' tiene el formato: [TAM_SO, TAM_PART_1, TAM_PART_2, ... TAM_PART_N]
        # al inicializar el atributo 'particiones' se modificará y luego contiene lista de instancias de clase Particion

        
        # validación
        for i in range(len(particiones)):
            if type(particiones[i]) != int:
                ventana_memo.limpiar()
                print('Los datos ingresados para crear particiones no son válidos. Sólo se permiten números enteros.')
                print(f'Error en el elemento: <{i}> {type(particiones[i])}')
                print('Corrija los errores y vuelva a ejecutar el programa.')
                sys.exit()
        
        # creando particiones
        lista_particiones = list()
        tam_memo = 0
        ult_dir = 0
        for i in range(len(particiones)):
            nueva_particion = Particion(id=i+1)
            if i != 0:
                dir_inicio = ult_dir
                nueva_particion.setDirInicio(dir_inicio)
            nueva_particion.setTam(particiones[i])
            # print('Se creó una partición nueva')
            # print(f'id = {nueva_particion.getId()}')
            # print(f'Dir de inicio = {nueva_particion.getDirInicio()}')
            # print(f'Tamaño = {nueva_particion.getTam()} KB')
            # print(f'Proceso asignado = {nueva_particion.getProcAsignado()}')
            # print(f'fragmentación = {nueva_particion.getFragmentacion()}\n')
            ult_dir += nueva_particion.getTam() + 1
            lista_particiones.append(nueva_particion)
        self.particiones = lista_particiones


    def getCantPart(self):
        return len(self.particiones)

    def getTam(self):
        tamanio = 0
        for part in self.particiones:
            tamanio += part.getTam()

        return tamanio



class Particion():
    def __init__(self, id=None, dirInicio=0, tam=None, procAsignado=None, fragmentacion=None):
        self.id = id
        self.dirInicio = dirInicio
        self.tam = tam
        self.procAsignado = procAsignado
        self.fragmentacion = fragmentacion

    #geters
    def getId(self):
        return self.id

    def getDirInicio(self):
        return self.dirInicio

    def getTam(self):
        return self.tam

    def getProcAsignado(self):
        return self.procAsignado

    def getFragmentacion(self):
        return self.fragmentacion
    
    #seters
    def setId(self, id):
        self.id = id

    def setDirInicio(self, dirInicio):
        self.dirInicio = dirInicio

    def setTam(self, tam):
        self.tam = tam

    def setProcAsignado(self, id_proceso):
        self.procAsignado = id_proceso

    def setFragmentacion(self, fragmentacion):
        self.fragmentacion = fragmentacion







