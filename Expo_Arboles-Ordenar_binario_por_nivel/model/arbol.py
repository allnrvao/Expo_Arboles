from model.nodo import Nodo
from collections import deque
class Arbol_Binario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, raiz, valor):
        nuevo_nodo = Nodo(valor)

        if raiz is None:
            return nuevo_nodo

        cola = deque()
        cola.append(raiz)

        while cola:
            actual = cola.popleft()

            if actual.izquierda is None:
                actual.izquierda = nuevo_nodo
                return raiz
            else:
                cola.append(actual.izquierda)

            if actual.derecha is None:
                actual.derecha = nuevo_nodo
                return raiz
            else:
                cola.append(actual.derecha)

        return raiz
    
    def ordenar(self):
        valores = self._recorrer_completo(self.raiz)
        return sorted(valores)

    def _recorrer_completo(self, nodo):
        if nodo is None:
            return []
        
        valores = []
        cola = deque()
        cola.append(nodo)
        
        while cola:
            actual = cola.popleft()
            valores.append(actual.valor)
            if actual.izquierda:
                cola.append(actual.izquierda)
            if actual.derecha:
                cola.append(actual.derecha)
        
        return valores

    
    def insertar_lista(self, lista):
        self.limpiar()
        for valor in lista:
            self.insertar(valor)

    def mostrar_arbol(self):
        if self.raiz is None:
            return "Árbol vacío"
        else:
            return self._mostrar_arbol_recursivo(self.raiz)
    def _mostrar_arbol_recursivo(self, nodo):
        if nodo is None:
            return ""
        resultado = ""
        resultado += self._mostrar_arbol_recursivo(nodo.izquierda)
        resultado += str(nodo.valor) + " "
        resultado += self._mostrar_arbol_recursivo(nodo.derecha)
        return resultado
    
    def obtener_arbol_como_json(self):
        def recorrer(nodo):
            if nodo is None:
                return None
            return {
                'valor': nodo.valor,
                'izquierda': recorrer(nodo.izquierda),
                'derecha': recorrer(nodo.derecha)
            }
        return recorrer(self.raiz)  
    
    def limpiar(self):
        self.raiz = None
