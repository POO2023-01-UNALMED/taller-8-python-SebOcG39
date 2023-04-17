from persona import Persona
from deportista import Deportista

class Futbolista(Persona, Deportista):
    listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self,nombre, edad, altura, sexo)
        Deportista.__init__(self,"Futbol", añosPracticando)
        self.__golesMarcados = golesMarcados
        self.__tarjetasRojas = tarjetasRojas
        self.__piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    def __str__(self):
        return f'Mi nombre es {super().getNombre()} soy profesional en el deporte {super().getDeporte()} Tengo {super().getEdad()} años de edad y llevo {super().getAñosPracticando()} años en el deporte'

    def getGolesMarcados(self):
        return self.__golesMarcados
    
    def setGolesMarcados(self, golesMarcados):
        self.__golesMarcados = golesMarcados

    def getTarjetasRojas(self):
        return self.__tarjetasRojas
    
    def setTarjetasRojas(self, tarjetasRojas):
        self.__tarjetasRojas = tarjetasRojas

    def getPiernaHabil(self):
        return self.__piernaHabil
    
    def setPiernaHabil(self, piernaHabil):
        self.__piernaHabil = piernaHabil