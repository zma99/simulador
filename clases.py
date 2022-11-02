import os
import sys
from sys import platform
from turtle import pos
from tabulate import tabulate # Es necesario instalar


class Consola():
    #falta definir
    def __init__(self, columnas=800):
        #self.formato(columnas)
        pass

    
    def limpiar(self):
        os.system('cls')

    def esperar(self):
        os.system('pause')
        
    def formato(self, columnas):
        #self.__init__(columnas, lineas)
        self.limpiar()
        os.system('TITLE Simulador')
        os.system(f'MODE con:cols={columnas}')

    

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

        # formatea lista de string en lista de listas
        for elemento in contenido:
            lista_temp.append(elemento.strip('[]').split(','))
        
        # Validación de datos de procesos
        # devuelve lista de lista con datos de procesos (datos_procesos)
        
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
                        sys.exit()
                    except ValueError:
                        if i==0:
                            elem_formateados.append(temp)
                        else:
                            sys.exit('\nRevise los datos de los procesos, deben ser números enteros para TA, TI y TAM.\n\nSaliendo...')

            datos_procesos.append(elem_formateados)

        # Control de procesos con ID repetidos
        lista_id = list()
        for proc in datos_procesos:
            # Se guardan ID's tmeporalmente para control
            lista_id.append(proc[0])

        for proc in datos_procesos:
            # Compara por cada proceso si su ID se repite
            if lista_id.count(proc[0]) > 1:
                print()
                sys.exit('Hay procesos con el mismo ID en el archivo')

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

    def getUbi(self):
        return self.__ubi

    def __str__(self):
        return str(self.__id)



class Cpu():
    def __init__(self, reloj):
        self.reloj = reloj

    def getReloj(self):
        return self.reloj


class Memoria():
    # Representa memoria principal de un sistema de cómputo

    def __init__(self, particiones):
        # 'particiones se pasa como lista, la cantidad de elementos es igual a cantidad de particiones
        # 'particiones' tiene el formato: [TAM_SO, TAM_PART_1, TAM_PART_2, ... TAM_PART_N]
        # al inicializar el atributo 'particiones' se modificará y luego contiene lista de instancias de clase Particion

        
        # validación
        for i in range(len(particiones)):
            if type(particiones[i]) != int:
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


    def worstfit(self, lista_procesos):
        # Recibe lista de procesos para asignar a particiones libres
        # Utiliza el criterio: "peor partición en la que cabe (el proceso)"
        part = self.partLibreMayor()
        if not part is None:
            part.setProcAsignado(lista_procesos.pop(0).getId())


    def libre(self):
        # Retorna una lista booleanos indicando si la partición está libre
        # cada posición de la lista corresponde a una partición en el orden que 
        # fueron creadas
        part_libre = list()
        for part in self.particiones:
            part_libre.append(part.libre())

        return part_libre


    def partLibreMayor(self):
        # Retorna el objetivo Particion de mayor tamaño que está libre
        # Contrario devuelve None
        mayorTam = 0
        for part in self.particiones:
            if part.libre() and part.getTam() > mayorTam:
                mayorTam = part.getTam()
                partMayor = part
            else: 
                partMayor = None
        
        return partMayor


class Particion():
    # Representa un objeto de tipo partición de memoria

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


    def libre(self):
        # si la partición no tiene asignado un proceso retorna True = Libre
        # contrario retorna False
        if self.procAsignado is None:
            return True

        return False





class LargoPlazo():
    def __init__(self, multiprog=5):
        self.multiprog = multiprog

    def getMultiprog(self):
        return self.multiprog




    def admitirProcesos(self, lista_procesos, memoria):
        # Recibe una lista de listas de procesos y memoria sobre la que va a trabajar,
        # Cada elemento de la lista tiene formato [ID,TA,TI,TAM]
        asignados = 0
        while len(lista_procesos) > 0:
            if memoria.libre():
                while asignados < self.getMultiprog():
                    try:
                        memoria.worstfit(lista_procesos)
                        print('Proceso asignado')
                        asignados += 1
                    except ValueError:
                        print('ALGO SALIO MAL EN LA ASIGANACIPON DE MEMORIA')
                sys.exit('\nMEMORIA LLENA\n\nSaliendo...')



        
    def llamar(self, datos_procesos, memoria):
        # Ejecuta el planificador de SO a largo plazo
        # Toma los datos procesos validados y crea una instancia de Proceso
        # por cada uno, luego asigna a particiones disponibles

        lista_procesos = list()
        while True:
            if not datos_procesos is None:
                for proc in datos_procesos:
                    nuevo_proc = Proceso(
                        proc[0], # ID
                        proc[1], # TA
                        proc[2], # TI
                        proc[3]  # TAM
                    )
                    lista_procesos.append(nuevo_proc)
                self.admitirProcesos(lista_procesos, memoria)
            sys.exit('No hay procesos para tratar.\nSaliendo...')              




class CortoPlazo():
    def __init__(self):
        pass

    def get(self):
        pass

    def SJF(self, lista):
        pass

    def dispatcher(self):
        pass
