
from operator import concat
from unidad import *

class ExceptionMonedas(Exception):
    pass

class MonedasNegativas(ExceptionMonedas):
    pass

class Jugador():
    "Un Jugador tiene un nombre, puntos_vida, monedas y unidades. Un jugador no puede deudas, es decir, no puede tener un numero de monedas negativo"

    def __init__(self, nombre, puntos_vida=20, monedas=0):
        self.nombre = nombre
        self.puntos_vida = puntos_vida
        self.unidades = []
        self.__monedas = monedas

    def descansar(self):
        """Hace que la primera unidad, si la hay, descanse"""
        pass

    def get_monedas(self):
        """Devuelve el numero de monedas actual del jugador"""
        return self.__monedas

    def set_monedas(self, value):
        """Modifica el numero de monedas por el valor value"""
        try:
            if value < 0:
                raise MonedasNegativas
            self.__monedas = value
        except MonedasNegativas:
            print('No se puede quedar en negativo')
