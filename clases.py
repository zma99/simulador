import os
import sys
from sys import platform
from tabulate import tabulate # Es necesario instalar


class list(list):
    def __init__(self):
        super().__init__(self)

    def ordenar(self, criterio):
        if criterio.upper() == 'TA':
            self.sort(key=lambda x : x.getTa())
        if criterio.upper() == 'TI':
            self.sort(key=lambda x : x.getTi())


class Simulador():
    def __init__(self):
        self.__reloj = 0

    def mainloop(self):
        # cuerpo principal del programa
        while True:
            break

    def cargar(self):
        # carga de archivo y carga manual
        pass

    def refrescar(self):
        # para actualizar interfaz
        pass

    def contar(self):
        self.__reloj += 1


class Consola():
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


class Menu(): 
    def __init__(self, opciones):
        # opciones debe ser un diccionario
        # opciones = { item : opción}
        self.opciones = opciones

    def mostrar(self):
        for item in self.opciones:
            print(f'{item}) {self.opciones[item]}')


    def cargaManual(self):
        # Devuelve lista con datos de procesos

        datos_procesos = self.pedirDatos()

        print(datos_procesos)

        os.system('pause')
        

        return datos_procesos


    def pedirDatos(self):
        datos_procesos = list()
        datos_procesos.append(['ID','TA','TI','TAM (KB)'])

        print('Ingrese datos del proceso. Recuerde que deben ser números eneteros. Ingrese -1 en cualquier momento para salir.\n')
        while True:
            id = self.ingresarDato('ID')
            ta = self.ingresarDato('TA')
            ti = self.ingresarDato('TI')
            tam = self.ingresarDato('TAM')
            datos_procesos.append([id,ta,ti,tam])
            print('\nIngrese "s" para seguir cargando procesos o cualquier otra tecla para finlizar.')
            seguir = input('> ')
            if seguir != 's':
                break

        return datos_procesos


                    
            
    def ingresarDato(self, nom_dato):
        nom_dato = nom_dato.upper()
        dato = 0
        if nom_dato != 'TAM':
            while True:
                dato = input(nom_dato + ' = ')
                if self.validarEntero(dato):
                    dato = int(dato)
                    return dato
                print('\nIntente de nuevo...\n') 
        else:
            while True:
                dato = input(nom_dato + ' = ')
                if self.validarTam(dato):
                    dato = int(dato)
                    return dato
                print('\nIntente de nuevo...\n')

            
    
    
    def validarEntero(self, dato):
        if dato == '-1':
            sys.exit('Saliendo...')
        if not dato.isdigit() or dato == 0:
            return False
        return True

    def validarTam(self, tam):
        while True:
            if tam == '-1':
                sys.exit('Saliendo...')

            if not tam.isdigit() or tam == 0:
                return False
            
            tam = int(tam)
            if tam > 250:
                print('\nEl tamaño del proceso no puede exceder de 250 KB.\n')
                return False
            
            return True


    def cargarArchivo(self, nombre_archivo):
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
        
        for i in range(1, len(lista_temp)):
            elem_formateados = list()
            elem = lista_temp[i]
            for j in range(0, len(elem)):
                temp = elem[j]
                if i == 0 or temp.isdigit():
                    elem_formateados.append(int(temp))
                else:
                    sys.exit('\nRevise los datos de los procesos, deben ser números enteros para ID, TA, TI y TAM.\n\nSaliendo...')

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

        for i in range(1, len(datos_procesos)):
            tam_proc = datos_procesos[i][3]
            if int(tam_proc) > 250:
                sys.exit('\nERROR: Hay al menos un proceso de tamaño mayor a 250 KB y no es posible tratar. \n\nCorrija e intente de nuevo.')

        return datos_procesos

    def capturar(self):
        while True:
            try:
                opc = int(input('\n> '))
                if opc == 1:
                    return self.cargaManual()
                elif opc == 2:
                    return self.cargarArchivo('procesos_precargados.txt')
                elif opc == 3:
                    self.autores()
                else:
                    pass
            except ValueError:
                print('Debe ingresar una opción válida. Verifica que sea un número entero.')

    def autores(self):
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


class Tabla():
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
        return f'\n id de proceso {self.__id} Tiempo de Arribo {self.__ta} Tiempo de irrupcion {self.__ti} Tamaño {self.__tam} '

    


