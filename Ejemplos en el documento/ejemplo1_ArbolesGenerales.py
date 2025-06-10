# Ejemplo sencillo: clase para representar un árbol genérico
class TreeNode:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []


# Creación de un árbol con un nodo raíz y dos hijos
root = TreeNode(1, [TreeNode(2), TreeNode(3, [TreeNode(4)])])
# Función para imprimir el árbol de forma recursiva
def print_tree(node, level=0):
    print(' ' * level + str(node.value))
    for child in node.children:
        print_tree(child, level + 2)
# Imprimir el árbol
print_tree(root)
