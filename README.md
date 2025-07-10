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
Bubble sort es un algoritmo de ordenamiento que funciona comparando elementos que están uno al lado del otro y los intercambia si están en el orden incorrecto. Esto se hace varias veces, y en cada pasada los valores más grandes van quedando al final, como si fueran burbujas subiendo a la superficie. A pesar de que no es el algoritmo más rápido que existe, es muy fácil de entender y es útil para aprender cómo funcionan los procesos de ordenamiento paso a paso. Me pareció interesante cómo, con solo unas cuantas líneas de código y ciclos anidados, se puede ordenar una lista completa. Para entenderlo mejor, hice una versión en Python y la probé con una lista desordenada, solo para ver cómo se comportaba y reforzar lo que había leído.

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
