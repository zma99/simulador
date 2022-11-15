# REDEFINICON DE CLASES PYTHON


class list(list):
    def __init__(self):
        super().__init__(self)

    def ordenar(self, criterio):
        if criterio.upper() == 'TA':
            self.sort(key=lambda x : x.getTa())
        if criterio.upper() == 'TI':
            self.sort(key=lambda x : x.getTi())


    





