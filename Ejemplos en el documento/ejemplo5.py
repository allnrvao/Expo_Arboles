def preorder(nodo): 
if nodo:
        print(nodo.value)       # visita la raíz
        preorder(nodo.left)     # recorre subárbol izquierdo
        preorder(nodo.right)    # recorre subárbol derecho
def inorder(nodo):
    if nodo:
        inorder(nodo.left)
        print(nodo.value)       # raíz entre hijos
        inorder(nodo.right)
def postorder(nodo):
    if nodo:
        postorder(nodo.left)
        postorder(nodo.right)
        print(nodo.value)       # visita la raíz al final