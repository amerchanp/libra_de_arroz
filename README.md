# RETO 9

## EJERCICIO 1
En este ejercicio necesitaba calcular el promedio de una lista de números reales. Lo que hice fue recorrer la lista con un for y sumar todos los elementos en una variable llamada suma. Luego simplemente dividí esa suma entre la cantidad de elementos usando len(lista), y así obtuve el promedio. Todo esto lo metí dentro de una función para que fuera más reutilizable. La prueba la hice con una lista de ejemplo que contiene decimales.

```
def calcular_promedio(lista):
    suma = 0
    for numero in lista:
        suma += numero
    promedio = suma / len(lista)
    return promedio

numeros = [3.2, 4.5, 1.7, 6.0]
print("Promedio:", calcular_promedio(numeros))
```

## EJERCICIO 2
Aquí tocaba hacer el producto punto de dos arreglos del mismo tamaño. Como se trata de multiplicar elemento a elemento y luego sumar los resultados, usé un for con range(len(lista1)) para acceder a los índices. En cada vuelta, multiplico los elementos que están en la misma posición y se los voy sumando a una variable resultado. Así obtengo el producto punto final. Lo probé con dos listas simples de números enteros para verificar que todo funcione bien.

```
def producto_punto(lista1, lista2):
    resultado = 0
    for i in range(len(lista1)):
        resultado += lista1[i] * lista2[i]
    return resultado

a = [1, 2, 3]
b = [4, 5, 6]
print("Producto punto:", producto_punto(a, b))
```

## EJERCICIO 3
La idea de este era reorganizar una lista de números para que todos los ceros quedaran al final, sin importar dónde estaban antes. Lo que hice fue crear una nueva lista donde voy metiendo solo los números que no son cero. Al mismo tiempo, cuento cuántos ceros hay. Al final, simplemente le agrego a la nueva lista la cantidad de ceros que conté. Con eso logro que todos los ceros terminen al final sin alterar el orden del resto.

```
def mover_ceros_al_final(lista):
    nueva_lista = []
    ceros = 0
    for numero in lista:
        if numero == 0:
            ceros += 1
        else:
            nueva_lista.append(numero)
    nueva_lista.extend([0] * ceros)
    return nueva_lista

numeros = [0, 1, 0, 3, 12]
print("Resultado:", mover_ceros_al_final(numeros))
```

## EJERCICIO 4
Este último ejercicio era para entender cómo funciona el algoritmo de bubble sort. Lo que hace este método es comparar elementos vecinos y los intercambia si están en el orden incorrecto. Eso se repite varias veces hasta que toda la lista queda ordenada. Usé dos ciclos for: uno externo para repetir el proceso varias veces, y otro interno para hacer las comparaciones entre pares de elementos. Aunque no es el más eficiente, es bueno para entender cómo funcionan los algoritmos de ordenamiento básicos.

```
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
```

Muchas gracias.
