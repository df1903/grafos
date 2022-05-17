"""————————————————
   Grafo class
———————————————————"""

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
        for i in range(len(self.listaVertices)):
            print("{0}".format(self.listaVertices[i].getDato()))
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
        for i in range(len(self.listaAristas)):
            print("| Origen: {0}  →  Destino: {1}  |  Peso: {2} |"
                  .format(self.listaAristas[i].getOrigen(),
                          self.listaAristas[i].getDestino(),
                          self.listaAristas[i].getPeso()))

    # show adjacencies
    def mostrarAdyacencias(self):
        for i in range(len(self.listaVertices)):
            print("| vértice: {0} |  Adyacencias: {1} |"
                  .format(self.listaVertices[i].getDato(),
                          self.listaVertices[i].getListaAdyacencias()))

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
        self.ordenar(entorno, entorno + 1)
        return self.minMaxAristas(entorno + 1)

    def ordenar(self, entorno, iter):
        if iter == (len(self.listaAristas)):
            return
        if self.listaAristas[entorno].getPeso() > self.listaAristas[iter].getPeso():
            aux = self.listaAristas[entorno]
            self.listaAristas[entorno] = self.listaAristas[iter]
            self.listaAristas[iter] = aux
        return self.ordenar(entorno, iter + 1)

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
        print("Grado de los vertices")
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
        print("Pozos")
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
        print("Fuentes")
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
        aristaMayor= [0]
        for i in range(len(self.listaAristas)):
            if aristaMayor < self.listaAristas[i].getPeso():
               aristaMayor = [self.listaAristas[i]]
            elif aristaMayor == self.listaAristas[i].getPeso():
                aristaMayor.append([self.listaAristas[i]])
    #fala mostra