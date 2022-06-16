
from operator import concat
from unidad import *

class ExceptionMonedas(Exception):
    pass

class MonedasNegativas(ExceptionMonedas):
    pass

class Jugador():
    "Un Jugador tiene un nombre, puntos_vida, monedas y unidades. Un jugador no puede deudas, es decir, no puede tener un numero de monedas negativo"

    def __init__(self, nombre, puntos_vida=20, monedas=0):
        self.__nombre = nombre
        self.__puntos_vida = puntos_vida
        self.__unidades = []
        self.__monedas = monedas

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def unidades(self):
        return self.__unidades

    @unidades.setter
    def unidades(self, unidades):
        self.__unidades = unidades

    @property
    def puntos_vida(self):
        return self.__puntos_vida

    @puntos_vida.setter
    def puntos_vida(self, puntos_vida):
        self.__puntos_vida = puntos_vida

    def descansar(self):
        """Hace que la primera unidad, si la hay, descanse"""
        if len(self.unidades) > 0:
            self.unidades[0].descansar()

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
            print('No dispones de suficiente dinero')
