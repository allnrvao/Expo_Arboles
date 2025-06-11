from collections import deque

class Nodo:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs(root):
    q = deque([root])
    while q:
        nodo = q.popleft()
        print(nodo.value)  # visita el nodo actual
        if nodo.left:
            q.append(nodo.left)
        if nodo.right:
            q.append(nodo.right)

# Ejemplo de uso
if __name__ == "__main__":
    # Creamos un árbol de ejemplo:
    #       A
    #      / \
    #     B   C
    #    / \   \
    #   D   E   F

    a = Nodo('A')
    b = Nodo('B')
    c = Nodo('C')
    d = Nodo('D')
    e = Nodo('E')
    f = Nodo('F')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    bfs(a)
