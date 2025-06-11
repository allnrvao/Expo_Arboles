from model.arbol import Arbol_Binario
class Ordenar:
    def __init__(self):
        self.arbol = Arbol_Binario()

    def ordenar(self):
        ordenados=self.arbol.ordenar()
        self.arbol.insertar_lista(ordenados)
    
    def insertar(self, valor):
        self.arbol.insertar(valor)
    def mostrar_arbol(self):
        return self.arbol.mostrar_arbol()
    
    def obtener_arbol_como_json(self):
        return self.arbol.obtener_arbol_como_json()