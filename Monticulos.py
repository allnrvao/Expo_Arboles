import flet as ft
import heapq
import math

class MinHeapApp:
    def __init__(self):
        self.heap = []

    def main(self, page: ft.Page):
        page.title = "Montículo Mínimo (Min Heap)"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.vertical_alignment = ft.MainAxisAlignment.START
        self.page = page

        self.input_number = ft.TextField(label="Número a insertar", width=200)
        self.heap_display = ft.Text("Montículo: []", size=20)
        self.heap_stack = ft.Stack(width=800, height=400)

        insert_button = ft.ElevatedButton("Insertar", on_click=self.insert_number)
        delete_button = ft.ElevatedButton("Eliminar mínimo", on_click=self.delete_minimum)

        controls = ft.Column([
            self.input_number,
            ft.Row([insert_button, delete_button]),
            self.heap_display,
            self.heap_stack
        ])

        page.add(controls)

    def insert_number(self, e):
        try:
            num = int(self.input_number.value)
            heapq.heappush(self.heap, num)
            self.input_number.value = ""
            self.update_heap_display()
            self.page.update()
        except ValueError:
            self.page.snack_bar = ft.SnackBar(ft.Text("Por favor ingrese un número válido."))
            self.page.snack_bar.open = True
            self.page.update()

    def delete_minimum(self, e):
        if self.heap:
            heapq.heappop(self.heap)
            self.update_heap_display()
            self.page.update()
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("El montículo está vacío."))
            self.page.snack_bar.open = True
            self.page.update()

    def update_heap_display(self):
        self.heap_display.value = f"Montículo: {self.heap}"
        self.draw_heap()

    def draw_heap(self):
        self.heap_stack.controls.clear()
        if not self.heap:
            return

        level_spacing = 80
        node_radius = 20
        canvas_width = 800

        for i, value in enumerate(self.heap):
            level = math.floor(math.log2(i + 1))
            max_nodes_in_level = 2 ** level
            index_in_level = i - (2 ** level - 1)
            x_gap = canvas_width / (max_nodes_in_level + 1)
            x = x_gap * (index_in_level + 1)
            y = level * level_spacing + 20

            # Nodo como círculo, ahora correctamente posicionado
            self.heap_stack.controls.append(
                ft.Container(
                    content=ft.Text(str(value), color=ft.Colors.WHITE, text_align=ft.TextAlign.CENTER),
                    width=node_radius * 2,
                    height=node_radius * 2,
                    border_radius=node_radius,
                    bgcolor=ft.Colors.BLUE,
                    alignment=ft.alignment.center,
                    left=x - node_radius,
                    top=y - node_radius
                )
            )

        self.page.update()

if __name__ == '__main__':
    app = MinHeapApp()
    ft.app(target=app.main)
