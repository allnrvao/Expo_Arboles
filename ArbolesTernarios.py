import flet as ft

class TernaryNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.middle = None
        self.right = None

class TernarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        def _insert(node, value):
            if not node:
                return TernaryNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            elif value > node.value:
                node.right = _insert(node.right, value)
            else:
                node.middle = _insert(node.middle, value)
            return node
        self.root = _insert(self.root, value)

    def search(self, value):
        def _search(node, value):
            if not node:
                return False
            if value < node.value:
                return _search(node.left, value)
            elif value > node.value:
                return _search(node.right, value)
            else:
                return True
        return _search(self.root, value)

    def in_order(self):
        def _in_order(node):
            if not node:
                return []
            return _in_order(node.left) + [node.value] + _in_order(node.middle) + _in_order(node.right)
        return _in_order(self.root)

    def pretty(self):
        lines = []

        def _pretty(node, indent=""):
            if not node:
                return
            _pretty(node.right, indent + "    ")
            lines.append(indent + f"R─ {node.value}")
            _pretty(node.middle, indent + "    ")
            _pretty(node.left, indent + "    ")

        _pretty(self.root)
        return "\n".join(lines)


def main(page: ft.Page):
    page.title = "Árbol Ternario con Flet"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO

    tree = TernarySearchTree()

    input_box = ft.TextField(label="Valor a insertar", width=200)
    insert_button = ft.ElevatedButton(text="Insertar")
    search_box = ft.TextField(label="Buscar valor", width=200)
    search_button = ft.ElevatedButton(text="Buscar")
    in_order_display = ft.Text()
    tree_structure = ft.Text(style=ft.TextStyle(font_family="Courier New", size=14))
    result_text = ft.Text()

    def insert_click(e):
        try:
            value = int(input_box.value)
            tree.insert(value)
            input_box.value = ""
            in_order_display.value = f"In-Order: {tree.in_order()}"
            tree_structure.value = tree.pretty()
            result_text.value = ""
            page.update()
        except ValueError:
            result_text.value = "❌ Ingresa un número válido"
            page.update()

    def search_click(e):
        try:
            value = int(search_box.value)
            found = tree.search(value)
            result_text.value = f"{value} {'✔️ encontrado' if found else '❌ no encontrado'}"
            page.update()
        except ValueError:
            result_text.value = "❌ Ingresa un número válido"
            page.update()

    insert_button.on_click = insert_click
    search_button.on_click = search_click

    page.add(
        ft.Column([
            ft.Text("Árbol Ternario de Búsqueda", size=24, weight="bold"),
            ft.Row([input_box, insert_button]),
            # Row for search input and button
            ft.Row([search_box, search_button]),
            result_text,
            in_order_display,
            ft.Text("Estructura del árbol:", weight="bold"),
            ft.Container(
                tree_structure,
                bgcolor=ft.Colors.BLACK12,
                padding=10,
                border_radius=5
            ),
        ])
    )

ft.app(target=main)