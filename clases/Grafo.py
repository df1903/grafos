"""————————————————
   Grafo class
———————————————————"""
import sys
from clases.Arista import *
from clases.Vertice import *

class Grafo:

    # builder
    def __init__(self):
        self.listaVertices = []
        self.listaAristas = []

    """————————————————————————————————————————————GETS | SETS————————————————————————————————————————————————————"""

    # Set - Get | lista de vertices
    def getListaVertices(self):
        return self.listaVertices

    def setListaVertices(self, listaVertices):
        self.listaVertices = listaVertices

    # Set - Get | lista de aristas
    def getListaAristas(self):
        return self.listaAristas

    def setListaAristas(self, listaAristas):
        self.listaAristas = listaAristas

    """—————————————————————————————————————————VERTEX METHODS———————————————————————————————————————————————————"""

    # enter vertex
    def ingresarVertice(self, dato):
        if not self.existeVertice(dato, self.listaVertices):
            self.listaVertices.append(Vertice(dato))

    # vertex exists
    def existeVertice(self, dato, listaVertices):
        for i in range(len(listaVertices)):
            if dato == listaVertices[i].getDato():
                return True
        return False

    # show Vertices
    def mostrarVertices(self):
        print("                                    VERTICES")
        for i in range(len(self.listaVertices)):
            print(i+1, "- {0}".format(self.listaVertices[i].getDato()))
        # return False

    # get Vertex
    def obtenerVertice(self, origen, lista):
        for i in range(len(lista)):
            if origen == lista[i].getDato():
                return lista[i]

    """—————————————————————————————————————————EDGES METHODS————————————————————————————————————————————————————"""

    # enter edge
    def ingresarArista(self, origen, destino, peso):
        if not self.verificarListaAristas(origen, destino, self.listaAristas):
            if self.existeVertice(origen, self.listaVertices) and self.existeVertice(destino, self.listaVertices):
                self.listaAristas.append(Arista(origen, destino, peso))
                self.obtenerVertice(origen, self.listaVertices).getListaAdyacentes().append(destino)
                return True
        return False

    # check List edges
    def verificarListaAristas(self, origen, destino, lista):
        for i in range(len(lista)):
            if origen == lista[i].getOrigen() and destino == lista[i].getDestino():
                return True
        return False

    # show edges
    def mostrarAristas(self):
        print("                                    ARISTAS")
        for i in range(len(self.listaAristas)):
            print("| Origen: {0}  →  Destino: {1}  |  Peso: {2} |"
                  .format(self.listaAristas[i].getOrigen(),
                          self.listaAristas[i].getDestino(),
                          self.listaAristas[i].getPeso()))

    # show adjacencies
    def mostrarAdyacencias(self):
        print("                                    ADYACENCIAS")
        for i in range(len(self.listaVertices)):
            print("| vértice: {0} |  Adyacencias: {1} |"
                  .format(self.listaVertices[i].getDato(),
                          self.listaVertices[i].getListaAdyacentes()))

    """—————————————————————————————————————————————FUNCTIONS————————————————————————————————————————————————————————"""

    # are there wells?
    def existenPozos(self):
        for i in range(len(self.listaVertices)):
            if not self.listaVertices[i].getListaAdyacentes():
                return print("Pozo --> {0}".format(self.listaVertices[i].getDato()))
        return print("El grafo no tiene Pozos")

    # are there sources?
    def existenFuentes(self):
        for i in range(len(self.listaVertices)):
            if self.listaVertices[i].getListaAdyacentes():
                return print("Fuente --> {0}".format(self.listaVertices[i].getDato()))
        return print("El grafo no tiene Fuentes")

    # 1)smallest to largest edges
    def minMaxAristas(self, entorno):
        if entorno == (len(self.listaAristas)):
            return
        self.ordenarMinMax(entorno, entorno + 1)
        return self.minMaxAristas(entorno + 1)

    def ordenarMinMax(self, entorno, iter):
        if iter == (len(self.listaAristas)):
            return
        if self.listaAristas[entorno].getPeso() > self.listaAristas[iter].getPeso():
            aux = self.listaAristas[entorno]
            self.listaAristas[entorno] = self.listaAristas[iter]
            self.listaAristas[iter] = aux
        return self.ordenarMinMax(entorno, iter + 1)

    # 1.1)largest to smallest edges
    def maxMinAristas(self, entorno):
        if entorno == (len(self.listaAristas)):
            return
        self.ordenarMaxMin(entorno, entorno + 1)
        return self.maxMinAristas(entorno + 1)

    def ordenarMaxMin(self, entorno, iter):
        if iter == (len(self.listaAristas)):
            return
        if self.listaAristas[entorno].getPeso() < self.listaAristas[iter].getPeso():
            aux = self.listaAristas[entorno]
            self.listaAristas[entorno] = self.listaAristas[iter]
            self.listaAristas[iter] = aux
        return self.ordenarMaxMin(entorno, iter + 1)


    # 2)degree of the vertices
    # def gradoVertices(self, entorno):
    #     if entorno == (len(self.listaVertices)):
    #         return True
    #     self.gradoVertice(self.listaVertices[entorno], 0, 0)
    #     return self.gradoVertices01(entorno+1)
    #
    # def gradoVertice(self, vertice, entorno, gradoVertice):
    #     if entorno == (len(self.listaAristas)):
    #         print("El grado del vertice {} es {}".format(vertice.getDato(), gradoVertice))
    #         return
    #     if vertice.getDato() == self.listaAristas[entorno].getOrigen() or vertice.getDato() == self.listaAristas[entorno].getDestino():
    #         gradoVertice += 1
    #     self.gradoVertice(vertice, entorno+1, gradoVertice)

    def gradoVertices(self, entorno, listaGrados):
        if entorno == 0:
            for i in range(len(self.listaVertices)):
                listaGrados.append(0)
        if entorno == (len(self.listaAristas)):
            return listaGrados
        for i in range(len(self.listaVertices)):
            if self.listaVertices[i].getDato() == self.listaAristas[entorno].getOrigen() or self.listaVertices[i].getDato() == self.listaAristas[entorno].getDestino():
                listaGrados[i] += 1
        return self.gradoVertices(entorno+1,listaGrados)

    def mostrarGradoVertices(self):
        print("                                 GRADOS DE LOS VERTICES")
        listaGrados = self.gradoVertices(0,[])
        for i in range(len(self.listaVertices)):
            print("{} Grado({})".format(self.listaVertices[i].getDato(), listaGrados[i]))

    # 3)vertex highest degree
    def verticeMayorGrado(self):
        listaGrados = self.gradoVertices(0,[])
        vertice = [0,0]
        for i in range(len(self.listaVertices)):
            if listaGrados[i] > vertice[1]:
                vertice[0] = i
                vertice[1] = listaGrados[i]
        print("{} con grado de {} es el vertice con mayor grado".format(self.listaVertices[vertice[0]].getDato(),vertice[1]))

    # 4)average adjacencies list
    def promedioListaAdyacencias(self):
        adyacencias = 0
        for i in range(len(self.listaVertices)):
            adyacencias += len(self.listaVertices[i].getListaAdyacentes())
        adyacencias = adyacencias/len(self.listaVertices)
        print("El promedio de la lista de adyacencias es: ",adyacencias)

    # 5)Show the wells
    def pozos(self,entorno,listaPozos):
        if entorno == 0:
            for i in range(len(self.listaVertices)):
                listaPozos.append(True)
        if entorno == (len(self.listaAristas)):
            return listaPozos
        for i in range(len(self.listaVertices)):
            if self.listaVertices[i].getDato() == self.listaAristas[entorno].getOrigen():
                listaPozos[i] = False
        return self.pozos(entorno+1, listaPozos)

    def mostrarPozos(self):
        print("                                    POZOS")
        listaPozos = self.pozos(0,[])
        for i in range(len(self.listaVertices)):
            if listaPozos[i]:
                print(self.listaVertices[i].getDato())

    # 6)Show the sources
    def fuentes(self,entorno,listaFuentes):
        if entorno == 0:
            for i in range(len(self.listaVertices)):
                listaFuentes.append(True)
        if entorno == (len(self.listaAristas)):
            return listaFuentes
        for i in range(len(self.listaVertices)):
            if self.listaVertices[i].getDato() == self.listaAristas[entorno].getDestino():
                listaFuentes[i] = False
        return self.fuentes(entorno+1, listaFuentes)

    def mostrarFuentes(self):
        print("                                   FUENTES")
        listaFuentes = self.fuentes(0,[])
        for i in range(len(self.listaVertices)):
            if listaFuentes[i]:
                print(self.listaVertices[i].getDato())

    # 7)average edge weight
    def promedioPesoAristas(self):
        promedio = 0
        for i in range(len(self.listaAristas)):
            promedio += self.listaAristas[i].getPeso()
        promedio = promedio / len(self.listaAristas)
        print("El promedio del peso de las aristas es: ",promedio)

    # 8)top artist
    def aristaMayorPeso(self):
        aristaMayor= [Arista(0,0,0)]
        for i in range(len(self.listaAristas)):
            if aristaMayor[len(aristaMayor)-1].getPeso() < self.listaAristas[i].getPeso():
               aristaMayor = [self.listaAristas[i]]
            elif aristaMayor[len(aristaMayor)-1].getPeso() == self.listaAristas[i].getPeso():
                aristaMayor.append(self.listaAristas[i])

        if len(aristaMayor) == 1:
            print("Arista mayor peso: {}--> {} peso {}".format(aristaMayor[0].getOrigen(), aristaMayor[0].getDestino(), aristaMayor[0].getPeso()))

        else:
            print("Las aristas de mayor peso son:")
            for i in range(len(aristaMayor)):
                print ("{}--> {} peso {}".format(aristaMayor[i].getOrigen(), aristaMayor[i].getDestino() , aristaMayor[i].getPeso()))

    # 9)
    def aristaMenorPeso(self):
        aristaMenor= [Arista(0,0,sys.maxsize)]
        for i in range(len(self.listaAristas)):
            if aristaMenor[len(aristaMenor)-1].getPeso() > self.listaAristas[i].getPeso():
               aristaMenor = [self.listaAristas[i]]
            elif aristaMenor[len(aristaMenor)-1].getPeso() == self.listaAristas[i].getPeso():
                aristaMenor.append(self.listaAristas[i])

        if len(aristaMenor) == 1:
            print("Arista menor peso: {}--> {} peso {}".format(aristaMenor[0].getOrigen(), aristaMenor[0].getDestino(), aristaMenor[0].getPeso()))

        else:
            print("Las aristas de menor peso son:")
            for i in range(len(aristaMenor)):
                print ("{}--> {} peso {}".format(aristaMenor[i].getOrigen(), aristaMenor[i].getDestino() , aristaMenor[i].getPeso()))

    # 10)
    def verticeAdyacente(self):
        print("Ahora")

    # 11)
    def listaAdyacencias(self):
        lista=[]
        for i in range(len(self.listaVertices)):
            for j in range(len(self.listaVertices[i].getListaAdyacentes())):
                lista.append(self.listaVertices[i].getListaAdyacentes()[j])
        return lista

    def mostrarListaAdyacentes(self):
        print("                                  LISTA ADYACENTES")
        lista = self.listaAdyacencias()
        for i in range(len(lista)):
            print(lista[i])
    # a)
    def verticesNoContemplados(self, entorno, listaVertices, listaAdyacencias):
        if entorno == 0:
            listaAdyacencias = self.listaAdyacencias()
            for i in range(len(self.listaVertices)):
                listaVertices.append(True)
        if entorno == (len(self.listaVertices)):
            return listaVertices
        for i in range(len(listaAdyacencias)):
            if self.listaVertices[entorno].getDato() == listaAdyacencias[i]:
                listaVertices[entorno] = False
        return self.verticesNoContemplados(entorno+1, listaVertices, listaAdyacencias)

    def mostrarVerticesNoContemplados(self):
        print("                                  VERTICES NO CONTEMPLADOS")
        listaVertices =self.verticesNoContemplados(0, [], [])
        for i in range(len(listaVertices)):
            if listaVertices[i]:
                print(self.listaVertices[i].getDato())

    # b)
    def adyacenciaMasComun(self, entorno, listaVertices, listaAdyacencias):
        if entorno == 0:
            listaAdyacencias = self.listaAdyacencias()
            for i in range(len(self.listaVertices)):
                listaVertices.append(0)
        if entorno == (len(self.listaVertices)):
            return listaVertices
        for i in range(len(listaAdyacencias)):
            if self.listaVertices[entorno].getDato() == listaAdyacencias[i]:
                listaVertices[entorno] += 1
        return self.adyacenciaMasComun(entorno+1, listaVertices, listaAdyacencias)

    def mostarAdyacenciaMasComun(self):
        listaVertices = self.adyacenciaMasComun(0, [], [])
        comun = 0
        for i in range(len(listaVertices)):
            if listaVertices[i] > comun:
                comun = i
        print("La adyacencia mas comun es {} con {} ".format(self.listaVertices[comun].getDato(), listaVertices[comun]))