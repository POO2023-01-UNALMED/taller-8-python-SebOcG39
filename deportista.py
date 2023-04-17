class Deportista:
    def __init__(self, deporte, anosPracticando):
        self.__deporte = deporte
        self.__anosPracticando = anosPracticando

    def getDeporte(self):
        return self.__deporte
    
    def setDeporte(self, deporte):
        self.__deporte = deporte

    def getAnosPracticando(self):
        return self.__anosPracticando
    
    def setAnosPracticando(self,  anosPracticando):
        self.__anosPracticando = anosPracticando