def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                # Intercambio
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    return lista

numeros = [5, 2, 9, 1, 5, 6]
print("Lista ordenada:", bubble_sort(numeros))


