def heapify(arr):
    n = len(arr)
    # Convertir arr en un montículo máximo
    for i in range(n//2 - 1, -1, -1):
        siftdown(arr, i, n)
def siftdown(arr, i, n):
    largest = i
    izq = 2*i + 1
    der = 2*i + 2
    if izq < n and arr[izq] > arr[largest]:
        largest = izq
    if der < n and arr[der] > arr[largest]:
        largest = der
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        siftdown(arr, largest, n)
# Uso: construir montículo máximo y extraer el máximo
arr = [3, 1, 6, 5, 2, 4]
heapify(arr)
print(arr)  # arr ahora reordenado como montículo (p.ej. [6,5,4,3,2,1])