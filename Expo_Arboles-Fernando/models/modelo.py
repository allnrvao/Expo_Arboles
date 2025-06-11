class Grafo:
    def __init__(self):
        self.grafo = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = []
    
    def adicionar_arista(self, vertice1, vertice2):
        if vertice1  not in self.grafo:
            return None
        else:
            self.adicionar_vertice(vertice2)
            self.grafo[vertice1].append(vertice2)
    
    def obter_vertices(self):
        return self.grafo.keys()
    
    def obter_aristas(self):
        aristas = []
        for vertice, adjacentes in self.grafo.items():
            for adjacente in adjacentes:
                aristas.append((vertice, adjacente))
        return aristas
    
    def obtener_arbol_completo(self):
        arbol = {}
        for vertice, adjacentes in self.grafo.items():
            if adjacentes:
                arbol[vertice] = adjacentes
            else:
                arbol[vertice] = []
        return arbol