def producto_punto(lista1, lista2):
    resultado = 0
    for i in range(len(lista1)):
        resultado += lista1[i] * lista2[i]
    return resultado

a = [1, 2, 3]
b = [4, 5, 6]
print("Producto punto:", producto_punto(a, b))



