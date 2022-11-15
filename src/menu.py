import os, sys
from .tabla import Tabla

class Menu(object): 
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

        # print(datos_procesos)
        # os.system('pause')
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
                elif opc == 4:
                    sys.exit('Saliendo...')
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

