
def heapify(arr, n ,i): #Funcion heapify, tambien se puede importar de la libreria heapq
    
    largest = i #Se establece el nodo mas grande como el nodo raiz
    left = 2 * i + 1 
    right = 2 * i + 2 

    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] #Se intercambia el nodo raiz con el nodo mas grande
        heapify(arr, n, largest)

def heapsort(arr): #Funcion principal que ordena el arreglo
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1): 
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Arreglo desordenado es:", arr)
    heapsort(arr)
    print("Arreglo ordenado es:", arr) 

