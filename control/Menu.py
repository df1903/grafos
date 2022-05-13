"""——————————————————————————————————————————————
    Menú con métodos funcionales por consola.
——————————————————————————————————————————————"""
# import sys, time, random
# from data.Grafo import *
# from helpers import


class Menu:

    """—————————————————————————————————————————————CONSTRUCTOR——————————————————————————————————————————————————————"""

    def __init__(self):
        self.name = 'Grafito'
        self.grafo = Grafo()
        self.lista_vertices = self.grafo.get_lista_vertices()
        self.lista_aristas = self.grafo.get_lista_aristas()

    """—————————————————————————————————————————————SALIDA-PANTALLA——————————————————————————————————————————————————"""

    def menu_inicio(self):
        """
        Inicio en selección de opciones.
        :return: salir será la salida estándar.
        """
        print('▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜\n' \
              '▌▓▒░     01. Iniciar     ░▒▓█▓▒░     02. Opciones     ░▒▓█▓▒░     03. Salir     ░▒▓▐\n' \
              '▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟')

        o = {
            1: self.ejecutar, 2: self.menu_opciones, 3: self.salir
        }
#        i = Helpers.read_int("Ingrese una opción: ", "Opción inválida.", 1, 3)
#        o[i]()

    def menu_opciones(self):
        print(
            "\nOPCIONES"
            "\n01 — Run Time!            02 — Ingresar vértice     03 — Ver vértices         04 — ¿Hay pozos?"
            "\n05 — Generar vértice      06 — Ingresar arista      07 — Ver aristas          08 — ¿Hay fuentes?"
            "\n09 — Generar arista       10 — ∙∙∙                  11 — ∙∙∙                  12 — ∙∙∙"
            "\n13 — ¿Hay pozos?          14 — ¿Hay fuentes?        15 — Prom. peso Aristas   16 — ∙∙∙"
            "\n13 — ¿Hay pozos?          14 — ¿Hay fuentes?        15 — ∙∙∙                  16 — ∙∙∙"
            "\n13 — ¿Hay pozos?          14 — ¿Hay fuentes?        15 — ∙∙∙                  16 — ∙∙∙"
            "\n13 — ¿Hay pozos?          14 — ¿Hay fuentes?        15 — ∙∙∙                  16 — ∙∙∙"
            # ∙∙∙
            "\n00 — Volver"
        )
        o = {
            1: self.ejecutar,          2: self.ingresar_vertice,  3: self.mostrar_vertices,  4: self.hay_pozos,
            5: self.generar_vertice,   6: self.ingresar_aristas,  7: self.mostrar_aristas,   8: self.hay_fuentes,
            9: self.default,          10: self.default,          11: self.default,          12: self.default,
            # ∙∙∙
            0: self.menu_inicio
        }
        i = Helpers.read_int('Ingrese una opción: ', 'Opción inválida.', 0, 16)
        o[i]()

        self.menu_opciones()

    @staticmethod
    def default():
        print('Opción no disponible.')

    @staticmethod
    def salir():
        s = '▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜\n' \
            '▌▓▓▒▒▒░                       ¡GRACIAS POR USAR EL PROGRAMA!                      ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                                                                           ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                             Desarrollado por:                             ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                                                                           ░▒▒▒▓▓▐\n' \
            '▌▓▓▒▒▒░                      Over Haider Castrillón Valencia.                     ░▒▒▒▓▓▐\n' \
            '▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟'
        print(s)
        sys.exit()

    """—————————————————————————————————————————————MÉTODOS——————————————————————————————————————————————————————————"""

    """———— ∙ ∙ ∙ ∙
        Vértices
    ∙ ∙ ∙ ∙ ————"""
    def ingresar_vertice(self):
        dato = input('Dato del vértice: ')
        self.grafo.ingresar_vertice(dato)

    def mostrar_vertices(self):
        self.grafo.mostrar_vertices()

    def obtener_vertice(self):
        origen = input('Origen: ')
        lista = []
        self.grafo.obtener_vertice(origen, lista)

        print('Lista [vértices]: ', lista)

    def generar_vertice(self):
        a = random.randint(65, 100)
        a = random.randint(65, 100)
        a = random.randint(65, 100)

        print(chr(65))
        print(chr(100))

    """———— ∙ ∙ ∙ ∙
        Aristas
    ∙ ∙ ∙ ∙ ————"""
    def ingresar_aristas(self):
        origen = input('Origen de la arista: ')
        destino = input('Destino de la arista: ')
        peso = input('Peso de la arista: ')
        ok = self.grafo.ingresar_arista(origen, destino, peso)
        if not ok:
            print('No se creó la arista.')

    def mostrar_aristas(self):
        print('Lista de aristas:')
        self.grafo.mostrar_aristas()

    """———— ∙ ∙ ∙
        Extras
    ∙ ∙ ∙ ————"""
    def hay_pozos(self):
        lista_vertices = self.grafo.get_lista_vertices()

        for i in range(len(lista_vertices)):
            if not lista_vertices[i].get_lista_adyacentes():
                return print("Pozo --> {0}".format(lista_vertices[i].get_dato()))
        return print("El grafo no tiene Pozos")

    def hay_fuentes(self):
        lista_vertices = self.lista_vertices


        for i in range(len(lista_vertices)):
            if lista_vertices[i].get_lista_adyacentes():
                return print("Fuente --> {0}".format(lista_vertices[i].get_dato()))
        return print("El grafo no tiene Fuentes")

        # determina el camino a recorrer
    def caminoRandom(self, padre, camion):
        i = random.randint(1, 3)
        # recorridos = {1: self.isla.recorrePre, 2: self.isla.recorreIn , 3: self.isla.recorrePos}
        # if i == 0:
        #     print('▌▓▒░    Camión no.', camion.getID(), 'recorre en Pre-Orden.')
        # elif i == 1:
        #     print('▌▓▒░    Camión no.', camion.getID(), 'recorre en In-Orden.')
        # else:
        #     print('▌▓▒░    Camión no.', camion.getID(), 'recorre en Pos-Orden.')
        # return recorridos[i](self.isla.getRaiz(), camion)

    """——————————————————————01——————————————————————EJECUCIÓN———————————————————————————————————————————————————————"""

    def ejecutar(self):

        print('▌▓▒░    Inicio ∙∙∙')

        """———— ∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙
            Variables iniciales
        ∙ ∙ ∙ ∙ ∙ ∙ ∙ ∙ ————"""
        cuevasNuevas = 0
        timer = 0
        seg = [1, 1, 2, 5, 10]

        # Ingreso de la velocidad
        print('▌▓▒░    Velocidad de ejecución    ▌▓▒░    '
              '01. Reloj [1s]    ▌▓▒░    02. Normal [2s]    ▌▓▒░    '
              '03. Rápido [5s]    ▌▓▒░    04. Parcial [10s]    ▌▓▒░')
        i = Helpers.read_int('Escoja una opción: ', 'Ingrese una velocidad correcta', 1, 4)

        # Ingreso tiempo
        limit = Helpers.read_int('Límite de tiempo: ', 'Ingrese un valor correcto', seg[i], sys.maxsize)

        self.crearCamiones(Helpers.read_int('Ingrese el numero de camiones: ', 'Ingrese un valor correcto', 1, sys.maxsize))
        # self.crearCamiones(10)

        self.crearCuevas(Helpers.read_int('Ingrese el numero de cuevas: ', 'Ingrese un valor correcto', 1, sys.maxsize))


        while timer >= 0:
            print('\n▌▓▒░    TIEMPO:', timer, 'SEGUNDOS—————————————————————————————————————————————————————————————————————')

            # Tiempo incremental y salida del programa.
            time.sleep(seg[i]/seg[i-1])
            timer += seg[i]
            if timer > limit:
                break

        self.salir()

    """——————————————————————01——————————————————————Terminado———————————————————————————————————————————————————————"""
