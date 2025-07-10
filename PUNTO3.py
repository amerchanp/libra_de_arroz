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


