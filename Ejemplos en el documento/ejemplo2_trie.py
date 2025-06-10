class TrieNode:
    def __init__(self):
        self.children = {}  # diccionario de hijos {carácter: nodoTrie}
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        nodo = self.root
        for ch in word:
            nodo = nodo.children.setdefault(ch, TrieNode())
        nodo.is_end = True
    def search(self, word):
        nodo = self.root
        for ch in word:
            if ch not in nodo.children:
                return False
            nodo = nodo.children[ch]
        return nodo.is_end
# Insertar y buscar en el trie
trie = Trie()
trie.insert("hola")
print(trie.search("hola"))   # True
print(trie.search("ole"))    # False