class CortoPlazo(object):

    def __init__(self):
        pass

    def get(self):
        pass

    def SJF(self, lista):
        pass

    def dispatcher(self):
        pass

    def algoritmoSRTF(self):
        global cpu, listos
        self.ordenarPorSJF() 
        if not (cpu.proceso): #Agregamos el primer proceso de la cola de listos a la cpu si no hay en la cpu
            if len(listos) >= 1:
                cpu.agregarProceso(listos[0])
                listos.pop(0)
        else:
            if len(listos) >= 1: #Si existe aunque sea un elemento de la cola de listos
                if listos[0].getTI() < cpu.getProceso().getTI() - cpu.getTIactual(): #Nos fijamos si alguno tiene el tiempo de irrupción menor que lo que le falta al proceso para finalizar ejecutándose en el procesador
                    self.dispatcher(listos[0])
                        
    def dispatcher(self, proceso):
        global listos
        cpu.proceso.asignarTI(cpu.getProceso().getTI() - cpu.getTIactual())
        listos.append(cpu.getProceso())
        cpu.agregarProceso(proceso)
        listos.pop(0)

    def ordenarPorSJF(self):
        global listos
        listos.sort(key=lambda proceso: proceso.getTI(), reverse=False)

    def quitarProcDeMem(self, idProceso):
        global part1, part2, part3
        if idProceso == part1.getIdProc():
            part1.liberar()
        if idProceso == part2.getIdProc():
            part2.liberar()
        if idProceso == part3.getIdProc():
            part3.liberar()
        print ("\t\t\t\t *** El proceso", idProceso, "sale de memoria ***")

        