class Cpu():
    def __init__(self, reloj):
        self.__reloj = reloj

    def getReloj(self):
        return self.__reloj

    def setReloj(self, reloj):
        self.__reloj = reloj


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
        ult_dir = 0
        for i in range(len(particiones)):
            nueva_particion = Particion(id=i+1)
            if i != 0:
                dir_inicio = ult_dir
                nueva_particion.setDirInicio(dir_inicio)
            nueva_particion.setTam(particiones[i])
            
            if i == 0:
                nueva_particion.setSO(True)
                
            ult_dir += nueva_particion.getTam() + 1
            lista_particiones.append(nueva_particion)
        self.__particiones = lista_particiones

    
    def getParticiones(self):
        return self.__particiones


    def getCantPart(self):
        return len(self.__particiones)

    def getTam(self):
        tamanio = 0
        for part in self.__particiones:
            tamanio += part.getTam()

        return tamanio


    def worstfit(self, lista_procesos):
        # Recibe lista de procesos para asignar a particiones libres
        # Utiliza el criterio: "peor partición en la que cabe (el proceso)"
        part = self.partLibreMayor()
        if part != 0 and len(lista_procesos) != 0:
            part.setProcAsignado(lista_procesos.pop(0).getId())
            print('Proceso asignado')
            return True
        
        return False
            


    def libre(self):
        # Retorna una lista booleanos indicando si la partición está libre
        # cada posición de la lista corresponde a una partición en el orden que 
        # fueron creadas
        part_libre = list()
        for part in self.__particiones:
            part_libre.append(part.libre())

        return part_libre


    def partLibreMayor(self):
        # Retorna el objetivo Particion de mayor tamaño que está libre
        # Contrario devuelve None
        mayorTam = 0
        partMayor = 0
        for part in self.__particiones:
            if part.libre() and part.getTam() > mayorTam:
                mayorTam = part.getTam()
                partMayor = part
                #os.system('pause')
        
        return partMayor


    def procAsignados(self):
        # Retorna lista con ID de procesos asignados a una partición

        listos = list()
        for part in self.__particiones:
            if not part.getSO():
                listos.append(part.getProcAsignado())

        return listos


class Particion():
    # Representa un objeto de tipo partición de memoria

    def __init__(self, id=None, dirInicio=0, tam=None, procAsignado=None, fragmentacion=None, so=False):
        self.__id = id
        self.__dirInicio = dirInicio
        self.__tam = tam
        self.__procAsignado = procAsignado
        self.__fragmentacion = fragmentacion
        self.__so = so

    #geters
    def getId(self):
        return self.__id

    def getDirInicio(self):
        return self.__dirInicio

    def getTam(self):
        return self.__tam

    def getProcAsignado(self):
        return self.__procAsignado

    def getFragmentacion(self):
        return self.__fragmentacion

    def getSO(self):
        return self.__so
    
    #seters
    def setId(self, id):
        self.__id = id

    def setDirInicio(self, dirInicio):
        self.__dirInicio = dirInicio

    def setTam(self, tam):
        self.__tam = tam

    def setProcAsignado(self, id_proceso):
        self.__procAsignado = id_proceso

    def setFragmentacion(self, fragmentacion):
        self.__fragmentacion = fragmentacion

    def setSO(self, so):
        self.__so = so


    def libre(self):
        # si la partición no tiene asignado un proceso retorna True = Libre
        # contrario retorna False
        if not self.__so and self.__procAsignado is None:
            return True

        return False


class LargoPlazo():
    def __init__(self, multiprog=5):
        self.__multiprog = multiprog
        self.__tiTotal = 0
        listos = list()
        suspendidos = list()

    def getMultiprog(self):
        return self.__multiprog
    
    def llamar(self, datos_procesos, memoria):
        # Ejecuta el planificador de SO a largo plazo
        # Toma los datos procesos validados y crea una instancia de Proceso
        # por cada uno, luego asigna a particiones disponibles

        lista_procesos = list()
        while True:
            if not datos_procesos is None:
                lista_procesos = self.crearListaProcesos(datos_procesos)
                self.setTiTotal(lista_procesos)
                print('\nTiempo de irrupción total: ',self.getTiTotal())
                self.admitirProcesos(lista_procesos, memoria)
            sys.exit('No hay procesos para tratar.\nSaliendo...')    



    def crearListaProcesos(self, datos_procesos):
        # Devuelve una lista de instancias de Proceso()
        
        lista_procesos = list()
        for datos in datos_procesos:
            lista_procesos.append(self.nuevoProceso(datos))
        
        return lista_procesos

    def nuevoProceso(self, datos):
        # Crea y retorna una instancia de la clase Proceso

        nuevo_proc = Proceso(
            datos[0], # ID
            datos[1], # TA
            datos[2], # TI
            datos[3]  # TAM
        )
        return nuevo_proc

    
    def admitirProcesos(self, lista_procesos, memoria):
        # Recibe una lista de listas de procesos y memoria sobre la que va a trabajar,
        # Cada elemento de la lista tiene formato [ID,TA,TI,TAM]

        # Se ordena por tiempo de arribo (TA)
        #lista_procesos = sorted(lista_procesos, key=lambda proceso : proceso.getTa())
        #print(lista_procesos)
        lista_procesos.ordenar('TA')
        #print(lista_procesos)

        #sys.exit('...')

        asignados = 0
        while len(lista_procesos) > 0:
            if memoria.libre():
                while asignados < self.getMultiprog():
                    try:
                        memoria.worstfit(lista_procesos)
                        asignados += 1
                    except ValueError:
                        print('ALGO SALIO MAL EN LA ASIGANACIPON DE MEMORIA')
                print('Cola de listos:', memoria.procAsignados())
                sys.exit('\nMEMORIA LLENA\n\nSaliendo...')
         

    def setTiTotal(self, lista_procesos):
        for proceso in lista_procesos:
            self.__tiTotal += proceso.getTi()
    
    def getTiTotal(self):
        return self.__tiTotal


class CortoPlazo():
    def __init__(self):
        pass

    def get(self):
        pass

    def SJF(self, lista):
        pass

    def dispatcher(self):
        pass
