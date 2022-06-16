from abc import ABC, abstractmethod

MAX_VIDA = 10


class Unidad(ABC):
    """Clase abstracta que modela una unidad"""

    def __init__(self):
        """Creadora del objecto Unidad"""

    @abstractmethod
    def descansar(self):
        """ Metodo abastracto, restaura puntos de vida a la unidad"""
        pass

    @abstractmethod
    def atacar(self):
        """Este metodo debe ser usado para consultar los puntos de ataque, en caso de que la unidad este atacando"""
        pass

    @abstractmethod
    def __getattr__(self, name: str):
        """Devuelve si el atributo coincide con el que se le pasa"""
        pass


class Soldado(Unidad):
    """Unidad soldado, tiene un coste de 5 monedas, tiene 3 puntos de ataque y restaura 5 puntos de vida al descansar"""
    def __init__(self, puntos_ataque=3, puntos_vida=10, coste = 5, restaura_descansar = 5):
        super().__init__(self)
        self.__puntos_ataque = puntos_ataque
        self.__puntos_vida = puntos_vida
        self.__coste = coste
        self.__restuara_descansar = restaura_descansar

    @property
    def puntos_vida(self):
        return self.__puntos_vida

    @puntos_vida.setter
    def puntos_vida(self, puntos_vida):
        self.__puntos_vida = puntos_vida

    @property
    def puntos_ataque(self):
        return self.__puntos_ataque

    @puntos_ataque.setter
    def puntos_ataque(self, puntos_ataque):
        self.__puntos_ataque = puntos_ataque

    def descansar(self):
        if self.__puntos_vida + 5 > self.__puntos_vida:
            self.__puntos_vida = 10
        else:
            self.__puntos_vida += 5

    def atacar(self):
        return self.__puntos_ataque

    def __getattr__(self, name: str):
        value = self.__dict__.get(name)
        if not value:
            raise AttributeError(f'{name} no es un atributo válido.')
        return value

class Arquero(Unidad):
    """ Unidad Arquero, tiene un coste de 6 monedas, tiene 8 puntos de ataque y restaura 2 puntos de vida al decansar
    Los arqueros atacan 1 de cada 2 veces ya que deben recargar, empiezan la partida sin estar preparados para atacar"""
    def __init__(self, coste = 6, puntos_ataque=8, restaura_descansar=2, puntos_vida=10, puede_atacar=False):
        super().__init__(self)
        self.__coste=coste
        self.__restaura_descansar=restaura_descansar
        self.__puede_atacar = puede_atacar
        self.__puntos_ataque = puntos_ataque
        self.__puntos_vida = puntos_vida

    @property
    def puntos_vida(self):
        return self.__puntos_vida

    @puntos_vida.setter
    def puntos_vida(self, puntos_vida):
        self.__puntos_vida = puntos_vida

    def descansar(self):
        self.__puntos_vida += self.__restaura_descansar

    def atacar(self):
        self.__puntos_ataque = 8 if self.__puntos_ataque == 0 else 0
        return self.__puntos_ataque

    def __getattr__(self, name: str):
        value = self.__dict__.get(name)
        if not value:
            raise AttributeError(f'{name} no es un atributo válido.')
        return value

class Caballero(Unidad):
    """ Unidad Caballero, tiene un coste de 9 monedas, tiene 5 puntos de ataque, y al descansar no restaura puntos de vida"""
    def __init__(self, coste = 9, puntos_ataque = 5, puntos_vida = 10, restaura_descansar = 0):
        super().__init__(self)
        self.__coste=coste
        self.__restaura_descansar=restaura_descansar
        self.__puntos_ataque = puntos_ataque
        self.__puntos_vida = puntos_vida

    @property
    def puntos_vida(self):
        return self.__puntos_vida

    @puntos_vida.setter
    def puntos_vida(self, puntos_vida):
        self.__puntos_vida = puntos_vida

    def descansar(self):
        pass

    def atacar(self):
        return self.__puntos_ataque

    def __getattr__(self, name: str):
        value = self.__dict__.get(name)
        if not value:
            raise AttributeError(f'{name} no es un atributo válido.')
        return value

