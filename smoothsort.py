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