def ajustar_grupo(arr, inicio, tamano):
    raiz = arr[inicio]  # El número "padre"
    mayor = inicio
    # Miramos los "hijos" (números que están justo después)
    for i in range(1, min(tamano, len(arr) - inicio)):
        if arr[inicio + i] > arr[mayor]:
            mayor = inicio + i
    # Si un hijo es mayor, intercambiamos
    if mayor != inicio:
        arr[inicio], arr[mayor] = arr[mayor], arr[inicio]

def smoothsort(arr):
    print("Arreglo inicial:", arr)
    n = len(arr)
    
    # 1. Hacer un grupo (montículo) con todos los números
    # Suponemos un grupo de tamaño 3 (como L(2) = 3 en números de Leonardo)
    if n >= 3:
        ajustar_grupo(arr, 0, 3)  # Aseguramos que el mayor esté al principio
        print("Después de organizar grupo:", arr)
    
    # 2. Sacar el número más grande y ponerlo al final
    for i in range(n-1, -1, -1):
        if i >= 2:  # Si hay al menos 3 elementos, ajustar grupo
            arr[0], arr[i] = arr[i], arr[0]  # Poner el mayor al final
            ajustar_grupo(arr, 0, i)  # Reorganizar el grupo restante
            print(f"Paso {n-i}:", arr)
    
    print("Arreglo ordenado:", arr)
    return arr