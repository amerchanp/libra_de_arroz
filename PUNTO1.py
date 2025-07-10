def calcular_promedio(lista):
    suma = 0
    for numero in lista:
        suma += numero
    promedio = suma / len(lista)
    return promedio

numeros = [3.2, 4.5, 1.7, 6.0]
print("Promedio:", calcular_promedio(numeros))
