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
    def __init__(self, coste = 5, puntos_ataque=3, restaura_descansar=5):
        super().__init__(self)

        self.coste=coste
        self.restaura_descansar=restaura_descansar
        self.__puntos_ataque=puntos_ataque

    def descansar(self):
        pass

    def atacar(self):
        pass

    def __getattr__(self, name: str):
        value = self.__dict__.get(name)
        if not value:
            raise AttributeError(f'{name} no es un atributo válido.')
        return value

class Arquero(Unidad):
    """ Unidad Arquero, tiene un coste de 6 monedas, tiene 8 puntos de ataque y restaura 2 puntos de vida al decansar
    Los arqueros atacan 1 de cada 2 veces ya que deben recargar, empiezan la partida sin estar preparados para atacar"""
    def __init__(self, coste = 6, puntos_ataque=8, restaura_descansar=2, puede_atacar=False):
        self.coste=coste
        self.restaura_descansar=restaura_descansar
        self.puede_atacar = puede_atacar
        self.__puntos_ataque=puntos_ataque

    def descansar(self):
        pass

    def atacar(self):
        return self.__puntos_ataque

    def __getattr__(self, name: str):
        value = self.__dict__.get(name)
        if not value:
            raise AttributeError(f'{name} no es un atributo válido.')
        return value

class Caballero(Unidad):
    """ Unidad Caballero, tiene un coste de 9 monedas, tiene 5 puntos de ataque, y al descansar no restaura puntos de vida"""
    def __init__(self, coste = 9, puntos_ataque=5, restaura_descansar=0):
        super().__init__(self)
        self.coste=coste
        self.restaura_descansar=restaura_descansar
        self.__puntos_ataque=puntos_ataque

    def descansar(self):
        pass

    def atacar(self):
        pass

    def __getattr__(self, name: str):
        value = self.__dict__.get(name)
        if not value:
            raise AttributeError(f'{name} no es un atributo válido.')
        return value

