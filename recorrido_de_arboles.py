from collections import deque

# Definición de la clase Nodo
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

# Recorrido Inorden: izquierda → raíz → derecha
def inorden(nodo):
    if nodo:
        inorden(nodo.izquierda)
        print(nodo.valor, end=" ")
        inorden(nodo.derecha)

# Recorrido Preorden: raíz → izquierda → derecha
def preorden(nodo):
    if nodo:
        print(nodo.valor, end=" ")
        preorden(nodo.izquierda)
        preorden(nodo.derecha)

# Recorrido Postorden: izquierda → derecha → raíz
def postorden(nodo):
    if nodo:
        postorden(nodo.izquierda)
        postorden(nodo.derecha)
        print(nodo.valor, end=" ")

# Recorrido por niveles (BFS)
def recorrido_por_niveles(raiz):
    if not raiz:
        return
    cola = deque([raiz])
    while cola:
        actual = cola.popleft()
        print(actual.valor, end=" ")
        if actual.izquierda:
            cola.append(actual.izquierda)
        if actual.derecha:
            cola.append(actual.derecha)

# Ejemplo de uso
if __name__ == "__main__":
    a = Nodo('A')
    b = Nodo('B')
    c = Nodo('C')
    d = Nodo('D')
    e = Nodo('E')

    a.izquierda = b
    a.derecha = c
    b.izquierda = d
    b.derecha = e

    print("Recorrido Inorden:")
    inorden(a)
    print("\n")

    print("Recorrido Preorden:")
    preorden(a)
    print("\n")

    print("Recorrido Postorden:")
    postorden(a)
    print("\n")

    print("Recorrido por niveles (BFS):")
    recorrido_por_niveles(a)
    print()
