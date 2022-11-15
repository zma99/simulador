import sys
from .tabla import Tabla

class MMU(object):
    def __init__(self, datos_particiones):
        self.__memo = Memoria(datos_particiones)

    def getParticiones(self):
        return self.__memo.getParticiones()

    def getDistribucion(self):
        datos_particiones = list()
        for part in self.getParticiones():
            particion = list()
            particion.append(part.getId())
            particion.append(part.getDirInicio())
            particion.append(part.getTam())
            datos_particiones.append(particion)

        titulo = '\nDistribución de particiones en MP:'
        encabezados = ['Num', 'Dir inicio', 'Tamaño (KB)']
        monitor_memo = Tabla(titulo, encabezados, datos_particiones)
        monitor_memo.construir()
        print('Cantidad de particiones: ', self.getCantPart())
        print(f'Tamaño total de la memoria: {self.getTam()} KB')

    def getCantPart(self):
        return self.__memo.getCantPart()

    def getTam(self):
        return self.__memo.getTam()

    def memoriaLibre(self):
        return self.__memo.libre()

    def worstfit(self, nuevos):
        return self.__memo.worstfit(nuevos)

    def procAsignados(self):
        # retorna lista con id de procesos asignados a las particiones
        # partición: [SO, p1, p2, p3] -> devuelve [id_proc_1,  id_proc_2, id_proc_3]
        # si todas las partición son ocupadas por procesos excepto la partición SO
        return self.__memo.procAsignados()

    def mostrarMemoria(self, datos_particiones):
        titulo = '\nMemoria Principal:'
        encabezados = ['ID Part', 'Direccion', 'Tamaño (KB)', 'ID Proc', 'Fragmentacion']
        monitor_memoria = Tabla(titulo, encabezados, datos_particiones)
        monitor_memoria.construir()

    def cantProcAsignados(self):
        return len(self.procAsignados())

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


    def worstfit(self, proceso):
        # Recibe lista de procesos para asignar a particiones libres
        # Utiliza el criterio: "peor partición en la que cabe (el proceso)"
        part = self.partLibreMayor()
        if part != 0 and proceso.getTam() <= part.getTam() :
            part.setProcAsignado(proceso.getId())
            print('Proceso asignado')
            proceso.setEst('L')
            return True
        else:
            print('Proceso Admitido')
            proceso.setEst('S')
        return False
            


    def libre(self):
        # Retorna True si hay memoria disponible, de lo contrario False
    
        part_libre = list()
        for part in self.__particiones:
            # Crea una lista de booleanos indicando si la partición está libre
            # cada posición de la lista corresponde a una partición en el orden que fueron creadas
            part_libre.append(part.libre())

        if part_libre.count(True) > 0:
            # Si hay al menos un elemento =True en part_libre
            # significa que hay partición libre
            # por tanto hay memoria disponible
            return True

        return False


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
        #
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

