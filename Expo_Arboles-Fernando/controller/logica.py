from models.modelo import Grafo
class Familia:
    def __init__(self):
        self.grafo = Grafo()

    def adicionar_persnoa(self, persona):
        self.grafo.adicionar_vertice(persona)

    def adicionar_relacionamiento(self, persona1, persona2):
        self.grafo.adicionar_arista(persona1, persona2)

    def obtener_personas(self):
        return list(self.grafo.obter_vertices())

    def obter_relacionamentos(self):
        return self.grafo.obter_aristas()
    
    def obtener_arbol_completo(self):
        return self.grafo.obtener_arbol_completo()