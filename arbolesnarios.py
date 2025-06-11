class NodoArbolNario:
    def __init__(self, valor):
        self.valor = valor  # Nombre del nodo (grupo o integrante)
        self.hijos = []  # Lista de hijos (puede tener 0 o más)

    def agregar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)  # Agrega un hijo al nodo

    def mostrar(self, nivel=0, prefijo=""):
        # Imprime el nodo actual con flecha y prefijo
        print(prefijo + "-> " + self.valor)
        # Iterar sobre los hijos
        for i, hijo in enumerate(self.hijos):
            # Añadir indentación para el siguiente nivel
            nuevo_prefijo = prefijo + "    "
            hijo.mostrar(nivel + 1, nuevo_prefijo)

# Crear un árbol n-ario que representa grupos de K-pop y sus integrantes
def crear_arbol_kpop():
    # Raíz del árbol
    raiz = NodoArbolNario("Grupos K-pop")

    # Grupos de K-pop
    twice = NodoArbolNario("TWICE")
    day6 = NodoArbolNario("DAY6")
    newjeans = NodoArbolNario("NewJeans")
    xdinary_heroes = NodoArbolNario("Xdinary Heroes")

    # Integrantes de TWICE
    twice.agregar_hijo(NodoArbolNario("Nayeon"))
    twice.agregar_hijo(NodoArbolNario("Jeongyeon"))
    twice.agregar_hijo(NodoArbolNario("Momo"))
    twice.agregar_hijo(NodoArbolNario("Sana"))
    twice.agregar_hijo(NodoArbolNario("Jihyo"))
    twice.agregar_hijo(NodoArbolNario("Mina"))
    twice.agregar_hijo(NodoArbolNario("Dahyun"))
    twice.agregar_hijo(NodoArbolNario("Chaeyoung"))
    twice.agregar_hijo(NodoArbolNario("Tzuyu"))

    # Integrantes de DAY6
    day6.agregar_hijo(NodoArbolNario("Sungjin"))
    day6.agregar_hijo(NodoArbolNario("Young K"))
    day6.agregar_hijo(NodoArbolNario("Wonpil"))
    day6.agregar_hijo(NodoArbolNario("Dowoon"))

    # Integrantes de NewJeans
    newjeans.agregar_hijo(NodoArbolNario("Hanni"))
    newjeans.agregar_hijo(NodoArbolNario("Haerin"))
    newjeans.agregar_hijo(NodoArbolNario("Hyein"))
    newjeans.agregar_hijo(NodoArbolNario("Minji"))
    newjeans.agregar_hijo(NodoArbolNario("Danielle"))

    # Integrantes de Xdinary Heroes
    xdinary_heroes.agregar_hijo(NodoArbolNario("Gunil"))
    xdinary_heroes.agregar_hijo(NodoArbolNario("Jungsu"))
    xdinary_heroes.agregar_hijo(NodoArbolNario("Gaon"))
    xdinary_heroes.agregar_hijo(NodoArbolNario("O.de"))
    xdinary_heroes.agregar_hijo(NodoArbolNario("Jun Han"))
    xdinary_heroes.agregar_hijo(NodoArbolNario("Jooyeon"))

    # Agregar grupos a la raíz
    raiz.agregar_hijo(twice)
    raiz.agregar_hijo(day6)
    raiz.agregar_hijo(newjeans)
    raiz.agregar_hijo(xdinary_heroes)

    return raiz

# Ejecutar y mostrar el árbol
if __name__ == "__main__":
    arbol_kpop = crear_arbol_kpop()
    print("Estructura de grupos de K-pop y sus integrantes:")
    arbol_kpop.mostrar()