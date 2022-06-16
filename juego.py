import os
from jugador import Jugador
from unidad import Soldado, Arquero, Caballero
import sys

N_VIDAS = 20
MONEDAS_TURNO = 10
BONUS_DANO = 1.5


class Juego():

    def __init__(self, nombre_jugador1, nombre_jugador2):
        """Creadora"""
        self.jugador1 = Jugador(nombre=nombre_jugador1,
                                puntos_vida=20)
        self.jugador2 = Jugador(nombre=nombre_jugador2,
                                puntos_vida=20)

    @staticmethod
    def _elegir_opcion(options):
        """Muestra por pantalla la lista de opciones enumeradas y retorna el número de opción elegida.
         options es una lista de strings"""
        print("Elige una opción:")
        for idx, element in enumerate(options):
            print("{}) {}".format(idx + 1, element))
        i = input("Introduce un número: ")
        try:
            if 0 < int(i) <= len(options):
                return int(i)
        except:
            pass
        return None

    def _turno(self, jugador):
        f"""Se le añaden {MONEDAS_TURNO} al jugador, se le muestran las opciones de compra hasta que decida finalizar el turno"""
        jugador.set_monedas(jugador.get_monedas() + 10)
        options = ["Terminar aplicación", "Finalizar turno",
                   "Comprar soldado:\n    coste: 5 puntos_ataque: 3 puntos_vida: 10",
                   "Comprar arquero:\n    coste: 6 puntos_ataque: 8 puntos_vida: 10",
                   "Comprar caballero:\n    coste: 9 puntos_ataque: 5 puntos_vida: 10"]
        while True:
            print("Jugador:", jugador.nombre)
            print("Puntos de vida:", jugador.puntos_vida)
            print("Monedas:", jugador.get_monedas())
            print("Unidades:")
            for i in range(len(jugador.unidades)): print("%s%s" % (i+1, "."), type(jugador.unidades[i]).__name__)
            print()

            selection = self._elegir_opcion(options)
            if selection == 1:
                raise SystemExit
            elif selection == 2:
                break
            else:
                if selection == 3:
                    if jugador.get_monedas() - 5 >= 0: jugador.unidades.append(Soldado())
                    jugador.set_monedas(jugador.get_monedas() - 5)
                if selection == 4:
                    if jugador.get_monedas() - 6 >= 0: jugador.unidades.append(Arquero())
                    jugador.set_monedas(jugador.get_monedas() - 6)
                if selection == 5:
                    if jugador.get_monedas() - 9 >= 0: jugador.unidades.append(Caballero())
                    jugador.set_monedas(jugador.get_monedas() - 9)

    def _finalizar(self, jugador_ganador):
        """Finaliza la partida mostrando como ganador al jugador_ganador"""
        self._clear_screen()

        print(f"""FIN DEL JUEGO
El jugador ganador es {jugador_ganador.nombre}""")
        quit()

    @staticmethod
    def _clear_screen():
        if (os.name == 'posix'):
            os.system('clear')
        # else screen will be cleared for windows
        else:
            os.system('cls')
            pass

    def loop(self):
        "Loop del juego, se ejecuta hasta finalizar la partida"
        ronda = 0
        while (True):
            ronda += 1
            self._turno(self.jugador1)
            self._clear_screen()
            self._turno(self.jugador2)
            self._batalla()

            # limitación para permitir tests de funcionalidad sin implementación
            if ronda == 100:
                break
        raise SystemExit()

    def _daño_al_jugador(self, defensor, atacante):
        """
        El defensor recibe un ataque de cada unidad del atacante, si el defensor se queda sin
        puntos de vida, llama a la función _finalizar.
        """
        for unidad in atacante.unidades:
            defensor.puntos_vida -= unidad.atacar()
        if defensor.puntos_vida <= 0:
            self._finalizar(atacante)

    @staticmethod
    def _calcular_bonus(atacante, defensor):
        """Devuelve el bonus de ataque que tiene el atacante contra el defensor, se debe usar
         la función isinstace(instancia, clase) para implementarla"""
        atacante = type(atacante).__name__
        defensor = type(defensor).__name__
        if atacante == "Soldado" and defensor == "Arquero" or atacante == "Arquero" and defensor == "Caballero" or atacante == "Caballero" and defensor == "Soldado":
            return 1.5
        elif atacante == "Arquero" and defensor == "Soldado" or atacante == "Caballero" and defensor == "Caballero":
            return 1

    def _batalla(self):
        """Realiza una batalla entre las unidades del jugador1 y el jugador2. 
        La batalla se desarrolla en combates 1 vs 1, siempre entre las unidades más antiguas de cada jugador.
        Durante un combate, las dos unidades pierdan tantos puntos de vida como puntos de ataque tenga la unidad adversaria.
        Si una unidad sobrevive a un combate, ésta participará en el siguiente combate, la batalla continua mientras ambos jugadores
         tengan unidades disponibles. 
        Cuando a un jugador no le queden más unidades, recibe un ataque de cada unidad enemiga remaniente.
        Al acabar, los jugadores hacen descansar a sus unidades.
        """
        ultima_unidad = None
        check_unidad = -1
        while True:
            if len(self.jugador2.unidades) == 0 or len(self.jugador1.unidades) == 0:
                break

            puntos_ataque_jugador1 = self.jugador1.unidades[0].atacar()
            puntos_ataque_jugador2 = self.jugador2.unidades[0].atacar()

            self.jugador1.unidades[0].puntos_vida -= puntos_ataque_jugador2
            self.jugador2.unidades[0].puntos_vida -= puntos_ataque_jugador1
            check_unidad = self.__check_unidades(self.jugador1.unidades[0], self.jugador2.unidades[0])

            if self.jugador2.unidades[0].puntos_vida <= 0:
                if len(self.jugador1.unidades) == 1 and self.jugador1.unidades[0].puntos_vida <= 0:
                    if check_unidad == 2:
                        ultima_unidad = self.jugador2.unidades[0]
                self.jugador2.unidades.pop(0)

            if self.jugador1.unidades[0].puntos_vida <= 0:
                if len(self.jugador2.unidades) == 0:
                    if check_unidad == 1:
                        ultima_unidad = self.jugador1.unidades[0]
                self.jugador1.unidades.pop(0)

        if len(self.jugador2.unidades) == 0 and len(self.jugador1.unidades) != 0 or check_unidad == 1 and ultima_unidad:
            if len(self.jugador1.unidades) == 0:
                puntos_ataque_jugador1 = ultima_unidad.atacar()
                print(type(ultima_unidad).__name__)
                self.jugador2.puntos_vida -= puntos_ataque_jugador1
            else:
                self._daño_al_jugador(self.jugador2, self.jugador1)
            if len(self.jugador1.unidades) != 0: self.jugador1.unidades[0].descansar()

        if len(self.jugador1.unidades) == 0 and len(self.jugador2.unidades) != 0 or check_unidad == 2 and ultima_unidad:
            if len(self.jugador2.unidades) == 0:
                puntos_ataque_jugador2 = ultima_unidad.atacar()
                self.jugador1.puntos_vida -= puntos_ataque_jugador2
            else:
                self._daño_al_jugador(self.jugador1, self.jugador2)
            if len(self.jugador2.unidades) != 0: self.jugador2.unidades[0].descansar()

    def __check_unidades(self, unidad1, unidad2):
        jugador1_unidad_tipo = type(unidad1).__name__
        jugador2_unidad_tipo = type(unidad2).__name__

        if jugador1_unidad_tipo == jugador2_unidad_tipo:
            return -1
        elif jugador1_unidad_tipo == "Soldado" and jugador2_unidad_tipo == "Arquero" or jugador1_unidad_tipo == "Arquero" and jugador2_unidad_tipo == "Caballero" or jugador1_unidad_tipo == "Caballero" and jugador2_unidad_tipo == "Soldado":
            return 1
        else:
            return 2

    @classmethod
    def mensaje_bienvenida(self):
        print(f"""
Bienvenido a ObjectWars
Este juego es un juego para dos jugadores. Lo que un jugador realiza durante su turno es secreto, por lo que el otro jugador no debe mirar las acciones que realize el otro \
jugador durante su turno.

El objectivo del juego es dejar el enemigo sin puntos de vida, al empezar cada jugador dispone de {N_VIDAS}.

Durante un turno el jugador puede comprar unidades.

Al empejar un turno cada jugador recibe {MONEDAS_TURNO} mondedas.

Despues de que ambos jugadores acaben sus turnos sus unidades entraran en combate. Si un jugador no tiene unidades, o son derrotadas, recibirá el daño en sus puntos de vida.

Existen tres tipologias de unidades: soldados, arqueros y caballeros. Las unidades tienen un bonus de {BONUS_DANO} de daño siguiendo la siguiente jerarquía:
soldado -> arquero -> caballero -> soldado


    
    """)


if __name__ == "__main__":
    Juego.mensaje_bienvenida()
    nombre1 = input("Introduce el nombre del jugador1: ")
    nombre2 = input("Introduce el nombre del jugador2: ")
    juego = Juego(nombre1, nombre2)
    juego.loop()
