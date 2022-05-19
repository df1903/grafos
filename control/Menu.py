"""——————————————————————————————————————————————
    console method menu
——————————————————————————————————————————————"""
# import sys, time, random
# from data.Grafo import *
# from helpers import
from helpers.Keyboard import *
import self

from clases.Grafo import *


class Menu:

    """—————————————————————————————————————————————CONSTRUCTOR——————————————————————————————————————————————————————"""

    def __init__(self):
        self.name = ''
        self.grafo = Grafo()

    """—————————————————————————————————————————————SALIDA-PANTALLA——————————————————————————————————————————————————"""

    def menuInicio(self):

        self.inicializarGrafo()
        print('▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜\n' \
              '▌▓▒░     01. Iniciar     ░▒▓█▓▒░     02. Opciones     ░▒▓█▓▒░     03. Salir     ░▒▓▐\n' \
              '▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟')

        opcion = {
            1: self.ejecutar, 2: self.menuOpciones, 3: self.salir
        }
        i = Keyboard.readIntRangeDefaultErrorMessage("Ingrese una opcion: ", 1, 3)
        opcion[i]()



    def menuOpciones(self):
        print(
            "\nOPCIONES"
            "\n01 — Ejecutar todos       02 — Mostrar aristas     03 — Ver vértices         04 — ¿Hay pozos?"
            "\n05 — Generar vértice      06 — Ingresar arista      07 — Ver aristas          08 — ¿Hay fuentes?"
            "\n09 — Generar arista       10 — ∙∙∙                  11 — ∙∙∙                  12 — ∙∙∙"
            "\n13 — ¿Hay pozos?          14 — ¿Hay fuentes?        15 — Prom. peso Aristas   16 — ∙∙∙"
            "\n13 — ¿Hay pozos?          14 — ¿Hay fuentes?        15 — ∙∙∙                  16 — ∙∙∙"
            "\n13 — ¿Hay pozos?          14 — ¿Hay fuentes?        15 — ∙∙∙                  16 — ∙∙∙"
            "\n13 — ¿Hay pozos?          14 — ¿Hay fuentes?        15 — ∙∙∙                  16 — ∙∙∙"
            # ∙∙∙
            "\n00 — Volver"
        )
        opcion = {
            1: self.todosMetodos
        }
        i = Keyboard.readIntRangeDefaultErrorMessage("Ingrese una opcion: ", 1, 3)
        opcion[i]()

        # self.menu_opciones()

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
            '▌▓▓▒▒▒░                      Daniel Felipe Franco Rincon                          ░▒▒▒▓▓▐\n' \
            '▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟'
        print(s)
        sys.exit()




    """——————————————————————01——————————————————————EJECUCIÓN———————————————————————————————————————————————————————"""

    def ejecutar(self):
        self.menuInicio()


    def todosMetodos(self):
        print("Todos los metodos\n")
        self.tipoGrafo()
        self.grafo.mostrarVertices()


    # graph type
    def tipoGrafo(self):
        print("Tipos de Grafos"
             "\n1) Grafo dirigido/sin ciclos/conexo     5) Grafo no dirigido/sin ciclos/conexo" 
             "\n2) Grafo dirigido/sin ciclos/no conexo  6) Grafo no dirigido/sin ciclos/no conexo" 
             "\n3) Grafo dirigido/con ciclos/conexo     7) Grafo no dirigido/con ciclos/conexo" 
             "\n4) Grafo dirigido/con ciclos/no conexo  8) Grafo nodirigido/con ciclos/no conexo "
             )
        opcion = {
            1: self.grafo_nociclos_conexo_dirigido, 5: self.grafo_nociclos_conexo_nodirigido,
            2: self.grafo_nociclos_noconexo_dirigido, 6: self.grafo_nociclos_noconexo_nodirigido,
            3: self.grafo_ciclos_conexo_dirigido, 7: self.grafo_ciclos_conexo_nodirigido,
            4: self.grafos_ciclos_noconexo_dirigido, 8: self.grafos_ciclos_noconexo_nodirigido
        }
        i = Keyboard.readIntRangeDefaultErrorMessage("Ingrese del tipo de grafo que desea crear: ", 1, 8)
        opcion[i]()


    """—————————————————————————————————————————————Grafos/Vertices——————————————————————————————————————————————————"""

    def inicializarGrafo(self):
        # creation of vertices
        self.grafo.ingresarVertice('Manizales')
        self.grafo.ingresarVertice('Pereira')
        self.grafo.ingresarVertice('Armenia')
        self.grafo.ingresarVertice('Cali')
        self.grafo.ingresarVertice('Bogota')
        self.grafo.ingresarVertice('Cututa')
        self.grafo.ingresarVertice('Barranquilla')
        self.grafo.ingresarVertice('Cartagena')
        self.grafo.ingresarVertice('Medellin')

    """———————————————————————————————————————————————Grafos/Aristas—————————————————————————————————————————————————"""

    # graph_nocycles_connected_directed
    def grafo_nociclos_conexo_dirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/dirigido/conexo/sin ciclos"
        self.grafo.ingresarArista('Manizales','Pereira',1)
        self.grafo.ingresarArista('Manizales', 'Bogota', 8)
        self.grafo.ingresarArista('Manizales', 'Medellin', 4)
        self.grafo.ingresarArista('Pereira','Armenia',3)
        self.grafo.ingresarArista('Armenia','Cali',4)
        self.grafo.ingresarArista('Armenia','Bogota',3)
        self.grafo.ingresarArista('Medellin','Bogota',4)
        self.grafo.ingresarArista('Bogota','Cututa',7)
        self.grafo.ingresarArista('Bogota','Cartagena',6)
        self.grafo.ingresarArista('Cartagena','Barranquilla',1)
        self.grafo.ingresarArista('Barranquilla','Cututa',12)

    # graph_no cycles_no connected_directed
    def grafo_nociclos_noconexo_dirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/dirigido/no conexo/sin ciclos"
        self.grafo.ingresarArista('Manizales', 'Pereira', 1)
        self.grafo.ingresarArista('Manizales', 'Bogota', 8)
        self.grafo.ingresarArista('Manizales', 'Medellin', 4)
        self.grafo.ingresarArista('Pereira', 'Armenia', 3)
        self.grafo.ingresarArista('Armenia', 'Cali', 4)
        self.grafo.ingresarArista('Armenia', 'Bogota', 3)
        self.grafo.ingresarArista('Medellin', 'Bogota', 4)
        self.grafo.ingresarArista('Cartagena', 'Barranquilla', 1)
        self.grafo.ingresarArista('Barranquilla', 'Cututa', 12)

    # graph_cycles_connected_directed
    def grafo_ciclos_conexo_dirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/dirigido/conexo/ciclos"
        self.grafo.ingresarArista('Manizales','Pereira',1)
        self.grafo.ingresarArista('Bogota','Manizales', 8)
        self.grafo.ingresarArista('Manizales','Medellin',4)
        self.grafo.ingresarArista('Pereira','Armenia',3)
        self.grafo.ingresarArista('Armenia','Cali',4)
        self.grafo.ingresarArista('Armenia','Bogota',3)
        self.grafo.ingresarArista('Medellin','Bogota',4)
        self.grafo.ingresarArista('Bogota','Cututa',7)
        self.grafo.ingresarArista('Bogota','Cartagena',6)
        self.grafo.ingresarArista('Cartagena','Barranquilla',1)
        self.grafo.ingresarArista('Barranquilla','Cututa',12)

    # graph_cycles_no connected_directed
    def grafos_ciclos_noconexo_dirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/dirigido/no conexo/ciclos"
        self.grafo.ingresarArista('Manizales','Pereira',1)
        self.grafo.ingresarArista('Bogota','Manizales',8)
        self.grafo.ingresarArista('Manizales','Medellin',4)
        self.grafo.ingresarArista('Pereira','Armenia',3)
        self.grafo.ingresarArista('Armenia','Cali',4)
        self.grafo.ingresarArista('Armenia','Bogota',3)
        self.grafo.ingresarArista('Medellin','Bogota',4)
        self.grafo.ingresarArista('Cututa','Cartagena',13)
        self.grafo.ingresarArista('Cartagena','Barranquilla',1)
        self.grafo.ingresarArista('Barranquilla','Cututa',12)

    # graph_cycles_connected_no directed
    def grafo_ciclos_conexo_nodirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/no dirigido/conexo/ciclos"
        self.grafo.ingresarArista('Manizales','Pereira',1)
        self.grafo.ingresarArista('Pereira','Manizales',1)
        self.grafo.ingresarArista('Manizales','Bogota',8)
        self.grafo.ingresarArista('Bogota','Manizales',8)
        self.grafo.ingresarArista('Manizales','Medellin',4)
        self.grafo.ingresarArista('Medellin','Manizales',4)
        self.grafo.ingresarArista('Pereira','Armenia',3)
        self.grafo.ingresarArista('Armenia', 'Pereira',3)
        self.grafo.ingresarArista('Armenia','Cali',4)
        self.grafo.ingresarArista('Cali','Armenia',4)
        self.grafo.ingresarArista('Armenia','Bogota',3)
        self.grafo.ingresarArista('Bogota','Armenia',3)
        self.grafo.ingresarArista('Medellin','Bogota',4)
        self.grafo.ingresarArista('Bogota','Medellin',4)
        self.grafo.ingresarArista('Bogota','Cututa',7)
        self.grafo.ingresarArista('Cututa','Bogota',7)
        self.grafo.ingresarArista('Bogota','Cartagena',6)
        self.grafo.ingresarArista('Cartagena','Bogota',6)
        self.grafo.ingresarArista('Cartagena','Barranquilla',1)
        self.grafo.ingresarArista('Barranquilla','Cartagena',1)
        self.grafo.ingresarArista('Barranquilla','Cututa',12)
        self.grafo.ingresarArista('Cututa','Barranquilla',12)

    # graph_cycles_no connected_no directed
    def grafos_ciclos_noconexo_nodirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/no dirigido/no conexo/ciclos"
        self.grafo.ingresarArista('Manizales','Pereira',1)
        self.grafo.ingresarArista('Pereira','Manizales',1)
        self.grafo.ingresarArista('Manizales','Bogota',8)
        self.grafo.ingresarArista('Bogota','Manizales',8)
        self.grafo.ingresarArista('Manizales','Medellin',4)
        self.grafo.ingresarArista('Medellin','Manizales',4)
        self.grafo.ingresarArista('Pereira','Armenia',3)
        self.grafo.ingresarArista('Armenia', 'Pereira',3)
        self.grafo.ingresarArista('Armenia','Cali',4)
        self.grafo.ingresarArista('Cali','Armenia',4)
        self.grafo.ingresarArista('Armenia','Bogota',3)
        self.grafo.ingresarArista('Bogota','Armenia',3)
        self.grafo.ingresarArista('Medellin','Bogota',4)
        self.grafo.ingresarArista('Bogota','Medellin',4)
        self.grafo.ingresarArista('Cartagena','Barranquilla',1)
        self.grafo.ingresarArista('Barranquilla','Cartagena',1)
        self.grafo.ingresarArista('Barranquilla','Cututa',12)
        self.grafo.ingresarArista('Cututa','Barranquilla',12)

    # graph_no cycles_connected_no directed
    def grafo_nociclos_conexo_nodirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/no dirigido/conexo/sin ciclos"
        self.grafo.ingresarArista('Manizales','Pereira',1)
        self.grafo.ingresarArista('Pereira','Manizales',1)
        self.grafo.ingresarArista('Manizales','Bogota',8)
        self.grafo.ingresarArista('Bogota','Manizales',8)
        self.grafo.ingresarArista('Manizales','Medellin',4)
        self.grafo.ingresarArista('Medellin','Manizales',4)
        self.grafo.ingresarArista('Pereira','Armenia',3)
        self.grafo.ingresarArista('Armenia', 'Pereira',3)
        self.grafo.ingresarArista('Armenia','Cali',4)
        self.grafo.ingresarArista('Cali','Armenia',4)
        self.grafo.ingresarArista('Bogota','Cartagena',4)
        self.grafo.ingresarArista('Cartagena','Bogota',6)
        self.grafo.ingresarArista('Cartagena','Barranquilla',1)
        self.grafo.ingresarArista('Barranquilla','Cartagena',1)
        self.grafo.ingresarArista('Barranquilla','Cututa',12)
        self.grafo.ingresarArista('Cututa','Barranquilla',12)

    # graph_no cycles_no connected_no directed
    def grafo_nociclos_noconexo_nodirigido(self):
        self.grafo.setListaAristas([])
        self.name = "grafo/no dirigido/no conexo/sin ciclos"
        self.grafo.ingresarArista('Manizales','Pereira',1)
        self.grafo.ingresarArista('Pereira','Manizales',1)
        self.grafo.ingresarArista('Manizales','Bogota',8)
        self.grafo.ingresarArista('Bogota','Manizales',8)
        self.grafo.ingresarArista('Manizales','Medellin',4)
        self.grafo.ingresarArista('Medellin','Manizales',4)
        self.grafo.ingresarArista('Pereira','Armenia',3)
        self.grafo.ingresarArista('Armenia', 'Pereira',3)
        self.grafo.ingresarArista('Armenia','Cali',4)
        self.grafo.ingresarArista('Cali','Armenia',4)
        self.grafo.ingresarArista('Cartagena','Barranquilla',1)
        self.grafo.ingresarArista('Barranquilla','Cartagena',1)
        self.grafo.ingresarArista('Barranquilla','Cututa',12)
        self.grafo.ingresarArista('Cututa','Barranquilla',12)